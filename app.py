
#!/usr/bin/env python
# coding: utf-8

from flask import Flask
import psycopg2

app=Flask(__name__)



@app.route("/")
def index():
    conn = psycopg2.connect(host='db',
                        user='postgres',
                        password='postgres',
                        )
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS books;')
    cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
                                    'title varchar (150) NOT NULL,'
                                    'author varchar (50) NOT NULL,'
                                    'pages_num integer NOT NULL,'
                                    'review text,'
                                    'date_added date DEFAULT CURRENT_TIMESTAMP);')

    # Insert data into the table
    cur.execute('INSERT INTO books (title, author, pages_num, review)'
                'VALUES (%s, %s, %s, %s)',
                ('A Tale of Two Cities',
                'Charles Dickens',
                489,
                'A great classic!'))
    cur.execute('INSERT INTO books (title, author, pages_num, review)'
                'VALUES (%s, %s, %s, %s)',
                ('Anna Karenina',
                'Leo Tolstoy',
                864,
                'Another great classic!'))
    conn.commit()
    cur.execute('SELECT * FROM books;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return (books)



if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')