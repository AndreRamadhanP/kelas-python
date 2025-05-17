import sqlite3

conn = sqlite3.connect('karyawan.db')

statement = """
    DELETE FROM karyawan
    WHERE nama = ?;
"""

nama = 'dwi'
cur = conn.cursor()
rows=cur.execute(statement, (nama,))
print(rows.rowcount)
conn.commit()
