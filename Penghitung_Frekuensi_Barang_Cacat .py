# Anda diberikan sebuah daftar (list) berisi kode jenis kecacatan produk dari hasil inspeksi harian. 
# Buatlah program untuk menghitung berapa kali masing-masing kode muncul, lalu tampilkan kode mana yang paling sering muncul.
# Tugas: Buat fungsi analisis_cacat(data_cacat) yang mengembalikan dictionary frekuensi dan kode terbanyak.

from collections import Counter

def analisis_cacat(data_cacat):
    if not data_cacat:
        return {}, None
        
    hitung = Counter(data_cacat)
    frekuensi = dict(hitung)
    terbanyak = hitung.most_common(1)
    
    return frekuensi, terbanyak

data = ["C01", "C02", "C01", "C03", "C01", "C02"]
freq, maks = analisis_cacat(data)
print("Frekuensi:", freq)
print("Terbanyak:", maks)
