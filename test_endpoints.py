import requests
import json

API_ENDPOINT = "http://localhost:9999/"

def test_edit_one_good():
	edit_one_good_endpoint = "goods/edit"
	good_name = "Super House, Sartrouville 78500"
	edit_params = {
		"name": "Super House, Sartrouville 78500",
		"edit" : {
			"proprietary": {
				"first_name": "Arthur"
			}
		}
	}

	req = requests.post(API_ENDPOINT + edit_one_good_endpoint,
						headers={"Content-Type": "application/json"},
						data=json.dumps(edit_params))

	print(req.json)

test_edit_one_good()
