"""
3) Crie uma classe denominada Elevador para armazenar as informações de um elevador dentro de
um prédio. A classe deve armazenar o andar atual (térreo = 0), total de andares no prédio,
excluindo o térreo, capacidade do elevador, e quantas pessoas estão presentes nele.
A classe deve também disponibilizar os seguintes métodos:
    . Inicializa: que deve receber como parâmetros a capacidade do elevador e
      o total de andares no prédio (os elevadores sempre começam no térreo vazio);
    . Entra: para acrescentar uma pessoa no elevador (só deve acrescentar se ainda
      houver espaço);
    . Sai: para remover uma pessoa do elevador (só deve remover se houver alguém
      dentro dele);
    . Sobe: para subir um andar (não deve subir se já estiver no último andar);
    . Desce: para descer um andar (não deve descer se já estiver no térreo);
    . Encapsular métodos os atributos da classe (criar métodos set e get).
"""


class Elevador:

    def __init__(self, capacidade, total_andares):
        """Construtor que recebe a capacidade(int) do elevador e a quantidade
        de andares que contém o prédio(int)"""
        self.__andar = 0
        self.__quantidade_pessoas = 0
        try:
            if int(capacidade) >= 0:
                if int(total_andares) > 0:
                    self.__capacidade = int(capacidade)
                    self.__total_andares = int(total_andares)
                else:
                    raise ValueError
        except ValueError:
            print("\nValores inválidos")
            exit(1)

    def get_andar(self):
        """Retorna o andar em que o elevador está"""
        return self.__andar

    def get_quantidade_pessoas(self):
        """Retorna a quantidade de pessoas que estão do elevador"""
        return self.__quantidade_pessoas

    def get_capacidade(self):
        """Retorna a capacidade do elevador"""
        return self.__capacidade

    def get_total_andares(self):
        """Retorna a quantidade de andares que têm no prédio"""
        return self.__total_andares

    def set_capacidade(self, nova_capacidade):
        """Recebe um valor do tipo int que será o novo valor do atributo
         de instância 'capacidade'"""
        try:
            if int(nova_capacidade) < 0 or int(nova_capacidade) < self.__quantidade_pessoas:
                raise ValueError
            else:
                self.__capacidade = int(nova_capacidade)
        except ValueError:
            print("\nCapacidade inválida")

    def set_total_andares(self, novo_total_andares):
        """Recebe um valor do tipo int que será o novo valor do atributo
        de instância 'total_andares'"""
        try:
            if int(novo_total_andares) >= 0 and novo_total_andares >= self.__andar:
                self.__total_andares = int(novo_total_andares)
            else:
                raise ValueError
        except ValueError:
            print("\nTotal de andares inválido.")

    def entra(self):
        if self.__quantidade_pessoas < self.__capacidade:
            self.__quantidade_pessoas += 1
        else:
            print("\nO elevador está cheio.")

    def sai(self):
        if self.__quantidade_pessoas > 0:
            self.__quantidade_pessoas -= 1
        else:
            print("\nO elevador está vazio.")

    def sobe(self):
        if self.__andar < self.__total_andares:
            self.__andar += 1
        else:
            print(f"\nO elevador está no último andar.")

    def desce(self):
        if self.__andar > 0:
            self.__andar -= 1
        else:
            print(f"\nO elevador está no térreo.")


if __name__ == "__main__":

    elevador1 = Elevador(9, 12)

    print(f"\nO elevador está no {elevador1.get_andar()} andar.")
    print(f"\nA capacidade total do elevador é de: {elevador1.get_capacidade()} pessoas")
    print(f"\n{elevador1.get_quantidade_pessoas()} pessoas estão no elevador")
    print(f"\nO elevador está em um prédio de {elevador1.get_total_andares()} andares")

    [elevador1.entra() for _ in range(5)]
    [elevador1.sai() for _ in range(2)]

    [elevador1.sobe() for _ in range(5)]
    [elevador1.desce() for _ in range(3)]

    print(f"\nO elevador está no {elevador1.get_andar()} andar.")
    print(f"\nA capacidade total do elevador é de: {elevador1.get_capacidade()} pessoas")
    print(f"\n{elevador1.get_quantidade_pessoas()} pessoas estão no elevador")
    print(f"\nO elevador está em um prédio de {elevador1.get_total_andares()} andares")

    elevador1.set_capacidade(9)
    elevador1.set_total_andares(11)

    print(f"\nO elevador está no {elevador1.get_andar()} andar.")
    print(f"\nA capacidade total do elevador é de: {elevador1.get_capacidade()} pessoas")
    print(f"\n{elevador1.get_quantidade_pessoas()} pessoas estão no elevador")
    print(f"\nO elevador está em um prédio de {elevador1.get_total_andares()} andares")
