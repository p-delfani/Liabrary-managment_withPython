import sqlite3

def connect():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY ,title text , author text , year INTEGER ,isbn INTEGER )")
    conn.commit()
    conn.close()


def insert(title,author,year,isbn):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL , ? , ? ,?,?)" ,(title,author,year,isbn))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(title="",author="",year="",isbn=""):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id) -> object:
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id =? ",(id,))
    conn.commit()
    conn.close()


def update(id,title,author,year,isbn):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET  title = ? , author = ? , year = ? , isbn=? WHERE id =?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()



connect()
# insert("newBook","masoud",1384,1212)
# update(1,"kotlin","sara",2015,1818)
# print(search(year=2021))
# insert("python book","parmis delfani",2021,1212)
# insert("c# book","saman delfani",2021,1313)
# insert("java book","sina delfani",2020,1414)
# insert("c++ book","peyman delfani",2018,1515)
print(view())
# print(search(title = "c# book"))
# update(2,"c#","json",2021,3445)

