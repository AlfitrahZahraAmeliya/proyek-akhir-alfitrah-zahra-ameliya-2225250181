# PROPOSAL PROYEK
# PROGRAM GENERATOR SOAL PERSAMAAN LINEAR SATU VARIABEL

## Identitas Mahasiswa

- Nama: Alfitrah Zahra Ameliya
- NIM: 2225250181
- Kelas: 3B

## 1. Judul Proyek

Program Generator Soal Persamaan Linear Satu Variabel

## 2. Latar Belakang

Persamaan Linear Satu Variabel (PLSV) merupakan salah satu materi matematika yang perlu dipahami dan dilatih oleh siswa. Dalam proses pembelajaran, siswa membutuhkan latihan soal yang bervariasi serta umpan balik untuk mengetahui apakah jawaban yang diberikan sudah benar.

Oleh karena itu, dirancang sebuah program sederhana menggunakan bahasa pemrograman Python yang dapat menghasilkan soal Persamaan Linear Satu Variabel secara otomatis, memeriksa jawaban siswa, dan menampilkan skor latihan. Program ini diharapkan dapat membantu siswa berlatih secara mandiri dengan cara yang sederhana dan mudah digunakan melalui terminal.

## 3. Pengguna dan Tujuan

### Pengguna

Pengguna utama program ini adalah siswa yang sedang mempelajari materi Persamaan Linear Satu Variabel.

### Tujuan

1. Membantu siswa berlatih menyelesaikan soal Persamaan Linear Satu Variabel.
2. Menghasilkan variasi soal secara otomatis.
3. Memeriksa kebenaran jawaban siswa.
4. Menampilkan skor sebagai evaluasi hasil latihan.

## 4. Ruang Lingkup

### Fitur Wajib

1. Program menghasilkan soal Persamaan Linear Satu Variabel secara otomatis.
2. Program menampilkan soal melalui terminal.
3. Program menerima dan memeriksa jawaban siswa.
4. Program menghitung dan menampilkan skor akhir latihan.

### Fitur Tambahan

Program dapat menampilkan pembahasan atau penyelesaian soal setelah latihan selesai apabila waktu pengembangan memungkinkan.

### Batasan Proyek

1. Program menggunakan bahasa Python.
2. Program dijalankan melalui terminal atau console.
3. Soal dibatasi pada persamaan berbentuk ax + b = c dengan a tidak sama dengan nol.
4. Jawaban yang diperiksa berupa bilangan bulat.
5. Program tidak menggunakan database, antarmuka web, atau layanan eksternal.

## 5. Analisis Kebutuhan

### A. Kebutuhan Fungsional

| ID | Kebutuhan | Prioritas |
|---|---|---|
| F01 | Program menghasilkan soal PLSV secara otomatis. | Wajib |
| F02 | Program menampilkan soal kepada pengguna. | Wajib |
| F03 | Program menerima dan memeriksa jawaban pengguna. | Wajib |
| F04 | Program menghitung dan menampilkan skor akhir. | Wajib |
| F05 | Program menampilkan pembahasan soal. | Tambahan |

### B. Kebutuhan Nonfungsional

1. Program mudah dijalankan melalui terminal VS Code.
2. Pesan dan petunjuk penggunaan mudah dipahami.
3. Nama variabel dan fungsi menggambarkan tugasnya dengan jelas.
4. Program menangani masukan yang tidak sesuai dengan pesan kesalahan yang mudah dipahami.
5. Program dapat diuji menggunakan contoh soal dan jawaban yang telah ditentukan.

## 6. IPO (Input, Process, Output)

### Input

1. Pilihan jumlah soal latihan.
2. Jawaban siswa untuk setiap soal.

### Process

1. Program menentukan koefisien dan konstanta untuk membentuk soal PLSV.
2. Program menghasilkan soal dengan jawaban bilangan bulat.
3. Program menampilkan soal kepada siswa.
4. Program menerima jawaban siswa.
5. Program membandingkan jawaban siswa dengan jawaban yang benar.
6. Program menambahkan skor apabila jawaban benar.
7. Program menghitung dan menampilkan hasil akhir latihan.

### Output

1. Soal Persamaan Linear Satu Variabel.
2. Informasi benar atau salah untuk setiap jawaban.
3. Jumlah jawaban benar dan salah.
4. Skor akhir latihan.

## 7. Algoritma

### Pseudocode

```text
MULAI

Tampilkan judul program
Minta pengguna memasukkan jumlah soal

Jika jumlah soal tidak valid:
    Tampilkan pesan kesalahan
    Minta masukan yang valid

Inisialisasi skor = 0

ULANGI sebanyak jumlah soal:
    Hasilkan soal PLSV
    Tentukan jawaban yang benar
    Tampilkan soal
    Minta jawaban pengguna

    Jika jawaban pengguna tidak valid:
        Tampilkan pesan kesalahan
        Minta jawaban kembali

    Jika jawaban pengguna benar:
        Tambahkan skor
        Tampilkan pesan benar
    Jika tidak:
        Tampilkan pesan salah

Hitung hasil akhir
Tampilkan jumlah jawaban benar dan salah
Tampilkan skor akhir

SELESAI
```

## 8. Struktur Program

Struktur folder dirancang berdasarkan contoh struktur program pada bahan ajar Pertemuan 14 dengan penyesuaian terhadap fungsi proyek generator soal.

```text
proyek-akhir-alfitrah-zahra-ameliya-2225250181/
|
|-- README.md
|-- proposal.md
|-- .gitignore
|
|-- data/
|   `-- contoh_soal.txt
|
|-- src/
|   |-- main.py
|   |-- data_io.py
|   |-- analisis.py
|   `-- utilitas.py
|
|-- tests/
|   `-- test_case.md
|
`-- output/
    `-- .gitkeep
```

### Tanggung Jawab Modul

- `main.py`: mengatur alur utama program.
- `data_io.py`: menangani masukan pengguna dan tampilan soal atau hasil.
- `analisis.py`: menangani pembentukan soal PLSV, penentuan jawaban benar, pemeriksaan jawaban, dan perhitungan skor.
- `utilitas.py`: menyediakan fungsi pendukung seperti validasi masukan.
- `contoh_soal.txt`: menyimpan contoh soal untuk referensi pengujian.
- `test_case.md`: mendokumentasikan skenario pengujian.
- `README.md`: menjelaskan deskripsi proyek dan cara menjalankan program.
- `proposal.md`: menyimpan rancangan proyek.
- `.gitignore`: menentukan file atau folder yang tidak perlu dimasukkan ke Git.
- `.gitkeep`: menjaga agar folder `output` tetap tercatat dalam repository.

## 9. Struktur Data

| Struktur Data | Penggunaan | Alasan |
|---|---|---|
| Integer | Menyimpan koefisien, konstanta, jawaban, jumlah soal, dan skor. | Sesuai untuk operasi aritmetika dan perhitungan skor. |
| String | Menyimpan teks soal dan pesan kepada pengguna. | Memudahkan penampilan informasi melalui terminal. |
| List | Menyimpan kumpulan soal atau hasil latihan. | Memudahkan pengolahan beberapa soal dalam satu sesi. |
| Dictionary | Menyimpan informasi soal, seperti koefisien, konstanta, dan jawaban benar. | Mengelompokkan beberapa atribut soal dalam satu struktur data. |
| Boolean | Menyatakan apakah jawaban pengguna benar atau salah. | Memudahkan pemeriksaan jawaban dan penentuan skor. |

## 10. Test Case

Pengujian awal dirancang sebelum implementasi penuh untuk memastikan fitur program dapat berjalan sesuai kebutuhan.

| ID | Kategori | Input/Kondisi | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Normal | Soal 2x + 4 = 10, jawaban 3. | Jawaban dinyatakan benar dan skor bertambah. |
| TC02 | Normal | Soal 3x + 2 = 11, jawaban 2. | Jawaban dinyatakan benar dan skor bertambah. |
| TC03 | Normal | Soal 2x + 4 = 10, jawaban 4. | Jawaban dinyatakan salah dan skor tidak bertambah. |
| TC04 | Batas | Pengguna memilih jumlah soal sebanyak 1. | Program menjalankan satu soal latihan. |
| TC05 | Invalid | Pengguna memasukkan jumlah soal 0. | Program menolak masukan dan menampilkan pesan kesalahan. |
| TC06 | Invalid | Pengguna memasukkan teks ketika diminta jawaban angka. | Program menampilkan pesan kesalahan dan meminta jawaban yang valid. |
| TC07 | Normal | Semua jawaban dalam latihan benar. | Skor akhir sesuai dengan jumlah jawaban benar. |

## 11. Pembagian Tugas

Proyek dikerjakan secara individu. Oleh karena itu, seluruh tugas perancangan, implementasi, pengujian, dan dokumentasi menjadi tanggung jawab mahasiswa.

| Peran | Tanggung Jawab |
|---|---|
| Perancang/Koordinator | Menentukan masalah, ruang lingkup, kebutuhan, dan rancangan proyek. |
| Programmer | Mengembangkan program dan mengintegrasikan modul. |
| Tester/QA | Menyusun dan menjalankan test case serta memeriksa hasil program. |
| Dokumentasi | Menyusun proposal, README, dan catatan pengujian. |

Nama penanggung jawab seluruh peran: Alfitrah Zahra Ameliya.

## 12. Jadwal Pelaksanaan

| Tahap | Target Kegiatan |
|---|---|
| Pertemuan 14 | Menyelesaikan proposal, kebutuhan, IPO, pseudocode, struktur program, struktur data, test case, dan repository GitHub. |
| Antara Pertemuan 14–15 | Membuat implementasi awal fitur wajib. |
| Pertemuan 15 | Melakukan integrasi, pengujian, debugging, dan melengkapi dokumentasi. |
| Pertemuan 16 | Mempersiapkan presentasi, demonstrasi program, dan evaluasi proyek. |

## 13. Repository GitHub

Repository proyek:

https://github.com/AlfitrahZahraAmeliya/proyek-akhir-alfitrah-zahra-ameliya-2225250181

Repository digunakan untuk menyimpan rancangan, kode program, test case, dokumentasi, serta riwayat perubahan proyek.

## Penutup

Program Generator Soal Persamaan Linear Satu Variabel dirancang sebagai proyek pembelajaran matematika sederhana berbasis Python. Perancangan ini mencakup identifikasi masalah, kebutuhan pengguna, ruang lingkup, IPO, algoritma, struktur program, struktur data, test case, jadwal, dan dokumentasi. Rancangan tersebut menjadi dasar untuk implementasi dan pengujian pada tahap berikutnya.

## Referensi

Bahan Ajar Algoritma dan Pemrograman, Pertemuan 14: Perancangan Proyek Program Sederhana Masalah Matematika/Pembelajaran Matematika, VS Code, dan GitHub. Program Studi S1 Pendidikan Matematika, FKIP, Universitas Sultan Ageng Tirtayasa, Tahun Akademik 2026/2027 Ganjil.