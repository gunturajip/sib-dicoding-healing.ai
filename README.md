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

3.  Terakhir, Push pembaruan kode bisa dilakukan di Branch manapun yang tersedia.

    Jika ingin Push pembaharuan kode di Branch "main", bisa mengetikkan perintah:

    ```
    git push origin main
    ```

    Jika ingin Push pembaharuan kode di Branch "back-end-ml", bisa mengetikkan perintah:

    ```
    git push origin back-end-ml
    ```

    Jika ingin Push pembaharuan kode di Branch "front-end", bisa mengetikkan perintah:

    ```
    git push origin front-end
    ```

4.  Jika ingin melakukan Push di Branch selain "main", perlu melakukan perpindahan Branch terlebih dahulu ke Branch yang dipilih.

    Jika ingin pindah ke Branch "back-end-ml", bisa mengetikkan perintah:

    ```
    git checkout -b back-end-ml
    ```

    Dan jika ingin kembali lagi ke Branch "main", bisa mengetikkan perintah:

    ```
    git checkout main
    ```

    Dan jika ingin kembali lagi ke Branch "back-end-ml", cukup mengetikkan perintah:

    ```
    git checkout back-end-ml
    ```

5.  Jika ingin melakukan Update dari seluruh kode yang dilakukan Contributor lain dalam suatu Branch, perlu melakukan Pull terlebih dahulu di Branch yang dipilih.

    Jika Update seluruh kode dari Branch "main", bisa mengetikkan perintah:

    ```
    git pull origin main
    ```

    Jika Update seluruh kode dari Branch "back-end-ml", bisa mengetikkan perintah:

    ```
    git pull origin back-end-ml
    ```

    Jika Update seluruh kode dari Branch "front-end", bisa mengetikkan perintah:

    ```
    git pull origin front-end
    ```
