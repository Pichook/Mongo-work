import pymongo


client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb = client['Pye']

work = mydb.pyework

# change = work.update_one({'firstname': 'Lucy'}, {"$set": {'firstname': 'Chauncey'}})

changes = work.update_many({'firstname': 'Lily'}, {'$set': {'firstname': 'Lanky'}})