# Buatlah program untuk mencetak pola bingkai persegi berukuran N x N menggunakan karakter * untuk bagian pinggir (bingkai), 
# dan spasi " " untuk bagian tengahnya. (Menguji logika nested loop).
# Tugas: Buat fungsi cetak_bingkai(n) yang mencetak pola ke layar. 

def cetak_bingkai(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end="")  
            else:
                print(" ", end="")
        
        print()

cetak_bingkai(4)

    