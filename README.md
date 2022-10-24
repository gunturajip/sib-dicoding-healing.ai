# Healing.ai

## Petunjuk Inisialisasi

1.  Buat direktori untuk menyimpan proyek ini
2.  Buka Git Bash pada direktori tersebut
3.  Clone proyek ini dengan perintah:

    ```
    git clone https://github.com/gunturajip/sib-dicoding-healing.ai.git
    ```

4.  Lalu buka folder proyek yang telah di-cloning sebelumnya dengan perintah:

    ```
    cd sib-dicoding-healing.ai/
    ```

5.  Buka folder proyek dengan VS Code dengan perintah:

    ```
    code .
    ```

## Petunjuk Pembaharuan Kode

1.  Pada folder proyek, buka Git Bash dan ketikkan perintah:

    ```
    git add *
    ```

2.  Perlu diingat, di setiap pembaharuan kode harus diberi pesan Commit yang jelas seperti perintah:
    (Pesan Commit harus sesuai dengan proses yang dilakukan, dalam hal ini "edit petunjuk inisialisasi")

    ```
    git commit -m "edit petunjuk inisialisasi"
    ```

3.  Terakhir, Push pembaharuan kode dengan perintah:
    (Push pembaruan kode bisa dilakukan di Branch manapun yang tersedia, dalam hal ini di Branch "main")

    ```
    git push origin main
    ```

4.  Jika ingin melakukan Push di Branch selain "main", bisa mengetikkan perintah:
    (Ingin pindah ke Branch "back-end-ml")

    ```
    git checkout -b "back-end-ml"
    ```

    Dan jika ingin kembali lagi ke Branch "main, bisa mengetikkan perintah:

    ```
    git checkout "main"
    ```

5.  Jika ingin melakukan Update dari seluruh kode yang dilakukan Contributor lain dalam suatu Branch, bisa mengetikkan perintah:
    (Ingin Update seluruh kode dari Branch "main")

    ```
    git pull origin main
    ```
