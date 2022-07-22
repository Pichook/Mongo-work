import pymongo


client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

#DB, Collection, insert
mydb = client['Pye']

work = mydb.pyework

record1 = [{
            'firstname':'Lily',
            'lastname': 'Brace',
            'school': 'KIT'

}, 
{
        'id': 66,
        'firstname': 'Bobby'
}, 
{
            'firstname': 'Lucy',
            'lastname': 'Heartfell',
            'school': 'KIT'

},
{
    'firstname': 'Walter',
    'lastname': 'Straight',
    'school': 'KIT'
}]

work.insert_many(record1)

record3 = {
            'firstname':'Lily',
            'lastname': 'Lance',
            'school': 'KIT'
}

work.insert_one(record3)
