import pymongo

def connect_client():
    try:
        client = pymongo.MongoClient('localhost')
        return client
    except:
        print("Client Connection failed")
        return -1

def connect_db(client):
    db = client.student_submissions
    return db

def connect_collection(db, coll_name):
    try:
        collection = db[coll_name]
        return collection
    except:
        print("Collection doesn't exist")
        return -1

def create_collection(coll_name):
    client = connect_client()
    if client == -1:
        return -1
    
    db = connect_db(client)
    try:
        collection = client.db.create_collection(coll_name)
        return 0
    except:
        print("Collection create failed: already exists")
        return -1

def list_collection(coll_name):
    client = connect_client()
    if client == -1:
        return -1
    
    db = connect_db(client)

    collection = connect_collection(db, coll_name)

    #print all documents in collection
    cursor = collection.find({})
    for document in cursor:
        print(document)

def drop_collection(coll_name):
    client = connect_client()
    if client == -1:
        return -1
    
    db = connect_db(client)

    collection = connect_collection(db, coll_name)

    collection.drop()
