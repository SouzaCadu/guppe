"""
A ideia de herança é a de reaproveitar código. Também extender nossas classes.

OBS: Com a herança, a partir de uma classe existente, nós estendemos outra classe que passa a herdar
atributos e métodos da classe herdada.


Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionario
    - nome;
    - sobrenome;
    - cpf;
    - matricula;

Perguntar: Existe alguma entidade genérica o suficiente para encapsular os atributos e métodos comuns
a outras entidades?

class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente('Charles', 'Xavier', '123.456.789-00', 5000)
funcionario1 = Funcionario('Steve', 'Rogers', '987.654.321-11', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

# Refatorando para aplicar a Herança

# Classe genérica
class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


# Sub classe ou classe filha ou classe específica de Pessoa
class Cliente(Pessoa):

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


# Sub classe ou classe filha ou classe específica de Pessoa
class Funcionario(Pessoa):

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula


cliente1 = Cliente('Charles', 'Xavier', '123.456.789-00', 5000)
funcionario1 = Funcionario('Steve', 'Rogers', '987.654.321-11', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(cliente1.__dict__, funcionario1.__dict__)

- Sobre escrevendo métodos (Overriding)
Quando um método da super classe é reescrito na classe filha, sobre escrevendo o método da super classe.
Nem todas as heranças são possíveis.


# Classe genérica
class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


# Sub classe ou classe filha ou classe específica de Pessoa
class Cliente(Pessoa):

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


# Sub classe ou classe filha ou classe específica de Pessoa
class Funcionario(Pessoa):

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        return f"Funcionário: {self.__matricula}, Nome: {self._Pessoa__nome}."


cliente1 = Cliente('Charles', 'Xavier', '123.456.789-00', 5000)
funcionario1 = Funcionario('Steve', 'Rogers', '987.654.321-11', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(cliente1.__dict__, funcionario1.__dict__)


"""




