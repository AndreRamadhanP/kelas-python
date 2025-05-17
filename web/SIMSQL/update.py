import sqlite3

conn = sqlite3.connect('karyawan.db')

statement = """
    UPDATE karyawan
    SET 
        umur = ?,
        kota = ? 
    WHERE nama = ?;
"""

nama = input('nama: ')
umur = input('umur: ')
kota = input('kota: ')
cur = conn.cursor()
rows=cur.execute(statement, (umur,kota,nama))
print(rows.rowcount)
conn.commit()
