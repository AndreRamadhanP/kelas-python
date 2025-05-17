from flask import Flask, request, send_from_directory
import  sqlite3

app = Flask(__name__)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('images', path)

@app.route('/')
def root():
    return open('./index.html', 'r').read()

@app.route('/tambah.html')
def tambah():
    return open('./tambah.html', 'r').read()

@app.route('/update.html')
def update():
    return open('./update.html', 'r').read()

@app.route('/hapus.html')
def hapus():
    return open('./hapus.html', 'r').read()

@app.route('/cari.html')
def cari():
    return open('./cari.html', 'r').read()

@app.route('/tambahdata')
def tambahdata():
    params=request.args
    con= sqlite3.connect('karyawan.db')
    id = params.get('id', None)
    nama = params.get('nama', None)
    umur = params.get('umur', None)
    kota = params.get('kota', None)

    con= sqlite3.connect('karyawan.db')
    cur= con.cursor()
    statement = """
    INSERT INTO    
        karyawan (
            id ,
            nama ,
            umur ,
            kota 
        ) VALUES(?,?,?,?);
    """

    cur.execute(statement, (id,nama,umur,kota))
    con.commit()
    return open('tambah.html', 'r').read()

app.run(debug=True)