def bintang_piramid(tinggi):
    for i in range(1, tinggi + 1):
        spasi = " " * (tinggi -i)
        bintang = "* " * i
        print(spasi + bintang)
print(bintang_piramid(5))