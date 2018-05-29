import sqlite3,datetime,json

connection = sqlite3.connect('db/rv_proj.db',check_same_thread=False)
cursor = connection.cursor()