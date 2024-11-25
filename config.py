from os import getenv as e
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

API_ID = e("API_ID", 11057906)
API_HASH = e("API_HASH", "b7f975dcdf30c826b3e6178ff3f72356")

BOT_TOKEN = e("BOT_TOKEN", None)
