from . import cursor, connection
import json

def get_visited_cities(user_id):
	cursor.execute('''
		SELECT * FROM city
		WHERE CityID IN (
			SELECT DISTINCT CityID FROM visit
			WHERE UserID={0}
		)
		'''.format(user_id))

	items = [dict(zip([key[0] for key in cursor.description], row)) for row in cursor.fetchall()]
	return json.dumps({'cities':items})


def get_visited_states(user_id):
	cursor.execute('''
		SELECT * FROM state
		WHERE StateID IN(
			SELECT DISTINCT StateID from visit
			WHERE UserID='{0}'
		)
		'''.format(user_id))

	items = [dict(zip([key[0] for key in cursor.description], row)) for row in cursor.fetchall()]
	return json.dumps({'states':items})


def remove_visit(user_id, visit_id):
	cursor.execute('''
		DELETE FROM visit
		WHERE UserID='{0}' AND
		VisitID='{1}'
		'''.format(user_id, visit_id))
	connection.commit()


def add_visit(user_id, city_id, state_id):
	cursor.execute('''
		INSERT OR IGNORE INTO visit(UserID, CityID, StateID)
		VALUES('{0}','{1}','{2}')
		'''.format(user_id, city_id, state_id))
	connection.commit()


def add_visit_by_state_name(user_id, city_name, state_name):
	cursor.execute('''
		INSERT OR IGNORE INTO visit(UserID, CityID, StateID)
		VALUES((SELECT UserID FROM user where UserID='{0}'),
		(SELECT CityID FROM city where Name='{1}' and StateID=(select StateID from state where Name='{2}')),
		(SELECT StateID from state where Name='{2}')
		)
		'''.format(user_id, city_name, state_name))
	connection.commit();
	

def add_visit_by_state_abbrev(user_id, city_name, state_abbrev):
	cursor.execute('''
		INSERT OR IGNORE INTO visit(UserID, CityID, StateID)
		VALUES((SELECT UserID FROM user where UserID='{0}'),
		(SELECT CityID FROM city where Name='{1}' and StateID=(select StateID from state where Abbreviation='{2}')),
		(SELECT StateID FROM state where Abbreviation='{2}')
		)
		'''.format(user_id, city_name, state_abbrev))
	connection.commit();