import csv
import modul_pengguna

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
        print("PROGRAM BERAKHIR")
    else:
        print("Pilihan tidak valid.")
        admin_menu()


def hapus_jadwal():
    print("=== HAPUS JADWAL ===")
    jadwal = input("Masukkan kode pemesanan jadwal yang akan dihapus: ")
    # kode untuk menghapus jadwal
    modul_pengguna.hapus_pesanan(jadwal)
    

def ganti_jadwal():
    print("=== GANTI JADWAL ===")
    jadwal_lama = input("Masukkan kodepesanan jadwal yang ingin diganti: ")
    print("==Masukkan Jadwal Baru==")
    print("Daftar kelas: ")
    list_kelas = ["1303", "1304", "1209", "5401", "5402"]
    print("1. ", list_kelas[0])
    print("2. ", list_kelas[1])
    print("3. ", list_kelas[2])
    print("4. ", list_kelas[3])
    print("5. ", list_kelas[4])
    kelass=input("Pilih Kelas: ")
    if kelass not in ['1', '2', '3','4', '5']:
        print("Kelas tidak valid, mohon inputkan antara 1-5")
    else:    
        tanggal=input("Tanggal pemesanan (hh/bb/tt): ")
        print("Daftar jam pemakaian: ")
        list_jam = ["07.30 - 09.15", "09.20 - 12.00", "13.00 - 14.45", "14.50 - 16.35"]
        print("1. ", list_jam[0])
        print("2. ", list_jam[1])
        print("3. ", list_jam[2])
        print("4. ", list_jam[3])
        jam=input("Pilih jam (dalam nomor 1-4 sesuai daftar): ")
        if jam not in ['1', '2', '3','4']:
            print("Nomor jam tidak valid, mohon inputkan antara 1-4")
        else:
            modul_pengguna.ubah_pesanan(jadwal_lama, kelass, tanggal, jam)
            print("Jadwal berhasil di booking, silahkan lanjut!")
    # jadwal_baru = input("Masukkan jadwal baru: ")
    # kode untuk mengganti jadwal
    