
from analisis import buat_soal, periksa_jawaban, hitung_nilai
from data_io import minta_jumlah_soal, minta_jawaban
from utilitas import tampilkan_judul, tampilkan_nilai


def main():
    tampilkan_judul()

    jumlah_soal = minta_jumlah_soal()
    jumlah_benar = 0

    for nomor in range(1, jumlah_soal + 1):
        data_soal = buat_soal()

        print(f"\nSoal nomor {nomor}:")
        print(data_soal["soal"])

        jawaban_pengguna = minta_jawaban(nomor)

        if periksa_jawaban(
            jawaban_pengguna, data_soal["jawaban"]
        ):
            print("Jawaban benar!")
            jumlah_benar += 1
        else:
            print(
                f"Jawaban salah. Jawaban benar: "
                f"{data_soal['jawaban']}"
            )

    nilai = hitung_nilai(jumlah_benar, jumlah_soal)
    tampilkan_nilai(jumlah_benar, jumlah_soal, nilai)


if __name__ == "__main__":
    main()
