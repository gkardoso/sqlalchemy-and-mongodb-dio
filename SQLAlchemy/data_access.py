from models import Cliente, Conta
from connection import engine


def inserir_cliente(cliente):
  cliente.save(engine)


def recuperar_cliente(id):
  return Cliente.query.filter_by(id=id).first()


def recuperar_todas_contas(cliente):
  return Conta.query.filter_by(cliente_id=cliente.id).all()