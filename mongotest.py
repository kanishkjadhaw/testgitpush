import pymongo
client = pymongo.MongoClient("mongodb+srv://kanishk:Changora031994@kanishk03.t3wmk1y.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d = {
    "name":"kanishk",
    "email":"'kaniahkjadhaw@gmail.com",
    "surname": "jadhaw"
}

d = {
    "name":"kanishk",
    "email":"'kaniahkjadhaw@gmail.com",
    "surname": "jadhaw"
}
d = {
    "name":"kanishk",
    "email":"'kaniahkjadhaw@gmail.com",
    "surname": "jadhaw"
}
d = {
    "name":"kanishk",
    "email":"'kaniahkjadhaw@gmail.com",
    "surname": "jadhaw"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
