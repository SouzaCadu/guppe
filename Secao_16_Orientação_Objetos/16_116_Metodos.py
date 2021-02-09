"""
Metodos

Representam os comportamentos do objeto, ou seja, as ações que esse objeto pode realizar no sistema. Devem ser
escritos em letras minúsculas separadas por underline, se composto.

Metodo de instância:
O metodo especial dunder init '__init__' é um metodo especial chamado de construtor e sua função é construir
o objeto a partir da clase. Os metdos dunder em Python são chamados de 'metodos mágicos'. Não devemos
utilizar dunder no início e no fim, pois podemos sobrescrever alguma função mudando o comportamento interno
da linguagem.


from passlib.hash import pbkdf2_sha256 as cryp


class Lampada:
    def __init__(self, voltagem, cor, luminosidade):
        self.__voltagem = voltagem  # self. é o objeto que está executando o método
        self.__cor = cor
        self.__luminosidade = luminosidade
        self.__ligado = False


class ContaCorrente:

    contador = 4999

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        return (self.__valor * (100 - porcentagem)) / 100


p1 = Produto("PlayStation 5", "Video Game", 4700)
p2 = Produto("X-Box S", "Video Game", 4200)

print(p1.desconto(10), p2.desconto(15))


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"

    def checa_senha(self, senha):
        if not cryp.verify(senha, self.__senha):
            return False
        return True


user1 = Usuario("Chales", "Xavier", "charles@xmen.com", "123456")
user2 = Usuario("Tony", "Stark", "stark@ironman.com", "123456")

print(user1.nome_completo(), Usuario.nome_completo(user2))

print(f"Senha User 1:{user1._Usuario__senha}", f"Senha User 1:{user2._Usuario__senha}")

nome = input("Informe o nome: ")
sobrenome = input("Informe o sobrenome: ")
email = input("Informe o e-mail: ")
senha = input("Informe a senha: ")
confirma_senha = input("Confirme a senha: ")

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print("Senha não confere.")
    exit(42)

print("Usuário criado com sucesso.")

senha = input("Informe a senha de acesso: ")

if user.checa_senha(senha):
    print("Acesso permitido")
else:
    print("Acesso negado")

print(f"Senha user criptografa: {user._Usuario__senha}")  # Acesso incorreto


Metodo de classe

Não estão vinculados a instância, e sim a diretamente classe. Utilizamos um decorator para indicar que o metodo
é de classe e não de instância.
O metodo de instância deve ser usado quando precisarem fazer acesso aos atributos de instância, já o método de
classe não acessa a instância apenas a classe.


from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    contador = 0

    @classmethod  # Utilizado para criar o metodo da classe
    def conta_usuarios(cls):  # o parametro de acesso é a própria classe, por convenção
        print(f"Temos {cls.contador} usuários no sistema.")

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"

    def checa_senha(self, senha):
        if not cryp.verify(senha, self.__senha):
            return False
        return True


user1 = Usuario("Chales", "Xavier", "charles@xmen.com", "123456")
user2 = Usuario("Tony", "Stark", "stark@ironman.com", "123456")

print(user1.nome_completo(), Usuario.nome_completo(user2))

# acesso de forma correta
Usuario.conta_usuarios()
# acesso da forma incorreta
user2.conta_usuarios


Metodos privados

São utilizados apenas dentro da classe.

from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    contador = 0

    @classmethod  # Utilizado para criar o metodo da classe
    def conta_usuarios(cls):  # o parametro de acesso é a própria classe, por convenção
        print(f"Temos {cls.contador} usuários no sistema.")

    @staticmethod
    def definicao():
        return "URX768"

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"

    def checa_senha(self, senha):
        if not cryp.verify(senha, self.__senha):
            return False
        return True

    def __gera_usuario(self):
        return self.__email.split("@")[0]


print(Usuario.contador, Usuario.definicao())
print("-"*20)
user1 = Usuario("Chales", "Xavier", "charles@xmen.com", "123456")
user2 = Usuario("Tony", "Stark", "stark@ironman.com", "123456")
print(user1.nome_completo(), Usuario.nome_completo(user2))
print("-"*20)
print(user2.contador, user1.definicao())


"""


