import flask
import pymongo
import json

HOST = "localhsot"
PORT = 9999
DB_HOST "localhost"
DB_PORT = 9200
DB_NAME = "ARCANE_REST_API"

app = flask.Flask(__name__)

goods = [
{
	name: "Super House, Sartrouville 78500",
	address: {
		number: 49,
		street_name: "Carnot",
		street_type: "Avenue",
		city: "Sartrouville",
		postal_code: 78500,
		country: "France"
	}
	proprietary: {
		first_name: "Virgile",
		last_name: "Amato"
	},
	size: 189,
	rooms: 4,
	garden: True,
},
{
	name: "Huge flat, Neuilly-Sur-Seine",
	address: {
		number: 17,
		street_name: "Sablonville",
		street_type: "Rue",
		city: "Neuilly-Sur-Seine",
		postal_code: 92200,
		country: "France"
	}
	proprietary: {
		first_name: "Virgile",
		last_name: "Amato"
	},
	size: 136,
	rooms: 4,
	garden: False,	
}]

@app.route("/goods/edit/", methods=["POST"])
def edit_one_good():
	edit_params = request.json
	edit_params = json.loads(edit_params)
	requested_good_id = edit_params["id"]
	requested_good_name = edit_params["name"]

	requested_good = app.db_client.find({"id": requested_good_id})
	requested_good = app.db_client.find({"name": requested_good_name})

	if not requested_good is None:
		requested_good = json.loads(requested_good)
		for param in edit_params.items():
			requested_good[param[0]] = param[1]

	app.db_client.update(requested_good)

def edit_user_info:






if __name__ = "__main__":
	mongo_client = pymongo.MongoClient(host=DB_HOST, port=DB_PORT)
	app.db_client = mongo_client[DB_NAME]
	app.run(host=HOST, port=PORT, debug=True)


