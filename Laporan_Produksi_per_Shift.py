input = [("Pagi", 120), ("Siang", 150), ("Pagi", 130), ("Malam", 100), ("Siang", 50)]

def rekap_shift(log_produksi):
    total_shift = {}
    
    for shift, jumlah in log_produksi:
        if shift in total_shift:
            total_shift[shift] += jumlah
        else:
            total_shift[shift] = jumlah
    return total_shift

print(rekap_shift(input))