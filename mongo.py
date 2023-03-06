from pymongo import MongoClient

class Mymongodb():
    def __init__(self, connection_link, db_name):
        self.client = MongoClient(connection_link)
        self.db_name = db_name

    def db(self, collection_name):
        self.dbs = self.client[self.db_name]
        if collection_name not in self.dbs.list_collection_names():
            self.dbs.create_collection(collection_name)
        return self.dbs[collection_name]

    def insert(self, data, collection_name):
        coll = self.db(collection_name)
        if isinstance(data, dict):
            coll.insert_one(data)
            print("Packet inserted")
        elif isinstance(data, list) or isinstance(data, tuple) or isinstance(data, set):
            coll.insert_many(data)
            print(f"{len(data)} packets inserted")
        else:
            raise ValueError("Invalid data type, data must be a dict, list, tuple, or set")

    def update(self, match_key, match_value, update_dict, collection_name):
        coll = self.db(collection_name)
        if isinstance(update_dict, dict):
            if len(update_dict) == 1 and "_id" in update_dict:
                print("Error: _id cannot be updated")
                return
            query = {match_key: match_value}
            matched_packets = list(coll.find(query))
            if len(matched_packets) == 0:
                print("Match not found")
                return
            for packet in matched_packets:
                if "_id" in update_dict:
                    del update_dict["_id"]
                coll.update_one({"_id": packet["_id"]}, {"$set": update_dict})
                print(f"Packet updated: {packet}")
        elif isinstance(update_dict, list):
            for packet in update_dict:
                self.update(match_key, match_value, packet, collection_name)
        else:
            print("Invalid update dictionary")

    def delete(self, match_key, match_value, collection_name):
        coll = self.db(collection_name)
        query = {match_key: match_value}
        result = coll.delete_many(query)
        print(f"{result.deleted_count} packet deleted")