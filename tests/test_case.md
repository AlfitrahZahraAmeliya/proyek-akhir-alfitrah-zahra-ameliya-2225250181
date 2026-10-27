# Test Case: Generator Soal Persamaan Linear Satu Variabel (PLSV)

## 1. Tujuan Pengujian

Pengujian dilakukan untuk memastikan program dapat menghasilkan soal Persamaan Linear Satu Variabel (PLSV), memeriksa jawaban pengguna, memvalidasi input, dan menghitung nilai akhir dengan benar.

## 2. Daftar Test Case

| ID | Kategori | Input/Kondisi | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Normal | Soal \(2x+4=10\), jawaban pengguna 3. | Program menyatakan jawaban benar dan menambah jumlah jawaban benar. |
| TC02 | Jawaban salah | Soal \(2x+4=10\), jawaban pengguna 2. | Program menyatakan jawaban salah dan menampilkan jawaban benar, yaitu 3. |
| TC03 | Jawaban salah | Soal \(2x+4=10\), jawaban pengguna 4. | Program menyatakan jawaban salah dan menampilkan jawaban benar, yaitu 3. |
| TC04 | Batas | Pengguna memasukkan jumlah soal 1. | Program menerima masukan dan menghasilkan satu soal. |
| TC05 | Invalid | Pengguna memasukkan jumlah soal 0. | Program menolak masukan dan meminta jumlah soal yang valid. |
| TC06 | Invalid | Pengguna memasukkan teks `abc` ketika diminta jawaban angka. | Program menampilkan pesan kesalahan dan meminta jawaban numerik yang valid. |
| TC07 | Normal | Semua soal dijawab dengan benar. | Nilai akhir yang ditampilkan adalah 100. |

## 3. Kesimpulan

Program dinyatakan memenuhi pengujian apabila setiap skenario menghasilkan keluaran sesuai dengan hasil yang diharapkan. Pengujian aktual dilakukan setelah implementasi program selesai.

Hasil aktual setiap pengujian akan dicatat dan dibandingkan dengan hasil yang diharapkan untuk mengetahui apakah program berjalan sesuai kebutuhan.