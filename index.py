# import library
from flask import Flask, request
import pandas as pd
# from flask_cors import CORS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# inisiasi object flask
app = Flask(__name__)
taman = pd.read_csv("taman.csv")
museum = pd.read_csv("museum.csv")

# inisiasi object flask_cors
# CORS(app)

# inisiasi variabel kosong bertipe dictionary (= json)
identitas = {}


@app.route("/api", methods=["GET"])
def get():
    return identitas


@app.route("/api", methods=["POST"])
def post():
    global identitas
    identitas = {}
    keyword = request.form["keyword"]
    hasil_taman = rekomendasi_taman(keyword)
    hasil_museum = rekomendasi_museum(keyword)
    if type(hasil_taman) == str and type(hasil_museum) == str:
        identitas[0] = hasil_taman
    else:
        if type(hasil_taman) == str:
            loop_hasi_rekomendasi(hasil_museum, 0)
        elif type(hasil_museum) == str:
            loop_hasi_rekomendasi(hasil_taman, 0)
        else:
            loop_hasi_rekomendasi(hasil_taman, 0)
            loop_hasi_rekomendasi(hasil_museum, len(identitas))

    return identitas


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
    nama_terbaik = [0, ""]
    for i in taman["nama"]:
        count = 0
        for j in nama.lower().split():
            if j in i.lower().split():
                count += 1
        if count >= 1 and nama_terbaik[0] < count:
            nama_terbaik[0] = count
            nama_terbaik[1] = i
    if nama_terbaik[1] == "":
        return "Tidak ada rekomendasi"
    nama = nama_terbaik[1]

    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan
    # Dataframe diubah menjadi numpy
    # Range(start, stop, step)
    index = similarity_data.loc[:, nama].to_numpy(
    ).argpartition(range(-1, -k, -1))

    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]

    # Drop nama agar nama data yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(nama, errors='ignore')

    # Menambahkan data sesuai keyword pencarian sebagai data pertama
    matched = taman[taman["nama"] == nama]

    return pd.concat([matched, pd.DataFrame(closest).merge(items).loc[:]]).reset_index(drop=True).reset_index()


def rekomendasi_museum(nama):
    # Inisialisasi TfidfVectorizer
    tf = TfidfVectorizer()

    # Melakukan fit lalu ditransformasikan ke bentuk dataframe
    tfidf_matrix = tf.fit_transform(museum['kecamatan'])

    # Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
    tfidf_matrix.todense()

    # Menghitung cosine similarity pada matrix tf-idf
    cosine_sim = cosine_similarity(tfidf_matrix)

    # Membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa nama
    cosine_sim_df = pd.DataFrame(
        cosine_sim, index=museum['nama'], columns=museum['nama'])

    # Membuat finalisasi rekomendasi data untuk Content-Based Filtering
    similarity_data = cosine_sim_df
    items = museum[['nama', 'kategori', 'rating',
                   'kecamatan', 'kota', 'provinsi', 'alamat', 'link']]
    k = 20

    # Melakukan matching data pertama yang paling mirip dengan parameter nama
    nama_terbaik = [0, ""]
    for i in museum["nama"]:
        count = 0
        for j in nama.lower().split():
            if j in i.lower().split():
                count += 1
        if count >= 1 and nama_terbaik[0] < count:
            nama_terbaik[0] = count
            nama_terbaik[1] = i
    if nama_terbaik[1] == "":
        return "Tidak ada rekomendasi"
    nama = nama_terbaik[1]

    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan
    # Dataframe diubah menjadi numpy
    # Range(start, stop, step)
    index = similarity_data.loc[:, nama].to_numpy(
    ).argpartition(range(-1, -k, -1))

    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]

    # Drop nama agar nama data yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(nama, errors='ignore')

    # Menambahkan data sesuai keyword pencarian sebagai data pertama
    matched = museum[museum["nama"] == nama]

    return pd.concat([matched, pd.DataFrame(closest).merge(items).loc[:]]).reset_index(drop=True).reset_index()


def loop_hasi_rekomendasi(data, start_index):
    for index in range(len(data)):
        identitas[int(data.loc[index, "index"])+start_index+1] = {'nama': data.loc[index, "nama"], 'kategori': data.loc[index, "kategori"], 'rating': int(data.loc[index, "rating"]),
                                                                  'kecamatan': data.loc[index, "kecamatan"], 'kota': data.loc[index, "kota"], 'provinsi': data.loc[index, "provinsi"], 'alamat': data.loc[index, "alamat"], 'link': data.loc[index, "link"]}


if __name__ == "__main__":
    app.run()
