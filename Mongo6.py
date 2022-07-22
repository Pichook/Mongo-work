import pymongo


client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb = client['Pye']

work = mydb.pyework

x = work.find()

# print(x[0])

for i in x: 
    print(i)