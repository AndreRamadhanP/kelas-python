from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def text ():
    return "kembalikan ke sebuah text berhasil"

@app.route('/index.html')
def serve_index():
    f = open('index.html', 'rb')
    return f.read()

@app.route('/tabel.html')
def serve_tabel():
    f = open('tabel.html', 'rb')
    return f.read()

@app.route('/entry.html')
def entry_tabel():
    f = open('entry.html', 'rb')
    return f.read()

@app.route('/cat.jpg')
def serve_cat():
    f = open('cat.jpg', 'rb')
    return f.read()

@app.route('/process')
def serve_process():
    request_masuk = request.args
    return request_masuk

@app.route('/tuliscsv', methods = ['GET','POST'])
def tuliscsv():
    req_params = dict(request.args)

    csv_file = open('berkas.csv','a')
    #csv_file.write("nama,umur\n")
    csv_file.write(f'{req_params["formname"]},{req_params["formumur"]}\n')
    csv_file.close()

    f = open('entry.html', 'rb')
    return f.read()
    #return "berhasil ditulis"
    

app.run(debug=True)