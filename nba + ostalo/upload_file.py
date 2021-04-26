import pymongo
import gridfs


client = pymongo.MongoClient("mongodb+srv://duhizjame:vornakulasurija1@cluster0.dstyf.mongodb.net/test?retryWrites=true&w=majority",27017)
db = client.bonafides

f = open("телекомуникационе услуге.zip",'rb')
content = f.read()

fs = gridfs.GridFS(db)
fs.put(content)
