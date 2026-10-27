
def tampilkan_garis():
    """Menampilkan garis pemisah di terminal."""
    print("-" * 40)


def tampilkan_judul():
    """Menampilkan judul program."""
    tampilkan_garis()
    print("GENERATOR SOAL PERSAMAAN LINEAR SATU VARIABEL")
    print("                 (PLSV)")
    tampilkan_garis()


def tampilkan_nilai(jumlah_benar, jumlah_soal, nilai):
    """Menampilkan ringkasan hasil latihan."""
    tampilkan_garis()
    print("HASIL LATIHAN")
    tampilkan_garis()
    print(f"Jumlah soal       : {jumlah_soal}")
    print(f"Jawaban benar     : {jumlah_benar}")
    print(f"Jawaban salah     : {jumlah_soal - jumlah_benar}")
    print(f"Nilai akhir       : {nilai}")
    tampilkan_garis()
