from pymongo import MongoClient
import certifi

import urllib

MONGO_URI = 'mongodb+srv://darklunaci69:' + urllib.parse.quote('Mudvayne04') +'@clusterdatamic.safidco.mongodb.net/?retryWrites=true&w=majority'

ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile = ca)
        db = client['db_app_product']
    except ConnectionError as e:
        print("Error con la base de datos")
    else:
        print("Estas conectado!")
        return db