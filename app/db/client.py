from pymongo import MongoClient
from config.config import settings

# Cliente de MongoDB
client = MongoClient(settings.mongodb_url)

# Base de datos
db = client[settings.database_name]