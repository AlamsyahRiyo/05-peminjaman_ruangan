import os 
os.system("cls")
os.system("clear")


print("Sekertariat Teknik Industri UNS ")
print("Alamat: Jalan Ir Sutami No 36-A Kentingan Surakarta. Kode Pos, 57126. Telp, (0271) 646994. Fax, (0271) 646655,")
print("")
print("Selamat datang di program PINJAMRUANG, Silahkan pilih menu untuk melanjutkan")


import modul_pengguna
import modul_admin

def main():
    print("1. User")
    print("2. Admin")
    print("0. Keluar")
    choice = input("Masukkan pilihan: ")
    if choice == "1":
        user_choice = input("Apakah Anda sudah memiliki akun? (y/n): ")
        if user_choice == "n":
            print("=== REGISTER ===")
            username = input("Masukkan username baru: ")
            password = input("Masukkan password baru: ")
            # modul_pengguna.register(username, password)
            modul_pengguna.simpan_data(username, password)

            print("Pendaftaran berhasil!")
            print("=== LOGIN ===")
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")

            modul_pengguna.cek_pengguna(username, password)
            main()

        elif user_choice == "y":
            print("=== LOGIN ===")
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")

            modul_pengguna.cek_pengguna(username, password)
            main()
        else:
            print("Pilihan tidak valid!")
    elif choice == "2":
            print("=== LOGIN SEBAGAI ADMIN ===")
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")

            modul_admin.cek_admin(username, password)
            main()
            
    elif choice == "0":
        print("Program berakhir.")
    else:
        print("Pilihan tidak valid.")
        main()

if __name__ == "__main__":
    main()

