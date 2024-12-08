# Import modul
import sqlite3  # Perbaikan pada nama modul

try:
    # Membuat koneksi ke database
    sqliteConnection = sqlite3.connect('database_siswa.db')
    cursor = sqliteConnection.cursor()
    print("Database Berhasil Terkoneksi")

    # Membuat tabel pada database
    sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS data_siswa (
                                id INTEGER PRIMARY KEY,
                                nama TEXT NOT NULL,
                                email TEXT NOT NULL UNIQUE)'''
    
    # Eksekusi perintah SQL
    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()
    print('Tabel berhasil dibuat atau sudah ada')

    # Mengecek versi SQLite
    sqlite_select_Query = "SELECT sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database version is:", record)

    # Menutup cursor
    cursor.close()

except sqlite3.Error as error:
    print("Error: Gagal terkoneksi ke database", error)

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("Koneksi Database Selesai")