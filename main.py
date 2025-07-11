import random

tebak_nomor = int(input("Tebak angka yang benar dari 1-9: "))

nomor_benar = random.randint(1, 9)  # Menghasilkan angka acak antara 1 dan 9

if tebak_nomor == nomor_benar:
    print(f"Benar, nomornya adalah {nomor_benar}")
else:
    print("Salah, coba tebak lagi")
    
# Tambahkan logika untuk mengulangi tebakan jika salah
while tebak_nomor != nomor_benar:
    tebak_nomor = int(input("Tebak angka yang benar dari 1-9: "))
    if tebak_nomor == nomor_benar:
        print(f"Benar, nomornya adalah {nomor_benar}")
    else:
        print("Salah, coba tebak lagi")