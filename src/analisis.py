
import random


def buat_soal():
    """Membuat satu soal Persamaan Linear Satu Variabel (PLSV)."""
    a = random.randint(2, 6)
    x = random.randint(1, 10)
    b = random.randint(1, 10)

    c = a * x + b
    soal = f"{a}x + {b} = {c}"

    return {
        "soal": soal,
        "jawaban": x
    }


def periksa_jawaban(jawaban_pengguna, jawaban_benar):
    """Memeriksa apakah jawaban pengguna benar."""
    return jawaban_pengguna == jawaban_benar


def hitung_nilai(jumlah_benar, jumlah_soal):
    """Menghitung nilai akhir dalam skala 0 sampai 100."""
    if jumlah_soal <= 0:
        return 0

    return round((jumlah_benar / jumlah_soal) * 100)
