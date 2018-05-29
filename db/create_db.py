import sqlite3, pandas

connection = sqlite3.connect('rv_proj.db')
cursor = connection.cursor()

def drop_table(table_name):
	cursor.execute('drop table if exists {0}'.format(table_name))
	connection.commit()

def init_table(table_name, index_label, file_name):
	data = pandas.read_csv('../data/'+file_name)
	data.index = data.index + 1
	data.to_sql(table_name, connection, if_exists='append', index=True, index_label=index_label)

drop_table('city')
drop_table('state')
drop_table('user')
drop_table('visit')

cursor.execute('''
	CREATE TABLE state(StateID integer primary key,
	Name text unique,
	Abbreviation text unique,
	DateAdded text,
	DateTimeAdded text,
	LastUpdated text
	)
	''')

cursor.execute('''
	CREATE TABLE city(CityID integer primary key,
	Name text not null,
	StateID integer not null,
	Status text,
	Latitude real,
	Longitude real,
	DateAdded text,
	DateTimeAdded text,
	LastUpdated text,
	FOREIGN KEY (StateID) REFERENCES state(StateID))
	''')

cursor.execute('''
	CREATE TABLE user(UserID integer primary key,
	FirstName text not null,
	LastName text not null,
	DateAdded text,
	DateTimeAdded text,
	LastUpdated text)
	''')

cursor.execute('''
	CREATE TABLE visit(VisitID integer primary key,
	UserID integer not null,
	CityID integer not null,
	StateID integer not null,
	FOREIGN KEY (UserID) REFERENCES user(UserID),
	FOREIGN KEY (CityID) REFERENCES city(CityID),
	FOREIGN KEY (StateID) REFERENCES state(StateID),
	UNIQUE(UserID,CityID))
	''')

init_table('visit', 'VisitID', 'Visit.csv')
init_table('city', 'CityID', 'City.csv')
init_table('state', 'StateID', 'State.csv')
init_table('user', 'UserID', 'User.csv')

connection.commit()
connection.close()