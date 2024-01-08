from pymongo import MongoClient
from .configuration_service import configuration_service

client = MongoClient(
   configuration_service['mongodb_uri'],
    uuidRepresentation='standard',
)

db = client['candidate_db']

user_collection = db['users']
candidate_collection = db['candidates']
