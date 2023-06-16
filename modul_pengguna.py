import csv

from menu import menu

def register(username, password):
    with open('data_pengguna.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

def login(username, password):
    with open('data_pengguna.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # print(list(row))
            if row[0] == username and row[1] == password:
                return True
    return False

def cek_pengguna(username, password):
    if login(username, password):
        print("Login berhasil!")
        # Panggil fungsi menu di sini
        menu()
    else:
        print("Login gagal!")

def simpan_data(username, password):
    with open('data_pengguna.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

def simpan_pesanan(nama, NIM, kelass, tanggal, jam):
    kodepesanan = tanggal.replace('/', '') + kelass + jam
    with open('data_pemesanan.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == kodepesanan:
                print("Pesanan pada ruangan dan waktu tidak tersedia, (kode pesanan", kodepesanan, ") sudah ada.")
                print ("Silakan pilih ruang dan jadwal yang lainnya")
                #memanggil fungsi menu kembali
                menu()
                return

    with open('data_pemesanan.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([kodepesanan, nama, NIM, kelass, tanggal, jam])
        print("Kode Pesanan Anda", kodepesanan)

def ubah_pesanan(kodepesanan, kelass, tanggal, jam):
    rows = []
    with open('data_pemesanan.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == kodepesanan:
                nama = row[1]
                NIM = row[2]
                row = [kodepesanan, nama, NIM, kelass, tanggal, jam]
            rows.append(row)
    
    with open('data_pemesanan.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    
    print("Pemesanan jadwal berhasil diubah.")

def hapus_pesanan(kodepesanan):
    rows = []
    with open('data_pemesanan.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != kodepesanan:
                rows.append(row)
    
    with open('data_pemesanan.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    
    print("Pemesanan jadwal berhasil dihapus.")