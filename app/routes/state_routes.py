from app.data_provider import city_data_provider
from app.data_provider import location_parser as state_parser
from app import app
from flask import request

@app.route('/state/<state>/cities')
def get_cities(state):
	if state_parser.is_state_abbrev(state):
		return city_data_provider.get_cities_by_state_abbrev(state)

	if state_parser.is_valid_state_name(state):
		return city_data_provider.get_cities_by_state_name(state)

	return "Invalid state name %s. State name or State abbreviation must be capitalized." % state,400
