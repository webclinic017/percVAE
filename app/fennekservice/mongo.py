import pymongo
from bson.objectid import ObjectId

def connect_mongoDB():
    print("Let's connect to Mongo DB")
    #
    client = pymongo.MongoClient(
        "mongodb+srv://admin:Welcome2BBS@cluster0.7gtgy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test
    print("hallooo wir haben eine Mongo verbindung!")
    print(client.list_database_names())

    dblist = client.list_database_names()
    if "myDB" in dblist:
        print("The database exists.")
    # load config for this file
    db = client["myDB"]
    #print(db.list_collection_names())
    #col_bookmarks = db["Bookmarks"]
    # mydict = {"user": "Preset",
    #          "model": "Big Room",
    #          "instrument": "Kick",
    #          "vector": "0101002020232324515151",
    #          "v_volume": 67,
    #          "v_distortion": 14,
    #          "v_reverb": 100,
    #          }
    # x = col_bookmarks.insert_one(mydict)

    #print("Starte die Query Experimente")
    # Query to get ONE Entry specific id:
    # {"user": "Preset", "model": "Small Room"}
    #x = col_bookmarks.find_one({"user": "Preset", "model": "Small Room"})
    #print(x)

    # Query to get a list of every bookmark from a specific user
    # Define Which specific fields you want back
    #for x in col_bookmarks.find({"user": "John"}, {"_id": 0, "user": 1, "model": 1}):
    #    print(x)

    # Define Which specific fields you want back
    #for x in col_bookmarks.find({"user": "John"}, {"_id": 0, "user": 1, "model": 1}):
    #    print(x)

    #for x in col_bookmarks.find({"user": "John"}):
    #    print(x)

    return db

def get_mongoDB_presets(db, preset):
    col_bookmarks = db["Bookmarks"]
    x = col_bookmarks.find_one({"user": "Preset", "model": preset})
    return x

def get_mongoDB_bookmarks(uname, db, bookmark_id):
    col_bookmarks = db["Bookmarks"]
    x = col_bookmarks.find_one({"user": uname, "_id": ObjectId(bookmark_id)})
    return x

def get_mongoDB_bookmarkListPerUser(uname, db):
    col_bookmarks = db["Bookmarks"]
    x = list(col_bookmarks.find({"user": uname, "type": "Bookmark"}))
    for i in range(len(x)):
        x[i]["_id"] = str(x[i]["_id"])
    #    print(x[i]["ObjectId"])
    return x

def post_mongoDB_bookmarks(uname, db, isReversed,lowpass_value,highpass_value,distortion_value,reverb_value,volume_value, model, model_instrument, timestamp):
    col_bookmarks = db["Bookmarks"]
    mydict = {"user": uname,
              "type": "Bookmark",
              "model": model,
              "instrument": model_instrument,
              "vector": "0101002020232324515151",
              "timestamp": timestamp,
              "v_volume": volume_value,
              "v_distortion": distortion_value,
              "v_reverb": reverb_value,
              "v_lowpass": lowpass_value,
              "v_highpass": highpass_value,
              "v_isReversed": isReversed
              }
    x = col_bookmarks.insert_one(mydict)
    return x