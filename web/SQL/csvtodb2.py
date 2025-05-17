import sqlite3

conn = sqlite3.connect('karyawan.db')

statment = """
    CREATE TABLE    
        karyawan (
            id INTEGER PRIMARY KEY NOT NULL,
            nama TEXT NOT NULL,
            umur INTEGER NOT NULL,
            kota TEXT NOT NULL
        );
"""

cur = conn.cursor()
#cur.execute(statment)
#conn.commit

statement = """
    INSERT INTO    
        karyawan (
            id,
            nama,
            umur,
            kota
            
        ) VALUES(?,?,?,?);
"""

cur = conn.cursor()
cur.execute(statement, (1, 'andre', '19', 'bandung'))
cur.execute(statement, (2, 'dwi', '41', 'jakarta'))
cur.execute(statement, (3, 'misnan', '42', 'surabaya'))
cur.execute(statement, (4, 'deden', '43', 'banten'))
cur.execute(statement, (5, 'ani', '34', 'jogja'))
cur.execute(statement, (6, 'dede', '35', 'garut'))

conn.commit()