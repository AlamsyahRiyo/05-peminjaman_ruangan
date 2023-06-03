import datetime
                    def print_struk_peminjaman(nama, jam, kelass, NIM):
                        current_time = datetime.datetime.now()
                                
                        print("======= STRUK BUKTI PEMINJAMAN RUANG =======")
                        print(f"Tanggal: {current_time.strftime('%d-%m-%Y')}")
                        print(f"Waktu: {current_time.strftime('%H:%M:%S')}")
                        print(f"Nama Peminjam : {nama}")
                        print(f"NIM : {NIM}")
                        print(f"Jam Pemakaian : {jam}")
                        print(f"Kelas : {kelass}")
                        print("============================================")

                        print_struk_peminjaman(nama, jam, kelass, NIM)
                    o = input("Apakah Anda ingin menghentikan program? (y/n): ")
                    if o == 'y':
                            break
            elif menu=="2":
                print("Panduan reschedule ruang kelas:")
                print("1. Isi formulir reschdule disertai keterangan reschecule ruang kelas")
                print("2. Sertakan bukti pemesanan")
                print("3. Kirimkan kepada nomor customer service yang tersedia")
                print("")
                print("Terimakasih!")
            elif menu=="3":
                print("Mohon hubungi kontak kami apabila ada kendala dan meminta bantuan.")
                listCS = ["(0271)714039", "121 / (021)121", "08.00-17.00"]
                print("Office phone : ", listCS[0])
                print("Contact center : ", listCS[1])
                print("Jam pelayanan : ", listCS[2])
                print("")
                print("Terima kasih")
            else:
                print("Menu tidak valid, pilih menu 1-3!")
                ulang=input("Kembali ke menu (y/n)?")
                if ulang=='y':
                    continue
    else:
        print("Username atau password salah!")

# Main program
def main():
    conn = create_connection()
    create_table(conn)

    while True:
        print("1. Register")
        print("2. Login")
        print("3. Keluar")
        choice = input("Pilih menu: ")

        if choice == '1':
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            register(conn, username, password)
        elif choice == '2':
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            login(conn, username, password)
        elif choice == '3':
            break
        else:
            print("Pilihan tidak valid!")

if name== '__main':
    main()