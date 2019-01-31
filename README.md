# Arcane_Project
REST API for Arcane Interviews

Instruction to run the project:
  1) Start your mongo DB server locally, on usual port 27017
  2) Feed mongo DB documents, with the "feed_db.py" script
  3) Run Flask development server with the "arcane_rest_api.py" script
  4) Test the endpoints with the "test_endpoints.py" script

How the endpoints works :
  - http://localhost:9999/goods/edit :
      POST request with 4 arguments :
        * name : name of the good to edit
        * uname : username of the proprietary of the good
        * secret_key : secret key of the proprietary of the good, in order or deny editing
        * edit : a dictionary containing field to update and their new values
 
 - http://localhost:9999/goods/edit/user/infos/edit :
    POST request with 2 arguments :
        * uname : username of the user which we want to edit informations from
        * edit : a dictionary containing field to update and their new values
 
  - http://localhost:9999/goods/search_by_city : 
    GET request with 1 argument :
        * req_city : the city from which we want to find goods


Améliorations : 
  - Plus de requetes GET
  - Le code n'est pas assez commenté
  - les code de retour HTTP ne sont pas tous bons (ils sont tous égaux à 200), alors qu'il faudrait renvoyer, notamment, un code 400 lorsque les arguments des requêtes sont mauvais.
