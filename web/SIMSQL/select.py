import sqlite3

namex = input ('nama: ')
conn = sqlite3.connect('karyawan.db')

statement = """
    SELECT 
        id,nama,umur,kota 
    FROM karyawan
    WHERE nama=? ;
"""

cur = conn.cursor()
rows=cur.execute(statement, (namex,))
for r in rows:
    print(r)
conn.commit()
