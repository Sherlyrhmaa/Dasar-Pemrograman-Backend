# Program Python Menghitung Gaji Karyawan

# Mendefinisikan upah per jam berdasarkan golongan
def hitung_upah(golongan, jam_kerja):
    if golongan == "A":
        upah_per_jam = 5000
    elif golongan == "B":
        upah_per_jam = 7000
    elif golongan == "C":
        upah_per_jam = 8000
    elif golongan == "D":
        upah_per_jam = 10000
    else:
        return "Golongan tidak valid."

    # Menghitung upah lembur
    if jam_kerja > 48:
        jam_lembur = jam_kerja - 48
        upah_lembur = jam_lembur * 4000
    else:
        upah_lembur = 0

    # Menghitung upah total
    upah_total = (jam_kerja * upah_per_jam) + upah_lembur
    return upah_total

# Input data karyawan
nama = input("Masukkan nama karyawan: ")
golongan = input("Masukkan golongan karyawan (A/B/C/D): ")
jam_kerja = int(input("Masukkan jumlah jam kerja: "))

# Menghitung gaji
gaji = hitung_upah(golongan.upper(), jam_kerja)

# Output hasil
print("\n## Program Python Menghitung Gaji Karyawan ##")
print("=============================================")
print(f"Nama Karyawan: {nama}")
print(f"Golongan: {golongan.upper()}")
print(f"Jumlah jam kerja: {jam_kerja}")
print(f"{nama} menerima upah Rp. {gaji} per minggu")