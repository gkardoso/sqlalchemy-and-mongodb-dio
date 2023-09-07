from connection import conectar_ao_mongodb

def criar_banco_de_dados(client):
  db = client["banco"]
  return db


def criar_colecao(db):
  collection = db["clientes"]
  return collection
