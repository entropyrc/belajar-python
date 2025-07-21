import random
from libs import welcome_message

cuypy_position = random.randint(1, 4)

welcome_message("Selamat datang di CUYPY")
nama_user = input("Masukkan nama kamu: ")

while nama_user == "":
    nama_user = input("Isi dulu nama anda: ")

bentuk_goa = "|_|"
goa_kosong =[bentuk_goa] * 4

goa = goa_kosong.copy()
goa[cuypy_position - 1] = "|0_0|"

goa_kosong = '  '.join(goa_kosong)
goa = '  '.join(goa)

while True:
    print(f'''
Halo {nama_user}! Coba perhatikan goa di bawah ini
{goa_kosong}
''')

    pilihan_user = int(input("Menurut kamu, CUYPY ada di goa ke berapa? [1 / 2 / 3 / 4]: "))

    while pilihan_user > 4:
        pilihan_user = int(input("Pilihanmu hanya dibatasi dari 1 sampai 4 saja, silahkan pilih ulang [1 / 2 / 3 / 4]: "))

    confirm_answer = input(f"Apakah kamu yakin jawabannya adalah {pilihan_user}? [y/n]: ")

    if confirm_answer == "n":
        print("Program dihentikan!")
        exit()
    elif confirm_answer == "y":
        if pilihan_user == cuypy_position:
            print(f"\n{goa}\n\nSelamat, kamu menang!")
        else:
            print(f"\n{goa}\n\nMaaf, kamu kalah!")

    else:
        print("Silahkan ulangi programnya!")
        exit()

    play_again = input("\n\nApakah ingin melanjutkan gamenya lagi? [y/n]: ")
    if play_again == "n":
        break

print("Program selesai")