tinggi = 5
angka = 1

for i in range(1, tinggi + 1):
    print(" " * (tinggi - i), end="")
    
    for j in range(i):
        print(angka, end=" ")
        angka += 2
        
    print()  