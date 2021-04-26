import pymongo

client = pymongo.MongoClient("mongodb+srv://duhizjame:vornakulasurija1@cluster0.dstyf.mongodb.net/test?retryWrites=true&w=majority",27017)
db = client.bonafides
nabavke = db.nabavke
konkursne = db.konkursne

nabavke.delete_many({})