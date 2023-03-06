#Mymongodb

Mymongodb is a Python class that provides a simple interface for working with MongoDB databases.

#Installation

To use Mymongodb, you need to have the pymongo library installed. You can install it using pip:

#Copy code

pip install pymongo

#Usage

To use Mymongodb, you need to create an instance of the Mymongodb class with a connection link and a database name. You can then use the db() method to get a reference to a specific collection, and the insert(), update(), and delete() methods to manipulate the data in the collection.

Here is an example:

python
Copy code

from pymongo import MongoClient

from mymongodb import Mymongodb

# Set up the connection to the database
connection_link = "mongodb://localhost:27017/"

db_name = "mydatabase"

client = MongoClient(connection_link)

# Create an instance of the Mymongodb class
db = Mymongodb(client, db_name)

# Insert a document into the "mycollection" collection
data = {"name": "John", "age": 35}
db.insert(data, "mycollection")

# Update all documents in the "mycollection" collection where the "name" field is "John"
update_dict = {"age": 36}
db.update("name", "John", update_dict, "mycollection")

# Delete all documents in the "mycollection" collection where the "name" field is "John"
db.delete("name", "John", "mycollection")

