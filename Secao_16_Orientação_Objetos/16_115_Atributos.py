"""
Atributos

Representam as caracteristicas do objeto. Através deles conseguimos representar computacionalmente os status
de um objeto.

Existem três tipos de atributos:

- Atributos de instância:
São atributos declarados dentro do método construtor, um método especial utilizado na construção do objeto.
Podem ser públicos ou privados no que se refere a visibilidade, quando o atributo for privado ele só pode
ser acessado dentro da classe em que foi criado, do contrário ele pode ser acessado por outras classes,
em qualquer parte do projeto.
Em Python ficou estabelecido que todo o atributo de uma classe é público, ou seja, pode ser acessado em todo
o projeto, caso desejemos que um atributo seja privado devemos utilizar '__' no inicio do seu nome
(Name Mangiling). Isso é apenas uma convenção, o Python não impede que um atributo seja acessado fora
da classe.  Quando são criados atributos de instância de uma classe, todas as instâncias criadas
terão esses atributos.

class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem  # self. é o objeto que está executando o método
        self.cor = cor
        self.ligado = False

class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Acesso:
    def __init__(self, mail, senha):
        self.mail = mail
        self.__senha = senha

    def mostra_senha(self):  # a forma correta é criar um atributo
        print(self.__senha)

    def mostra_email(self):
        print(self.mail)


user = Acesso("user@gmail.com", "123456")
print(user.mail)
print(user._Acesso__senha)  # acesso via Name Mangiling

user.mostra_senha()  # acesso direto e da forma correta
user.mostra_email()  # acesso direto e da forma correta

user1 = Acesso("user1@gmail.com", "123457")
user2 = Acesso("user2@gmail.com", "123458")

user1.mostra_email()
user2.mostra_email()


- Atributos de classe:
São atributos declarados diretamente na classe, ou seja, fora do construtor, geralmente já inicializado com
valor que é compartilhado entre todas as instâncias da classe, ou seja, ao invés de cada instância ter a
instância da classe e seus próprios valores como é o caso dos atributos de instância, com os atributos de classe
todas as instâncias terão mesmo valor para aquele atributo.

class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


p1 = Produto("PlayStation 5", "Video Game", 4700)
p2 = Produto("X-Box S", "Video Game", 4200)

print(p1.valor, p2. valor)

# Refatorando a classe Produto


class Produto:

    imposto = 1.005  # atributos de instância, só aloca um espaço em memória
    contador = 0  # atributo de instância, só aloca um espaço em memória

    def __init__(self, nome, descricao, valor):  # recebe apenas os dados necessários
        self.id = (Produto.contador + 1)  # Atributo de instância
        self.nome = nome
        self.descricao = descricao
        self.valor = f"{valor * Produto.imposto:.2f}"
        Produto.contador = self.id  # Atributo de classe acessado via "nome da classe".atributo"


p1 = Produto("PlayStation 5", "Video Game", 4700)  # Aloca 4 espaços em memória
p2 = Produto("X-Box S", "Video Game", 4200)

print(p1.valor, p2.valor)  # Acesso possível mas incorreto

print(Produto.imposto)  # Acesso correto
print(p1.id, p2.id)


- Atributos dinâmicos:
É um atributo de instância que pode ser criado em tempo de execução. Será exclusivo da instância que o criou.

class Produto:
    imposto = 1.005  # atributos de instância, só aloca um espaço em memória
    contador = 0  # atributo de instância, só aloca um espaço em memória

    def __init__(self, nome, descricao, valor):  # recebe apenas os dados necessários
        self.id = (Produto.contador + 1)  # Atributo de instância
        self.nome = nome
        self.descricao = descricao
        self.valor = f"{valor * Produto.imposto:.2f}"
        Produto.contador = self.id  # Atributo de classe acessado via "nome da classe".atributo"


p1 = Produto("PlayStation 5", "Video Game", 4700)  # Aloca 4 espaços em memória
p2 = Produto("X-Box S", "Video Game", 4200)

print(p1.valor, p2.valor)  # Acesso possível mas incorreto

print(Produto.imposto)  # Acesso correto
print(p1.id, p2.id)

# Editando atributos dinâmicos

p2.peso = "5 kg"  # atributo criado em tempo de execução
print(f"Produto: {p2.valor}, Descricao: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}")
# print(f"Produto: {p1.valor}, Descricao: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}")
# p1 não possui atributo peso

# acessando os atributo da classe, incluindo os dinâmicos
print(p1.__dict__, p2.__dict__)

# apagando um atributo dinamicamente
del p2.peso
print(p1.__dict__, p2.__dict__)

"""
