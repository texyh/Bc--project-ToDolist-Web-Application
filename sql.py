import sqlite3

with sqlite3.connect("todo.db") as connection:
    c = connection.cursor()
    c.execute("CREATE TABLE user(firstname TEXT,lastname TEXT,email TEXT,password TEXT)")
    c.execute('INSERT INTO user VALUES("onwwuzulike","emeka","onwuzulikee1@gmail.com","andela")')