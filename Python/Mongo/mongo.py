import pymongo
from mongojoin.mongojoin import  MongoCollection

	
print(MongoJoin)

exit()

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# myclient = pymongo.MongoClient("mongodb+srv://sharvan:sharvan@cluster0.wkm7v.mongodb.net/sharvan?retryWrites=true&w=majority")

# print(myclient)

myDb = myclient['python_mongo']

collection = myDb["users"]





# dataOfuser = {"name": "sharvan", "email": "s@gmail.com", "mobile": "9835401515"}

# # print(dataOfuser)

# x = collection.insert_one(dataOfuser)

# print(x.inserted_id)

# list_database_names()
# list_collection_names()


# print(myclient.list_database_names())

#print("python_mongo" in myclient.list_database_names())

# print(myDb.list_collection_names())

# dataOfuser = [
# 	{"name": "sharvan", "email": "s@gmail.com", "mobile": "9835401515"},
# 	{"name": "sharvan", "email": "s@gmail.com", "mobile": "9835401515"},
# 	{"name": "sharvan", "email": "s@gmail.com", "mobile": "9835401515"},
# 	{"name": "sharvan", "email": "s@gmail.com", "mobile": "9835401515"}
# ]

# x = collection.insert_many(dataOfuser)

# print(x.inserted_ids)

# dataOfuser = [
# 	{"_id": 1, "name": "sharvan", "email": "s@gmail.com", "mobile": "9835401515"},
# 	{"_id": 2, "name": "sharvan", "email": "s@gmail.com", "mobile": "9835401515"},
# 	{"_id": 3, "name": "sharvan", "email": "s@gmail.com", "mobile": "9835401515"},
# 	{"_id": 4, "name": "sharvan", "email": "s@gmail.com", "mobile": "9835401515"}
# ]

# x = collection.insert_many(dataOfuser)

# print(x.inserted_ids)

# x = collection.find_one()

# print(x)

# allData = collection.find()

# for x in allData:
# 	print(x)

# for x in collection.find({},{ "_id": 0, "name": 1, "email": 1, "mobile": 1 }):
#   print(x)

# myquery = { "mobile": "8160410477" }

# for x in collection.find(myquery):
# 	print(x)

# myquery = { "address": { "$gt": "S" } }

# myquery = { "name": { "$gt": "A" } }

# for x in collection.find(myquery):
# 	print(x)

# myquery = { "name": { "$regex": "^A" } }

# for x in collection.find(myquery):
# 	print(x)

# mydoc = collection.find().sort("name", -1)

# for x in mydoc:
# 	print(x)

# myquery = { "_id": 1 }

# x = collection.delete_one(myquery)

# print(x.deleted_count)

# myquery = { "name" : "sharvan"}

# x = collection.delete_many(myquery)

# print(x.deleted_count)


# x = collection.delete_many({})

# print(x.deleted_count)


# collection.drop()


# myquery = { "email": "s@gmail.com" }
# newvalues = { "$set": { "email": "kumar@tops-int.com" } }


# # #collection.update_one(myquery, newvalues)


# x = collection.update_many(myquery, newvalues)

# print(x.modified_count, "documents updated.")

# x = collection.find().limit(2)

# for y in x:
# 	print(y)


