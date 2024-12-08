from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    sqliteConnection = sqlite3.connect('database_siswa.db')
    cursor = sqliteConnection.cursor()
    cursor.row_factory = sqlite3.Row
    cursor.execute("SELECT * FROM data_siswa")
    data = cursor.fetchall()
    return render_template("index.html", datas=data)

@app.route("/tambah_data", methods=['POST', 'GET'])
def tambah_data():
    if request.method == 'POST':
        nama = request.form['nama']
        email = request.form['email']
        sqliteConnection = sqlite3.connect('database_siswa.db')
        cursor = sqliteConnection.cursor()
        cursor.execute("INSERT INTO data_siswa (nama, email) VALUES (?, ?)", (nama, email))
        sqliteConnection.commit()
        flash('Data berhasil ditambahkan', 'success')
        return redirect(url_for("index"))
    return render_template("tambah_data.html")

@app.route("/edit_data/<int:id>", methods=['POST', 'GET'])
def edit_data(id):
    sqliteConnection = sqlite3.connect('database_siswa.db')
    cursor = sqliteConnection.cursor()
    if request.method == 'POST':
        nama = request.form['nama']
        email = request.form['email']
        cursor.execute("UPDATE data_siswa SET nama = ?, email = ? WHERE id = ?", (nama, email, id))
        sqliteConnection.commit()
        flash('Data berhasil diupdate', 'success')
        return redirect(url_for("index"))

    cursor.row_factory = sqlite3.Row
    cursor.execute("SELECT * FROM data_siswa WHERE id = ?", (id,))
    data = cursor.fetchone()
    return render_template("edit_data.html", datas=data)

@app.route("/hapus_data/<int:id>", methods=['GET'])
def hapus_data(id):
    sqliteConnection = sqlite3.connect('database_siswa.db')
    cursor = sqliteConnection.cursor()
    cursor.execute("DELETE FROM data_siswa WHERE id = ?", (id,))
    sqliteConnection.commit()
    flash('Data berhasil dihapus', 'warning')
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.secret_key = 'stikom123'
    app.run(debug=True)
