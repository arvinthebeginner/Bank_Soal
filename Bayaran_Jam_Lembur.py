# Sebuah pabrik mencatat durasi kerja karyawan dalam sehari (dalam jam). Jam kerja normal adalah 8 jam.
# • Jika kerja <= 8 jam, tidak ada lembur.
# • Jika kerja >8 jam, kelebihan jam dihitung sebagai lembur:
# • 2 jam pertama lembur dibayar Rp 20.000 / jam.
# • Jam lembur berikutnya (jam ke-3 lembur dan seterusnya) dibayar Rp 30.000 / jam.
# Tugas: Buat fungsi hitung_total_lembur(daftar_jam) yang menerima list jam kerja karyawan selama seminggu 
# dan mengembalikan total uang lembur yang didapat.

jam_lembur= [8, 9, 11, 8, 10]

def hitung_total_lembur(daftar_jam):
    total_uang=0
    for jam in daftar_jam:
        if jam > 8:
            jam_lembur = jam - 8
            if jam_lembur <= 2:
                total_uang += jam_lembur * 20000
            else:
                sisa_jam_lembur = jam_lembur-2
                total_uang += (jam_lembur * 20000) + (sisa_jam_lembur * 30000)
    return total_uang

print(hitung_total_lembur(jam_lembur))