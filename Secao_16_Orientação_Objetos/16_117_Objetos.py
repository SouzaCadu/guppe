"""
Objetos

São instâncias da classe, ou seja, após o mapeamento do objeto no mundo real para sua representação
computacional, poderemos criar quantos objetos forem necessários. Podemos pensar nos objetos e
instâncias de uma classe como variáveis do tipo definido na classe.


class Lampada:
    def __init__(self, voltagem, cor, luminosidade):
        self.__ligada = True
        self.__voltagem = voltagem  # self. é o objeto que está executando o método
        self.__cor = cor
        self.__luminosidade = luminosidade
        self.__ligado = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            pass


# Instância dos objetos
lampada1 = Lampada(220, "branca", 75)
print(f"A lampada está ligada? {lampada1.checa_lampada()}.")


class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente {self.__nome} diz oi')


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')


cliente1 = Cliente("Charles Xavier", "123.123.123-12")

cc1 = ContaCorrente(5000, 500, cliente1)

cc1.mostra_cliente()

cc1._ContaCorrente__cliente.diz()


"""

