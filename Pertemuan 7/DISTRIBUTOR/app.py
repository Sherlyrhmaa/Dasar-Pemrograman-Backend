from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='sherly', 
        database='stok'
    )

@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM barang")
    barang = cursor.fetchall()
    connection.close()
    return render_template('index.html', barang=barang)

@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        kode_barang = request.form['kode_barang']
        nama_barang = request.form['nama_barang']
        harga = request.form['harga']
        jumlah = request.form['jumlah']

        connection = get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO barang (kode_barang, nama_barang, harga, jumlah) VALUES (%s, %s, %s, %s)", 
                (kode_barang, nama_barang, harga, jumlah)
            )
            connection.commit()
            return redirect(url_for('index'))
        except pymysql.Error as err:
            connection.rollback()
            return render_template('tambah.html', error="Error adding product: " + str(err))
        finally:
            connection.close()

    return render_template('tambah.html')

@app.route('/edit/<kode_barang>', methods=['GET', 'POST'])
def edit(kode_barang):
    connection = get_db_connection()
    cursor = connection.cursor()

    if request.method == 'POST':
        kode_barang_baru = request.form['kode_barang']
        nama_barang = request.form['nama_barang']
        harga = request.form['harga']
        jumlah = request.form['jumlah']

        try:
            cursor.execute(
                "UPDATE barang SET kode_barang=%s, nama_barang=%s, harga=%s, jumlah=%s WHERE kode_barang=%s",
                (kode_barang_baru, nama_barang, harga, jumlah, kode_barang)
            )
            connection.commit()
            return redirect(url_for('index'))
        except pymysql.Error as err:
            connection.rollback()
            return render_template('edit.html', barang=(kode_barang, nama_barang, harga, jumlah), error="Error updating product: " + str(err))
        finally:
            connection.close()

    cursor.execute("SELECT * FROM barang WHERE kode_barang=%s", (kode_barang,))
    barang = cursor.fetchone()
    connection.close()

    return render_template('edit.html', barang=barang)

@app.route('/hapus/<kode_barang>', methods=['POST'])
def hapus(kode_barang):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM barang WHERE kode_barang=%s", (kode_barang,))
        connection.commit()
        return redirect(url_for('index'))
    except pymysql.Error as err:
        connection.rollback()
        return f"Error deleting product: {err}"
    finally:
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)
