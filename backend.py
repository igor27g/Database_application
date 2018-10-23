import sqlite3

def connect():
    conn=sqlite3.connect("players.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS players (id INTEGER PRIMARY KEY, player text, club text, age integer, position text)")
    conn.commit()
    conn.close()

def insert(player,club,age,position):
    conn=sqlite3.connect("players.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO players VALUES (NULL,?,?,?,?)",(player,club,age,position))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("players.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM players")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(player="",club="",age="",position=""):
    conn=sqlite3.connect("players.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM players WHERE player=? OR club=? OR age=? OR position=?", (player,club,age,position))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("players.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM players WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,player,club,age,position):
    conn=sqlite3.connect("players.db")
    cur=conn.cursor()
    cur.execute("UPDATE players SET player=?, club=?, age=?, position=? WHERE id=?",(player,club,age,position,id))
    conn.commit()
    conn.close()

connect()
