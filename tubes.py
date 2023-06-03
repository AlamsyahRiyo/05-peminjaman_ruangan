print("Sekertariat Teknik Industri UNS ")
print("Alamat: Jalan Ir Sutami No 36-A Kentingan Surakarta. Kode Pos, 57126. Telp, (0271) 646994. Fax, (0271) 646655,")
print("")
print("Selamat datang di program PINJAMRUANG, Silahkan pilih menu untuk melanjutkan")

import sqlite3

# Fungsi untuk membuat koneksi ke database
def create_connection():
    conn = sqlite3.connect('login.db')
    return conn

# Fungsi untuk membuat tabel login jika belum ada
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS login
                      (username TEXT PRIMARY KEY, password TEXT)''')

# Fungsi untuk membuat akun baru (registrasi)
def register(conn, username, password):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO login (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    print("Registrasi berhasil!")

# Fungsi untuk melakukan login
def login(conn, username, password):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM login WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    if result:
        print("Login berhasil!")
        list_Menu = ["Pemesanan Ruangan", "Panduan Reschedule", "Customer Service"]
        print("1. ", list_Menu[0])
        print("2. ", list_Menu[1])
        print("3. ", list_Menu[2])
        print("=====================================")