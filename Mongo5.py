import pymongo


client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb = client['Pye']

work = mydb.pyework

# cut = work.delete_one({"id": 66})

# cut_spec = work.delete_many({"firstname": 'Lanky'})

cut_all = work.delete_many({})