while (True):
            menu=input("Pilih menu: ")
            if menu == "1":
                    nama=input("Nama: ")
                    NIM =input("Nomor NIM: ")
                    print("Daftar kelas: ")
                    list_kelas = ["1303", "1304", "1209", "5401", "5402"]
                    print("1. ", list_kelas[0])
                    print("2. ", list_kelas[1])
                    print("3. ", list_kelas[2])
                    print("4. ", list_kelas[3])
                    print("5. ", list_kelas[4])
                    kelass=input("Pilih Kelas: ")
                    if kelass=="1":
                        print("Jadwal pemesanan")
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
                            break
                        else:
                            print("Jadwal berhasil di booking, silahkan lanjut!")
                    elif kelass=="2":
                        print("Jadwal pemesanan")
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
                            break
                        else:
                            print("Jadwal berhasil di booking, silahkan lanjut!")
                    elif kelass=="3":
                        print("Jadwal pemesanan")
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
                            break
                        else:
                            print("Jadwal berhasil di booking, silahkan lanjut!")
                    elif kelass=="4":
                        print("Jadwal pemesanan")
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
                            break
                        else:
                            print("Jadwal berhasil di booking, silahkan lanjut!")
                    elif kelass=="5":
                        print("Jadwal pemesanan")
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
                            break
                        else:
                            print("Jadwal berhasil di booking, silahkan lanjut!")
                    else:
                        print("Kelas tidak valid, mohon inputkan kelas 1/2/3/4!")       
                    print("NIM: ", NIM )
                    print("Silahkan menggunakan ruang kelas sesuai kelas yang  anda pesan.")
                    print("Terimakasih atas kepercayaannya, semoga disemogakan..... info kata kata.")
                    o=input("Apakah anda ingin meencetak bukti peminjaman? (y/n): ")
                    if o=='y':