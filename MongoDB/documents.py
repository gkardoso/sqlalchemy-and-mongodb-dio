from database import criar_banco_de_dados, criar_colecao

def inserir_documento(banco, colecao, documento):
  colecao.insert_one(documento)


def recuperar_documentos(banco, colecao, filtro):
  documentos = colecao.find(filtro)
  return documentos


