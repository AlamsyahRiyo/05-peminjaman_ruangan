print("Sekertariat Teknik Industri UNS ")
print("Alamat: Jalan Ir Sutami No 36-A Kentingan Surakarta. Kode Pos, 57126. Telp, (0271) 646994. Fax, (0271) 646655,")
print("")
print("Selamat datang di program PINJAMRUANG, Silahkan pilih menu untuk melanjutkan")

from admin_menu import admin_menu
import modul_pengguna

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
            modul_pengguna.register(username, password)
            print("Pendaftaran berhasil!")
            pilihan = input("Silakan pilih: 1. Register, 2. Login: ")
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")

            modul_pengguna.cek_pengguna(username, password)
            main()

        elif user_choice == "y":
            print("=== REGISTER ===")
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")

            modul_pengguna.cek_pengguna(username, password)
            main()
        else:
            print("Pilihan tidak valid!")
    elif choice == "2":
        admin_id = input("Masukkan ID admin: ")
        admin_password = input("Masukkan password admin: ")
        if admin_id == "admin" and admin_password == "riyo":
            admin_menu()
        else:
            print("ID admin atau password salah.")
            main()
    elif choice == "0":
        print("Program berakhir.")
    else:
        print("Pilihan tidak valid.")
        main()

if __name__ == "__main__":
    main()

