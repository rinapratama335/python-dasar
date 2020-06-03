## Cara Kerja Program dan Bytecode

- Python merupakan bahasa pemrograman interpreted

- Setiap baris kode akan dieksekusi secara berurutan

- Komen, baris kosong, maupun multi komen akan diabakan (tidak diprogram)

- Untuk menjalakan program yang dibuat kita bisa ketikkan :

```
python nama_file.py
```

pada versi ini python diinstal di windows

### Membaut bytecode dari program python

Meskipun python adalah bahasa interpreted namun bisa juga kita membuatnya menjadi bahasa pemrograman compiler. Kita bisa membuat Bytecode dari programa yang kita buat. Caranya adalah :

```
python -m py_compile nama_file.py
```

maka akan terbentuk sebuah folder `__pycache__` yang didalamnya adalah program bytecode yang kita buat. Dan untuk menjalankannya kita bisa ketikkan :

```
python __pychahe__/nama_file.pyc
```

Hal ini belum akan terlihat jika kita hanya membuat program yang sederhana. Namun jika aplikasi yang kita buat sudah besar, maka dengan menjadikan python menjadi bytecode ini akan terasa manfaatnya karena akan menjadi lebih cepat.

Python adalah bahasa yang interpreted makanya akan menjadi lambat, hal itu tidak salah 100%, namun kita bisa mengantisipasi itu dengan menjadikannya sebagai compiler sehingga program akan lebih cepat.
