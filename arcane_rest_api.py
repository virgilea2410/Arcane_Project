import flask
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

@app.route("/goods/edit", methods=["POST"])
def edit_one_good():
	edit_params = flask.request.json
	#edit_params = json.loads(edit_params)
	requested_good_name = edit_params["name"]
	edit_params = edit_params["edit"]

	requested_good = list(app.db_client[GOOD_DOC_NAME].find({"name": requested_good_name}))

	if requested_good:
		req = app.db_client[GOOD_DOC_NAME].update({"name": requested_good_name},
													{"$set": edit_params},
													upsert= False)

	resp = flask.Response(json.dumps(req), status=200, mimetype="application/json")

	return resp

@app.route("/user/infos/edit", methods=["POST"])
def edit_user_info():
	edit_params = flask.request.json
	edit_params = json.loads(edit_params)	
	uname = edit_params["username"]

	requested_user = app.db_client.find({"username": uname})

	if requested_user:
		req = app.db_client[USERS_DOC_NAME].update({"username": uname},
													edit_params)

	
	return json.dumps(req)

if __name__ == "__main__":
	mongo_client = pymongo.MongoClient(host=DB_HOST, port=DB_PORT)
	app.db_client = mongo_client[DB_NAME]
	app.run(host=HOST, port=PORT, debug=True)


