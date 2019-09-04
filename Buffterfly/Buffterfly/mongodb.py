from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['buffterfly']

topics = db['topics']
settings = db['settings']
