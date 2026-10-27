
def minta_jumlah_soal():
    """Meminta jumlah soal dan memvalidasi input pengguna."""
    while True:
        try:
            jumlah = int(input("Masukkan jumlah soal (1-10): "))

            if 1 <= jumlah <= 10:
                return jumlah

            print("Jumlah soal harus antara 1 sampai 10.")

        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat.")


def minta_jawaban(nomor_soal):
    """Meminta jawaban numerik dari pengguna."""
    while True:
        try:
            return int(input(f"Jawaban soal nomor {nomor_soal} (nilai x): "))

        except ValueError:
            print("Jawaban tidak valid. Masukkan bilangan bulat.")
