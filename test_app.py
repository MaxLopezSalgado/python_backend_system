from fastapi.testclient import TestClient
from pymongo import MongoClient
from bson import ObjectId
import pytest
from main import app
import os
from dotenv import load_dotenv

load_dotenv()
URI = os.getenv('URI')

client = TestClient(app)
mongo_client = MongoClient(URI)
db = mongo_client['courses']