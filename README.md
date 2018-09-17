# shoppinglist rest api
# The following endpoints are exposed by this api

VERB   END POINT                             BODY (FORM-DATA)                              HEADERS                            DESCRIPTION
========================================================================================================================================================================================
POST   /get_token/                           username=test, password=testshoppinglist      N/A                                Fetch authorization token
GET    /shoppinglists/                       N/A                                           Authorizatrion: Token <TOKEN>      Get the list of shoppinglists
POST   /shoppinglists/                       name e.g "Road-trip" , budget e.g 5000.00     Authorizatrion: Token <TOKEN>      Create a new shopping list
GET    /shoppinglists/1/                     N/A                                           Authorizatrion: Token <TOKEN>      Get details of a particular shoppinglist
PUT    /shoppinglists/1/                     name e.g "Road-trip" , budget e.g 500.00      Authorizatrion: Token <TOKEN>      Update a particular shoppinglist
GET    /shoppinglists/1/shoppingitems/       N/A                                           Authorizatrion: Token <TOKEN>      Get the list of shopping items of a particular shoppinglist
GET    /shoppinglists/1/shoppingitems/1/     N/A                                           Authorizatrion: Token <TOKEN>      Get a particular shoppinglist item
