# Setiap batch produksi mencetak nomor urut dokumen sekuriti mulai dari 1 hingga N. 
# Karena gangguan sensor, ada satu nomor yang terlewat (hilang) dari urutan. 
# Daftar nomor yang masuk ke sistem juga dalam keadaan acak.
# Tugas: Buat fungsi cari_nomor_hilang(data_nomor, n) untuk menemukan angka berapa yang hilang dari urutan 1 sampai n.

def cari_semua_nomor_hilang(data_nomor, n):
    semua_angka = set(range(1, n + 1))  
    angka_ada = set(data_nomor)          
    
    hilang = sorted(list(semua_angka - angka_ada))
    return hilang

data = [4, 1, 6, 2]
print(cari_semua_nomor_hilang(data, 6))  
