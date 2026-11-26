# Palindrom adalah kata atau frasa yang terbaca sama baik dari depan maupun dari belakang, 
# dengan mengabaikan spasi, tanda baca, dan huruf besar/kecil.
# Tugas: Buat fungsi is_palindrom(teks) yang mengembalikan True jika kalimat tersebut palindrom, dan False jika bukan. 
# (Hindari penggunaan library eksternal, gunakan logika manipulasi string dasar).

def is_palindrom(teks):
    teks_bersih = ""
    for karakter in teks:
        if karakter.isalnum():
            teks_bersih += karakter.lower()
            
    return teks_bersih == teks_bersih[::-1]

print(is_palindrom("Kasur ini rusak"))       
print(is_palindrom("Ibu Ratna antar ubi!"))  
print(is_palindrom("Pura Group Indonesia"))  
