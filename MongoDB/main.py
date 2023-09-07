from connection import conectar_ao_mongodb
from database import criar_banco_de_dados, criar_colecao
from documents import inserir_documento, recuperar_documentos

client = conectar_ao_mongodb()
db = criar_banco_de_dados(client)
colecao = criar_colecao(db)

documento = {
  "cliente_id": 1,
  "nome": "Fulano de Tal",
  "email": "fulano@example.com",
  "contas": [
    {
      "id": 1,
      "saldo": 1000.00,
      "data_criacao": "2023-07-20T12:00:00"
    },
    {
      "id": 2,
      "saldo": 500.00,
      "data_criacao": "2023-07-20T12:00:00"
    }
  ]
}

inserir_documento(db, colecao, documento)

documentos = recuperar_documentos(db, colecao, {"cliente_id": 1})

for documento in documentos:
  print(documento)
