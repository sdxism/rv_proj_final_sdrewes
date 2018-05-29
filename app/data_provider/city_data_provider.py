from . import cursor, connection
import json


def get_cities_by_state_id(state_id):
	cursor.execute('''
		SELECT * FROM city
		WHERE StateID='{0}'
		'''.format(state_id))
	
	items = [dict(zip([key[0] for key in cursor.description], row)) for row in cursor.fetchall()]
	return json.dumps({'cities':items})


def get_cities_by_state_name(state_name):
	cursor.execute('''
		SELECT * FROM city
		WHERE StateID=(
			SELECT StateID FROM state
			WHERE Name='{0}'
		)
		'''.format(state_name))

	items = [dict(zip([key[0] for key in cursor.description], row)) for row in cursor.fetchall()]
	return json.dumps({'cities':items})


def get_cities_by_state_abbrev(state_abbrev):
	cursor.execute('''
		SELECT * FROM city
		WHERE StateID=(
			SELECT StateID FROM state
			WHERE Abbreviation='{0}'
		)
		'''.format(state_abbrev))
	
	items = [dict(zip([key[0] for key in cursor.description], row)) for row in cursor.fetchall()]
	return json.dumps({'cities':items})