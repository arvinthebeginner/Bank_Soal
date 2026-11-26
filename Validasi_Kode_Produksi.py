# Sebuah mesin cetak membuat kode produksi yang terdiri dari huruf dan angka. Kode dianggap VALID jika memenuhi semua syarat berikut:
# 1. Panjang karakter tepat 8 digit.
# 2. Diawali dengan huruf kapital 'P' atau 'G'.
# 3. Diakhiri dengan angka genap.
# Tugas: Buat fungsi cek_kode(kode) yang mengembalikan True jika valid, dan False jika tidak.

kode = "P1234563"

def cek_kode(n):
    if len(n)== 8 and n[0] in ["P","G"] and int(n[7])%2==0:
        print("valid")
    else:
        print("tidak valid")

cek_kode(kode)

