"""
Propriedades

Em linguagens de programação como o Java, ao declararmos atributos privados nas classes,
costumamos a criar métodos públicos para manipulação desses atributos. Esses métodos
são conhecidos por getters e setters, onde os getters retornam o valor do atributo
e os setters alteram o valor do mesmo.

Os atributos devem ser criados de forma privada, se necessário devem ser criadas propriedades do tipo
getters e setters.

Ainda é possível criar métodos/funções como propriedades

# Trabalhando com getters e setters, analogo ao Java

class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f"Saldo de {self.__saldo} do cliente {self.__titular}"

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    # Recupera o valor do atributo
    def get_numero(self):
        return self.__numero

    # Recupera o valor do atributo
    def get_titular(self):
        return self.__titular

    # Recupera o valor do atributo
    def get_saldo(self):
        return self.__saldo

    # Recupera o valor do atributo
    def get_limite(self):
        return self.__limite

    # Recebe um parametro e modifica o valor do atributo
    def set_titular(self, titular):
        self.__titular = titular

    def set_limite(self, limite):
        self.__limite = limite

conta1 = Conta('Tony', 3000, 5000)
conta2 = Conta('Steve', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.get_saldo() + conta2.get_saldo()
print(f'A soma do saldo das contas é {soma}')

print(conta1.__dict__)
conta1.set_limite(999999)
print(conta1.__dict__)

# Utilizando o método property - Reescrevendo a classe

class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    # @property por definição é do tipo get, retorna o valor do atributo
    @property
    def numero(self):
        return self.__numero

    # @property por definição é do tipo get, retorna o valor do atributo
    @property
    def titular(self):
        return self.__titular

    # @property por definição é do tipo get, retorna o valor do atributo
    @property
    def saldo(self):
        return self.__saldo

    # @property por definição é do tipo get, retorna o valor do atributo
    @property
    def limite(self):
        return self.__limite

    # @property por definição é do tipo get, retorna o valor do atributo
    # podemos usar um método como propriedade
    @property
    def valor_total(self):
        return self.__saldo + self.__limite

    # @variável.setter por definição é do tipo set, alteram o valor do atributo
    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor


conta1 = Conta('Tony', 3000, 5000)
conta2 = Conta('Steve', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.saldo + conta2.saldo
print(f'A soma do saldo das contas é {soma}')

print(conta1.__dict__)
conta1.limite = 76543  # Propriedade limite
print(conta1.__dict__)
print(conta1.limite)

print(conta1.valor_total)  # valor total é uma propriedade, e não uma função, do contrário usariamos parenteses
print(conta2.valor_total)  # valor total é uma propriedade, e não uma função, do contrário usariamos parenteses

"""
