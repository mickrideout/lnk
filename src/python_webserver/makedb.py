import sqlite3
con = sqlite3.connect('age.db') # Warning: This file is created in the current directory
con.execute("CREATE TABLE age (name char(100) NOT NULL, age integer NOT NULL)")
con.execute("INSERT INTO age (name,age) VALUES ('Peter Pan',101)")
con.commit()
