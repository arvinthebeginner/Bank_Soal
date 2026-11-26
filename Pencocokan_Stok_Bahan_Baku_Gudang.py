# Tim produksi ingin membuat produk yang membutuhkan daftar bahan baku tertentu. 
# Di gudang tersedia stok bahan dalam bentuk dictionary. 
# Buatlah pengecekan apakah semua bahan yang dibutuhkan tersedia di gudang dengan jumlah yang mencukupi.
# Tugas: Buat fungsi cek_stok(kebutuhan, stok_gudang) yang mengembalikan True jika semua bahan cukup,
# dan False jika ada minimal 1 bahan yang kurang atau tidak ada di gudang.

def cek_stok(kebutuhan, stok_gudang):
    for barang, jumlah_butuh in kebutuhan.items():
        if stok_gudang.get(barang, 0) < jumlah_butuh:
            return False
    return True

butuh = {'semen':'20','pasir':'10'}
gudang = {'semen':'30','pasir':'10'}   

print(cek_stok(butuh,gudang))
        