import pymongo
from arcane_rest_api import DB_PORT, DB_HOST, DB_NAME, GOOD_DOC_NAME, USERS_DOC_NAME


goods = [
{
	"id": 1,
	"name": "Super House, Sartrouville 78500",
	"address": {
		"number": 49,
		"street_name": "Carnot",
		"street_type": "Avenue",
		"city": "Sartrouville",
		"postal_code": 78500,
		"country": "France"
	},
	"proprietary": {
		"first_name": "Virgile",
		"last_name": "Amato"
	},
	"size": 189,
	"rooms": 4,
	"garden": True,
},
{
	"id": 2,
	"name": "Huge flat, Neuilly-Sur-Seine",
	"address": {
		"number": 17,
		"street_name": "Sablonville",
		"street_type": "Rue",
		"city": "Neuilly-Sur-Seine",
		"postal_code": 92200,
		"country": "France"
	},
	"proprietary": {
		"first_name": "Virgile",
		"last_name": "Amato"
	},
	"size": 136,
	"rooms": 4,
	"garden": False
}
]

users = [
	{
		"id": 1,
		"uname" : "vamato",
		"first_name": "Virgile",
		"last_name": "Amato",
		"birthdate": "24/10/1993",
		"secret_key": "jnU47uIDi8"
	},
	{
		"id": 2,
		"uname" : "aamato",
		"first_name": "Arthur",
		"last_name": "Amato",
		"birthdate": "24/10/1993",
		"secret_key": "kdjO37bxID"
	},
	{
		"id": 3,
		"uname" : "mdupont",
		"first_name": "Michel",
		"last_name": "Dupont",
		"birthdate": "24/10/1993",
		"secret_key": "lE9jD0JEma"
	},
]


def feed_db(db_name, doc_name, list_data):
	for dict_data in list_data:
		with pymongo.MongoClient(host=DB_HOST, port=DB_PORT) as conn:
			db = conn[db_name]
			req_good = list(db[doc_name].find({"id": dict_data["id"]}))
			if not req_good:
				db[doc_name].insert(dict_data)


feed_db(DB_NAME, GOOD_DOC_NAME, goods)
feed_db(DB_NAME, USERS_DOC_NAME, users)