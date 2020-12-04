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
    coll_name = str(coll_name)
    try:
        collection = db[coll_name]
        return collection
    except:
        print("Collection doesn't exist")
        return -1

def create_collection(coll_name):
    coll_name = str(coll_name)
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

#currently only works with course collections (with sections, assignments, etc)
def list_collection(coll_name):
    coll_name = str(coll_name)
    client = connect_client()
    if client == -1:
        return -1
    
    db = connect_db(client)

    collection = connect_collection(db, coll_name)

    print("Listing information from ", coll_name , " ...")
    #print all documents in collection
    cursor = collection.find({})
    for document in cursor:
        print("section number: " , document["section"])
        print()
        for student in document["students"]:
            print("student ID and name: " , student["ID"], " / ", student["name"])
            print("submissions: ")
            for submission in student["submissions"]:
                print(submission)
        print()
        print("assignments: ")
        for assignment in document["assignments"]:
            print(assignment)
        print()
        #print(document)

def drop_collection(coll_name):
    coll_name = str(coll_name)
    client = connect_client()
    if client == -1:
        return -1
    
    db = connect_db(client)

    collection = connect_collection(db, coll_name)

    collection.drop()
