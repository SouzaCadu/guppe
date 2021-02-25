from models.cliente import Cliente
from models.conta import Conta

scott: Cliente = Cliente("Scott Summers", "scott@xmen.com", "123.123.123-00", "01/01/1978")
conta: Conta = Conta(scott)

print(scott)
print(conta)
