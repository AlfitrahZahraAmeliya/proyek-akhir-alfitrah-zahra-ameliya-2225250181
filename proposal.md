# PROPOSAL PROYEK

# PROGRAM GENERATOR SOAL PERSAMAAN LINEAR SATU VARIABEL (PLSV)

## Identitas Mahasiswa

- **Nama:** Alfitrah Zahra Ameliya
- **NIM:** 2225250181
- **Kelas:** 3B

## 1. Judul Proyek

Program Generator Soal Persamaan Linear Satu Variabel (PLSV).

## 2. Latar Belakang

Persamaan Linear Satu Variabel (PLSV) merupakan salah satu materi matematika yang perlu dipahami dan dilatih oleh siswa. Dalam proses pembelajaran, siswa membutuhkan latihan soal yang bervariasi serta umpan balik untuk mengetahui apakah jawaban yang diberikan sudah benar.

Oleh karena itu, dirancang program sederhana menggunakan bahasa pemrograman Python yang dapat menghasilkan soal PLSV secara otomatis, memeriksa jawaban siswa, dan menampilkan nilai akhir latihan. Program dijalankan melalui terminal agar sederhana dan mudah digunakan.

## 3. Pengguna dan Tujuan

### 3.1 Pengguna

Pengguna utama program ini adalah siswa yang sedang mempelajari materi Persamaan Linear Satu Variabel.

### 3.2 Tujuan

1. Membantu siswa berlatih menyelesaikan soal PLSV.
2. Menghasilkan variasi soal secara otomatis.
3. Memeriksa kebenaran jawaban siswa.
4. Menampilkan hasil dan nilai akhir latihan.

## 4. Ruang Lingkup

### 4.1 Fitur Wajib

1. Program menghasilkan soal PLSV secara otomatis.
2. Program menampilkan soal melalui terminal.
3. Program menerima dan memeriksa jawaban siswa.
4. Program menghitung dan menampilkan nilai akhir latihan.

### 4.2 Fitur Tambahan

Program dapat menampilkan pembahasan atau langkah penyelesaian soal apabila waktu pengembangan memungkinkan.

### 4.3 Batasan Proyek

1. Program menggunakan bahasa pemrograman Python.
2. Program dijalankan melalui terminal atau console.
3. Soal menggunakan bentuk persamaan \(ax+b=c\), dengan \(a\neq0\).
4. Soal dirancang agar memiliki jawaban berupa bilangan bulat.
5. Program tidak menggunakan database, antarmuka web, atau layanan eksternal.
6. Program digunakan oleh satu pengguna dalam satu sesi latihan.
7. Jumlah soal yang dapat dipilih adalah 1 sampai 10 soal.

## 5. Analisis Kebutuhan

### 5.1 Kebutuhan Fungsional

| ID | Kebutuhan | Prioritas |
|---|---|---|
| F01 | Program menghasilkan soal PLSV secara otomatis. | Wajib |
| F02 | Program menampilkan soal melalui terminal. | Wajib |
| F03 | Program menerima dan memeriksa jawaban pengguna. | Wajib |
| F04 | Program menghitung dan menampilkan nilai akhir. | Wajib |
| F05 | Program menampilkan pembahasan soal. | Tambahan |

### 5.2 Kebutuhan Nonfungsional

1. Program dapat dijalankan melalui terminal menggunakan Python.
2. Pesan dan petunjuk penggunaan mudah dipahami.
3. Nama variabel dan fungsi menggambarkan tugasnya dengan jelas.
4. Program menangani masukan yang tidak valid dengan menampilkan pesan kesalahan.
5. Program dapat diuji menggunakan skenario pengujian yang telah disusun.

## 6. IPO (Input, Process, Output)

### 6.1 Input

1. Jumlah soal yang ingin dikerjakan pengguna.
2. Jawaban pengguna untuk setiap soal.

### 6.2 Process

1. Program menerima jumlah soal dari pengguna.
2. Program memvalidasi jumlah soal agar berada pada rentang 1 sampai 10.
3. Program menentukan koefisien dan konstanta untuk menghasilkan soal PLSV.
4. Program menentukan jawaban benar untuk setiap soal.
5. Program menampilkan soal melalui terminal.
6. Program menerima dan memvalidasi jawaban pengguna.
7. Program membandingkan jawaban pengguna dengan jawaban yang benar.
8. Program menghitung jumlah jawaban benar dan salah.
9. Program menghitung nilai akhir berdasarkan jumlah jawaban benar dan jumlah soal.

### 6.3 Output

1. Soal PLSV yang dihasilkan.
2. Informasi benar atau salah untuk setiap jawaban.
3. Jawaban yang benar apabila jawaban pengguna salah.
4. Jumlah jawaban benar dan salah.
5. Nilai akhir latihan dalam rentang 0–100.

## 7. Algoritma

### 7.1 Pseudocode

```text
MULAI

Tampilkan judul program

Minta pengguna memasukkan jumlah soal

SELAMA jumlah soal tidak valid
    Tampilkan pesan kesalahan
    Minta pengguna memasukkan jumlah soal kembali
SELESAI SELAMA

Inisialisasi jumlah benar = 0

UNTUK setiap nomor soal dari 1 sampai jumlah soal
    Hasilkan soal PLSV
    Tentukan jawaban yang benar
    Tampilkan soal

    Minta pengguna memasukkan jawaban

    SELAMA jawaban bukan bilangan bulat yang valid
        Tampilkan pesan kesalahan
        Minta pengguna memasukkan jawaban kembali
    SELESAI SELAMA

    JIKA jawaban pengguna sama dengan jawaban benar
        Tambahkan jumlah benar
        Tampilkan pesan jawaban benar
    JIKA TIDAK
        Tampilkan pesan jawaban salah
        Tampilkan jawaban yang benar
    SELESAI JIKA
SELESAI UNTUK

Hitung jumlah salah
Hitung nilai akhir

Tampilkan jumlah soal
Tampilkan jumlah jawaban benar
Tampilkan jumlah jawaban salah
Tampilkan nilai akhir

SELESAI
```

### 7.2 Rumus Perhitungan Nilai

Nilai akhir dihitung menggunakan rumus:

\[
\text{Nilai Akhir}
=
\frac{\text{Jumlah Jawaban Benar}}
{\text{Jumlah Soal}}\times100
\]

Rumus digunakan apabila jumlah soal lebih besar dari nol.

## 8. Struktur Program

Struktur folder proyek disusun berdasarkan kebutuhan program dan disesuaikan dengan rancangan proyek pada bahan ajar Pertemuan 14.

```text
proyek-akhir-alfitrah-zahra-ameliya-2225250181/
|
|-- README.md
|-- proposal.md
|-- .gitignore
|
|-- data/
|   `-- nilai_contoh.txt
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

### 8.1 Tanggung Jawab Modul

- **`main.py`**: mengatur alur utama program dan menghubungkan fungsi dari modul lainnya.
- **`data_io.py`**: menangani masukan pengguna, termasuk jumlah soal dan jawaban.
- **`analisis.py`**: menghasilkan soal PLSV, menentukan jawaban benar, memeriksa jawaban, dan menghitung nilai.
- **`utilitas.py`**: menyediakan fungsi pendukung untuk menampilkan judul, garis pemisah, dan ringkasan hasil latihan.
- **`data/nilai_contoh.txt`**: menyimpan contoh soal sebagai referensi.
- **`tests/test_case.md`**: mendokumentasikan skenario pengujian dan hasil yang diharapkan.
- **`README.md`**: menjelaskan deskripsi, fitur, struktur, dan informasi proyek.
- **`proposal.md`**: menyimpan rancangan proyek.
- **`.gitignore`**: menentukan file atau folder yang tidak perlu dimasukkan ke Git.
- **`output/.gitkeep`**: menjaga agar folder `output` tetap tercatat dalam repository.

## 9. Struktur Data

| Struktur Data | Penggunaan | Alasan |
|---|---|---|
| Integer | Menyimpan koefisien, konstanta, jawaban, jumlah soal, dan jumlah jawaban benar. | Sesuai untuk operasi aritmetika dan perhitungan nilai. |
| String | Menyimpan teks soal dan pesan kepada pengguna. | Memudahkan penampilan informasi melalui terminal. |
| List | Belum digunakan dalam implementasi awal. Dapat digunakan pada pengembangan selanjutnya untuk menyimpan kumpulan soal atau hasil latihan. | Dapat memudahkan pengolahan beberapa soal jika fitur tersebut dikembangkan. |
| Dictionary | Menyimpan informasi soal, seperti teks soal dan jawaban benar. | Mengelompokkan beberapa atribut soal dalam satu struktur. |
| Boolean | Menyatakan apakah jawaban pengguna benar atau salah. | Memudahkan pemeriksaan jawaban. |

## 10. Test Case

Pengujian awal dirancang sebelum implementasi penuh. Pengujian aktual dilakukan setelah program selesai diimplementasikan.

| ID | Kategori | Input/Kondisi | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Normal | Soal \(2x+4=10\), jawaban pengguna 3. | Program menyatakan jawaban benar dan menambah jumlah jawaban benar. |
| TC02 | Jawaban salah | Soal \(2x+4=10\), jawaban pengguna 2. | Program menyatakan jawaban salah dan menampilkan jawaban benar, yaitu 3. |
| TC03 | Jawaban salah | Soal \(2x+4=10\), jawaban pengguna 4. | Program menyatakan jawaban salah dan menampilkan jawaban benar, yaitu 3. |
| TC04 | Batas | Pengguna memasukkan jumlah soal 1. | Program menerima masukan dan menghasilkan satu soal. |
| TC05 | Invalid | Pengguna memasukkan jumlah soal 0. | Program menolak masukan dan meminta jumlah soal yang valid. |
| TC06 | Invalid | Pengguna memasukkan teks `abc` ketika diminta jawaban angka. | Program menampilkan pesan kesalahan dan meminta jawaban numerik yang valid. |
| TC07 | Normal | Semua soal dijawab dengan benar. | Nilai akhir yang ditampilkan adalah 100. |

Hasil aktual setiap pengujian akan dicatat dan dibandingkan dengan hasil yang diharapkan untuk mengetahui apakah program berjalan sesuai kebutuhan.

## 11. Pembagian Tugas

Proyek dikerjakan secara individu. Oleh karena itu, seluruh tugas perancangan, implementasi, pengujian, dan dokumentasi menjadi tanggung jawab mahasiswa.

| Peran | Tanggung Jawab |
|---|---|
| Perancang/Koordinator | Menentukan masalah, ruang lingkup, kebutuhan, dan rancangan proyek. |
| Programmer | Mengembangkan program dan mengintegrasikan modul. |
| Tester/QA | Menyusun serta menjalankan test case dan memeriksa hasil program. |
| Dokumentasi | Menyusun proposal, README, dan catatan pengujian. |

**Nama penanggung jawab seluruh peran:** Alfitrah Zahra Ameliya.

## 12. Jadwal Pelaksanaan

| Tahap | Target Kegiatan |
|---|---|
| Pertemuan 14 | Menyelesaikan proposal, analisis kebutuhan, IPO, pseudocode, struktur program, struktur data, test case, pembagian tugas, jadwal, dan repository GitHub. |
| Antara Pertemuan 14–15 | Mengembangkan implementasi awal fitur wajib berdasarkan rancangan. |
| Pertemuan 15 | Melakukan integrasi, pengujian, debugging, dan melengkapi dokumentasi berdasarkan hasil implementasi. |
| Pertemuan 16 | Mempersiapkan presentasi, demonstrasi program, dan evaluasi proyek. |

## 13. Repository GitHub

Repository proyek:

https://github.com/AlfitrahZahraAmeliya/proyek-akhir-alfitrah-zahra-ameliya-2225250181

Repository digunakan untuk menyimpan rancangan, kode program, test case, dokumentasi, dan riwayat perubahan proyek.

## Penutup

Program Generator Soal Persamaan Linear Satu Variabel dirancang sebagai proyek pembelajaran matematika sederhana berbasis Python. Rancangan ini mencakup identifikasi masalah, kebutuhan pengguna, ruang lingkup, IPO, algoritma, struktur program, struktur data, test case, pembagian tugas, jadwal pelaksanaan, dan repository GitHub. Rancangan tersebut menjadi dasar untuk implementasi dan pengujian pada tahap berikutnya.

## Referensi

Bahan Ajar Algoritma dan Pemrograman, Pertemuan 14: Perancangan Proyek Program Sederhana Masalah Matematika/Pembelajaran Matematika, VS Code, dan GitHub. Program Studi S1 Pendidikan Matematika, FKIP, Universitas Sultan Ageng Tirtayasa, Tahun Akademik 2026/2027 Ganjil.