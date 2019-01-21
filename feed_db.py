import pymongo
from arcane_rest_api import DB_PORT, DB_HOST, DB_NAME, GOOD_DOC_NAME

goods = [
{
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

def feed_db(db_name, doc_name, list_data):
	for dict_data in list_data:
		with pymongo.MongoClient(host=DB_HOST, port=DB_PORT) as conn:
			db = conn[db_name]
			req_good = list(db[doc_name].find({"name": dict_data["name"]}))
			if not req_good:
				db[doc_name].insert(dict_data)

feed_db(DB_NAME, GOOD_DOC_NAME, goods)