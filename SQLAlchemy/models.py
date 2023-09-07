from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Cliente(Base):
  __tablename__ = "cliente"

  id = Column(Integer, primary_key=True, autoincrement=True)
  nome = Column(String(255), nullable=False)
  email = Column(String(255), nullable=False)


class Conta(Base):
  __tablename__ = "conta"

  id = Column(Integer, primary_key=True, autoincrement=True)
  cliente_id = Column(Integer, ForeignKey("cliente.id"), nullable=False)
  saldo = Column(DECIMAL, nullable=False)
  data_criacao = Column(DateTime, nullable=False)