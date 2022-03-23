import pymongo

client = pymongo.MongoClient("mongodb+srv://delas:delas@cluster0.lbdym.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test