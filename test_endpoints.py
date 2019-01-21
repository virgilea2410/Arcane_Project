import requests
import json


API_ENDPOINT = "http://localhost:9999/"


def test_edit_one_good():
	edit_one_good_endpoint = "goods/edit"
	edit_params = {
		"name": "Super House, Sartrouville 78500",
		"uname": "vamato",
		"secret_key": "jnU47uIDi8",
		"edit" : {
			"proprietary.first_name": "Arthur"
		}
	}

	req = requests.post(API_ENDPOINT + edit_one_good_endpoint,
						headers={"Content-Type": "application/json"},
						data=json.dumps(edit_params))

	print(req.json())


def test_edit_one_user():
	edit_one_user_endpoint = "user/infos/edit"
	edit_params = {
		"uname": "vamato",
		"edit" : {
			"first_name": "Louis"
		}
	}

	req = requests.post(API_ENDPOINT + edit_one_user_endpoint,
						headers={"Content-Type": "application/json"},
						data=json.dumps(edit_params))

	print(req.json())


def test_search_by_city():
	search_by_city_endpoint = "goods/search_by_city"
	req_city = "Neuilly-Sur-Seine"

	req = requests.get(API_ENDPOINT + search_by_city_endpoint + "/" + req_city)

	print(req.json())


test_edit_one_good()
test_edit_one_user()
test_search_by_city()
