def admin_menu():
    print("=== MENU ADMIN ===")
    print("1. Menghapus jadwal")
    print("2. Mengganti jadwal")
    print("0. Keluar")

    choice = input("Masukkan pilihan: ")
    if choice == "1":
        hapus_jadwal()
    elif choice == "2":
        ganti_jadwal()
    elif choice == "0":
        logout()
    else:
        print("Pilihan tidak valid.")
        admin_menu()

def hapus_jadwal():
    print("=== HAPUS JADWAL ===")
    jadwal = input("Masukkan jadwal yang akan dihapus: ")
    # kode untuk menghapus jadwal
    

def ganti_jadwal():
    print("=== GANTI JADWAL ===")
    jadwal_lama = input("Masukkan jadwal yang ingin diganti: ")
    jadwal_baru = input("Masukkan jadwal baru: ")
    # kode untuk mengganti jadwal
    