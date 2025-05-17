import sqlite3

conn = sqlite3.connect('belajar.db')

statment = """
    CREATE TABLE    
        buku (
            id INTEGER PRIMARY KEY NOT NULL,
            judul TEXT NOT NULL,
            tahun INTEGER NOT NULL,
            status_dipinjam TEXT NOT NULL,
            tanggal_diinput TEXT NOT NULL,
            tanggal_diupdate TEXT NOT NULL
        );
"""

cur = conn.cursor()
#cur.execute(statment)
#conn.commit

statement = """
    INSERT INTO    
        buku (
            id ,
            judul ,
            tahun ,
            status_dipinjam ,
            tanggal_diinput ,
            tanggal_diupdate
        ) VALUES(?,?,?,?,?,?);
"""

cur = conn.cursor()
cur.execute(statement, (1, 'Lord Of The Rings', '1940', 'true', '2025-01-25', '2025-01-25'))
cur.execute(statement, (2, 'Harry Poter ', '1941', 'true', '2025-01-25', '2025-01-25'))
cur.execute(statement, (3, 'Cinderella', '1942', 'true', '2025-01-25', '2025-01-25'))
cur.execute(statement, (4, 'Pinokio', '1943', 'true', '2025-01-25', '2025-01-25'))
cur.execute(statement, (5, 'Aladin', '1944', 'true', '2025-01-25', '2025-01-25'))
cur.execute(statement, (6, 'Naruto', '1945', 'true', '2025-01-25', '2025-01-25'))

conn.commit()