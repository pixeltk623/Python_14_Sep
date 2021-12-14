from pymongo import *
import pymongo


# server conn
client = MongoClient("mongodb+srv://root:1234@cluster0.j5ona.mongodb.net/root?retryWrites=true&w=majority")
print(client)
nameAdd = {
    "name" : "Shashwat Gupta"
}
mydb = client["pythondb"]
mycol = mydb["table1"]

x = mycol.insert_one(nameAdd)
print(x)

# # database conn

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["pythondb"]

# print("pythondb" in  myclient.list_database_names())

# mycol = mydb["table1"]

# print("table1" in mydb.list_collection_names())

# mycol.insert_one(nameAdd)