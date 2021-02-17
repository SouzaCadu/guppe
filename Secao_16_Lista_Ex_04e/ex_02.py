"""
2) Crie um classe Agenda que pode armazenar 10 pessoas e seja capas de realizar as seguintes operações:
    . void armazenaPessoa(String nome, int idade, float altura);
    . void removePessoa(String nome);
    . int buscaPessoa(String nome);  // informa em que posição da agenda está a pessoa
    . void imprimeAgenda();  // imprime os dados de todas as pessoas da agenda
    . void imprimePessoa(int index);  // imprime os dados da pessoa que está na posição "i" da agenda
"""

from ex_01 import Pessoa


class Agenda:
    registros = []

    @staticmethod
    def registro(nome, idade, altura):
        if len(Agenda.registros) < 10:
            Agenda.registros.append(Pessoa(nome, idade, altura))
        else:
            print("O limite máximo da agenda é de 10 registros.\n"
                  "Não é possivel adicionar mais pessoas.")

    @staticmethod
    def remove_registro(nome):
        removido = False
        for pessoa in Agenda.registros:
            if nome.strip().title() == pessoa.get_nome():
                Agenda.registros.remove(pessoa)
                print(f"{nome} removido com sucesso")
                removido = True
            if not removido:
                print(f"{nome} não localizado.")

    @staticmethod
    def busca_pessoa(nome):
        indice = False
        for posicao in range(len(Agenda.registros)):
            if nome.strip().title() == Agenda.registros[posicao].get_nome():
                print(f"\nO contato {nome} está no índice: {posicao}.")
                indice = True
        if not indice:
            print(f"\n Nome não encontrado.")

    @staticmethod
    def imprime_agenda():
        [print(f"\nNome: {registro.get_nome()}, idade: {registro.get_idade()}, altura: {registro.get_altura()}")
         for registro in Agenda.registros]

    @staticmethod
    def imprime_pessoa(index):
        index = int(index)
        nome = Agenda.registros[index].get_nome()
        idade = Agenda.registros[index].get_idade()
        altura = Agenda.registros[index].get_altura()
        print(f"\nNome: {nome}, idade: {idade}, altura: {altura}.")


if __name__ == '__main__':
    agenda = Agenda()

agenda.registro("Wade Wilson", 25, 1.82)
agenda.registro("Scott Summers", 22, 1.90)
agenda.registro("Edward Brok", 28, 2.01)
agenda.registro("William Wallace", 29, 1.80)
agenda.registro("Ororo Monroe", 20, 1.73)
agenda.registro("Carol Denver", 21, 1.70)
agenda.registro("Anna Marie", 19, 1.80)
agenda.registro("Jean Grey", 20, 1.81)
agenda.registro("Elisabeth Braddock", 22, 1.75)
agenda.remove_registro("Wade Wilson")
agenda.imprime_agenda()
agenda.busca_pessoa("Carol Denver")
agenda.imprime_pessoa(3)