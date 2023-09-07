from models import Cliente, Conta
from data_access import inserir_cliente, recuperar_cliente, recuperar_todas_contas

cliente1 = Cliente(nome="Fulano de Tal", email="fulano@example.com")
cliente2 = Cliente(nome="Beltrano de Tal", email="beltrano@example.com")

inserir_cliente(cliente1)
inserir_cliente(cliente2)

cliente = recuperar_cliente(1)
contas = recuperar_todas_contas(cliente)

print(cliente)
print(contas)