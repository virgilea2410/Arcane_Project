import flask
from flask_cors import CORS
import pymongo
import json


HOST = "localhost"
PORT = 9999
DB_HOST = "localhost"
DB_PORT = 27017
DB_NAME = "ARCANE_DB"
GOOD_DOC_NAME = "MainGoods"
USERS_DOC_NAME = "Users"

app = flask.Flask(__name__)
cors = CORS(app)


@app.route("/goods/edit", methods=["POST"])
def edit_one_good():
	edit_params = flask.request.json

	if all(arg in edit_params.keys() for arg in ["name", "uname", "secret_key"]):
		requested_good_name = edit_params["name"]
		requested_good_key = edit_params["secret_key"]
		requested_good_uname = edit_params["uname"]
		edit_params = edit_params["edit"]
	else:
		resp = flask.Response(json.dumps({"error": "missing_arguments"}), status=200, mimetype="application/json")

		return resp 

	requested_good = list(app.db_client[GOOD_DOC_NAME].find({"name": requested_good_name}))
	requested_user = list(app.db_client[USERS_DOC_NAME].find({"uname": requested_good_uname}))

	if requested_good:
		if requested_user:
			if requested_user[0]["secret_key"] == requested_good_key:
				req = app.db_client[GOOD_DOC_NAME].update({"name": requested_good_name},
															{"$set": edit_params},
															upsert= False)
				resp = flask.Response(json.dumps(req), status=200, mimetype="application/json")
			else:
				resp = flask.Response(json.dumps({"error": "wrong_secret_key"}), status=200, mimetype="application/json")
		else:
			resp = flask.Response(json.dumps({"error": "user_not_found"}), status=200, mimetype="application/json")	
	else:
		resp = flask.Response(json.dumps({"error": "good_not_found"}), status=200, mimetype="application/json")
	
	return resp


@app.route("/user/infos/edit", methods=["POST"])
def edit_user_info():
	edit_params = flask.request.json
	uname = edit_params["uname"]
	edit_params = edit_params["edit"]

	requested_user = list(app.db_client[USERS_DOC_NAME].find({"uname": uname}))

	if requested_user:
		req = app.db_client[USERS_DOC_NAME].update({"uname": uname},
													{"$set": edit_params},
													upsert= False)
		resp = flask.Response(json.dumps(req), status=200, mimetype="application/json")
	else:
		resp = flask.Response(json.dumps({"error": "user_not_found"}), status=200, mimetype="application/json")
	
	return resp


@app.route("/goods/search_by_city/<req_city>", methods=["GET"])
def get_goods_by_city(req_city):
	req = list(app.db_client[GOOD_DOC_NAME].find({"address.city": req_city}, {"_id": 0}))

	if req:
		resp = flask.Response(json.dumps(req[0]), status=200, mimetype="application/json")
	else:
		resp = flask.Response(json.dumps({"error": "no_goods_matching_city"}), status=200, mimetype="application/json")

	return resp 


if __name__ == "__main__":
	mongo_client = pymongo.MongoClient(host=DB_HOST, port=DB_PORT)
	app.db_client = mongo_client[DB_NAME]
	app.run(host=HOST, port=PORT, debug=True)


