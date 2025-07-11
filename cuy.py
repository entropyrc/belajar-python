import random

welcome_message = "Welcome to CUYPY Games!"
cuypy_position = random.randint(1, 4)

print("*****************************")
print(f"** {welcome_message} **")
print("*****************************")

nama_user = input("Masukkan nama kamu: ")

bentuk_goa = "|_|"
goa_kosong =[bentuk_goa] * 4

goa = goa_kosong.copy()
goa[cuypy_position - 1] = "0_0"

goa_kosong = '  '.join(goa_kosong)
goa = '  '.join(goa)

print(f'''
Halo {nama_user}! Coba perhatikan goa di bawah ini
{goa_kosong}
''')

pilihan_user = int(input("Menurut kamu, CUYPY ada di goa ke berapa? [1 / 2 / 3 / 4]: "))

confirm_answer = input(f"Apakah kamu yakin jawabannya adalah {pilihan_user}? [y/n]: ")

if confirm_answer == "n":
    print("Program dihentikan!")
    exit()
elif confirm_answer == "y":
    if pilihan_user == cuypy_position:
        print(f"{goa}\nSelamat, kamu menang!")
    else:
        print(f"{goa}\nMaaf, kamu kalah!")

else:
    print("Silahkan ulangi programnya!")
    exit()

