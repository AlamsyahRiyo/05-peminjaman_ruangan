import csv

from menu import menu

def register(username, password):
    with open('data_pengguna.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

def login(username, password):
    with open('data_pengguna.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Mengabaikan baris header
        for row in reader:
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
