from app import app
from flask import request,abort
from app.data_provider import visit_data_provider
from app.data_provider import location_parser as state_parser

@app.route('/user/<user>/visits', methods=['POST'])
def add_visit(user):
	city = request.json.get('city')
	state = request.json.get('state')

	if not city:
		return 'A visit must contain a city name',400

	if not state:
		return 'A visit must contain a state name',400

	if state_parser.is_state_abbrev(state):
		visit_data_provider.add_visit_by_state_abbrev(user,city,state)
		return '',200

	if state_parser.is_valid_state_name(state):
		visit_data_provider.add_visit_by_state_name(user,city,state)
		return '',200

	return 'Invalid state name %s' % state,400


@app.route('/user/<user>/visit/<visit>', methods=['DELETE'])
def remove_visit(user, visit):
	visit_data_provider.remove_visit(user, visit)
	return '',200


@app.route('/user/<user>/visits')
def get_visited_cities(user):
	return visit_data_provider.get_visited_cities(user)


@app.route('/user/<user>/visits/states')
def get_visited_states(user):
	return visit_data_provider.get_visited_states(user)