# import library
from flask import Flask, request
from flask_cors import CORS
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# inisiasi object flask
app = Flask(__name__)
taman = pd.read_csv("taman.csv")
museum = pd.read_csv("museum_csv")

# inisiasi object flask_cors
CORS(app)

# inisiasi variabel kosong bertipe dictionary (= json)
identitas = {}


@app.route("/api", methods=["GET"])
def get():
    return identitas


@app.route("/api", methods=["POST"])
def post():
    keyword = request.form["keyword"]
    result = rekomendasi_taman(keyword)
    identitas["keyword"] = result
    response = {"msg": "data berhasil dimasukkan"}
    return response


def rekomendasi_taman(nama):
    # Inisialisasi TfidfVectorizer
    tf = TfidfVectorizer()

    # Melakukan fit lalu ditransformasikan ke bentuk dataframe
    tfidf_matrix = tf.fit_transform(taman['kecamatan'])

    # Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
    tfidf_matrix.todense()

    # Menghitung cosine similarity pada matrix tf-idf
    cosine_sim = cosine_similarity(tfidf_matrix)

    # Membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa nama
    cosine_sim_df = pd.DataFrame(
        cosine_sim, index=taman['nama'], columns=taman['nama'])

    # Membuat finalisasi rekomendasi data untuk Content-Based Filtering
    similarity_data = cosine_sim_df
    items = taman[['nama', 'kategori', 'rating',
                   'kecamatan', 'kota', 'provinsi', 'alamat', 'link']]
    k = 20

    # Melakukan matching data pertama yang paling mirip dengan parameter nama
    for i in taman["nama"]:
        count = 0
        for j in nama.lower().split():
            if j in i.lower().split():
                count += 1
        if count == len(nama.split()):
            nama = i
            break
    else:
        return "Tidak ada rekomendasi"

    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan
    # Dataframe diubah menjadi numpy
    # Range(start, stop, step)
    index = similarity_data.loc[:, nama].to_numpy(
    ).argpartition(range(-1, -k, -1))

    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]

    # Drop nama agar nama data yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(nama, errors='ignore')

    return pd.DataFrame(closest).merge(items).to_json()


if __name__ == "__main__":
    app.run()
