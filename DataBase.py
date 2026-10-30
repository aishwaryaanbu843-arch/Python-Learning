from pymongo import MongoClient

server = MongoClient("mongodb://localhost:27017/")

db = server["PythonRockers"]
collection1 = db["Students"]

students = [
    {
        "name": "Swetha",
        "rollNo": 103,
        "phno": 9876543211
    },
    {
        "name": "Yuvaraj",
        "rollNo": 104,
        "phno": 9876543212
    },
    {
        "name": "Bala",
        "rollNo": 105,
        "phno": 9876543213
    },
    {
        "name": "Priyadharshini",
        "rollNo": 106,
        "phno": 9876543214
    },
    {
        "name": "Srinivasan",
        "rollNo": 107,
        "phno": 9876543215
    },
    {
        "name": "Akash",
        "rollNo": 108,
        "phno": 9876543216
    },
    {
        "name":"Aishu",
        "rollNo": 109,
        "phno": 9876543217
    } ,
    {
        "name":"Ramanan",
        "rollNo": 110,
        "phno": 9876543218
    },
    {
        "name":"Sathana",
        "rollNo": 111,
        "phNo":987654320
    }
]

output = collection1.insert_many(students)

print("Inserted IDs:", output.inserted_ids)

server.close()
