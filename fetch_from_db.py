import pymongo

def fetch_rss_feed_url_from_mongodb():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    db = client["your_db_name"]
    collection = db["your_collection_name"]
    
    result = collection.find_one({"your_query_criteria"})
    
    if result:
        return result.get("rss_feed_url")
    else:
        return None
