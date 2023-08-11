import contextlib
from fastapi import FastAPI, HTTPException, Query
from pymongo import MongoClient
from bson import ObjectId
from fastapi.encoders import jsonable_encoder
import os
from dotenv import load_dotenv

load_dotenv()
URI = os.getenv('URI')

app = FastAPI()
client = MongoClient(URI)
db = client["courses"]