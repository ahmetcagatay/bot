import discord 
import os
import random
import sqlite3

minWork=25
maxWork=720
minSpring=1
maxSpring=2
minWorkRatio=5

db = sqlite3.connect("pomodata.db")
c = db.cursor()
c.execute("CREATE TABLE IF NOT EXISTS pomodoroveri (userid TEXT NOT NULL, sonzaman INTEGER NOT NULL)")
db.commit()




#verileri database'e yazma
#insert = "INSERT INTO pomodoroveri (userid, sonzaman) VALUES(?,?)"
#c.execute(insert, [(id),(sonz)])
#db.commit()


#aut değişkeni içindeki değeri arama
#read = c.execute("SELECT * FROM user WHERE username='{}'".format(aut))
#for pgn in read.fetchall():
#print(pgn)