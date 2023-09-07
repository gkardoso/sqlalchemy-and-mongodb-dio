from pymongo import MongoClient

def conectar_ao_mongodb():
  client = MongoClient("mongodb://localhost:27017")
  return client
