# Test Case: Generator Soal Persamaan Linear Satu Variabel (PLSV)

## 1. Tujuan Pengujian

Pengujian dilakukan untuk memastikan program dapat menghasilkan soal Persamaan Linear Satu Variabel (PLSV), memeriksa jawaban pengguna, dan menghitung nilai akhir dengan benar.

## 2. Daftar Test Case

### TC01 – Jawaban Benar
- **Input:** Soal `2x + 4 = 10`, jawaban pengguna `3`.
- **Hasil yang Diharapkan:** Program menyatakan jawaban benar.

### TC02 – Jawaban Salah
- **Input:** Soal `2x + 4 = 10`, jawaban pengguna `2`.
- **Hasil yang Diharapkan:** Program menyatakan jawaban salah dan menampilkan jawaban yang benar, yaitu `3`.

### TC03 – Jumlah Soal Satu
- **Input:** Jumlah soal `1`.
- **Hasil yang Diharapkan:** Program menghasilkan dan menampilkan satu soal PLSV.

### TC04 – Jumlah Soal Tidak Valid
- **Input:** Jumlah soal `0`.
- **Hasil yang Diharapkan:** Program menolak input dan meminta pengguna memasukkan jumlah soal yang valid.

### TC05 – Jawaban Berupa Teks
- **Input:** Jawaban pengguna `abc`.
- **Hasil yang Diharapkan:** Program menolak jawaban yang bukan angka dan meminta pengguna memasukkan jawaban numerik.

### TC06 – Semua Jawaban Benar
- **Input:** Pengguna menjawab semua soal dengan benar.
- **Hasil yang Diharapkan:** Program menampilkan nilai akhir `100`.

## 3. Kesimpulan

Program dinyatakan memenuhi pengujian apabila setiap skenario menghasilkan keluaran sesuai dengan hasil yang diharapkan. Pengujian aktual dilakukan setelah implementasi program selesai.