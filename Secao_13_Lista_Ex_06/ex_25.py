"""
25) Faça um programa gerenciar uma agenda de contatos. Para cada contato armazene o nome, o telefone e o aniversário
    (dia e mes). O programa deve permitir
    (a) Inserir contato
    (b) remover contato
    (c) pesquisar um contato pelo nome
    (d) listar todos os contatos
    (e) listar os contatos cujo nome inicia com uma dada letra
    (f) imprimir os aniversariantes do mês
    Sempre que o programa for encerrado, os contatos devem ser armazenados em um arquivo binário.
    Quando o programa iniciar, os contatos devem ser inicializados com os dados contidos neste arquivo binário.
"""

import pickle
from valida_cadastro import valida_nome, valida_telefone


def cadastrar_contato(agenda, nome, telefone, aniversario):
    if valida_nome(nome):
        if valida_telefone(telefone):
            cadastro = [nome, telefone, aniversario]
    agenda.append(cadastro)


def remover_contato(agenda, nome):
    y = 0
    for contato in agenda:
        if nome == contato[0]:
            if agenda[y].pop:
                print(f"{contato[0]} removido com sucesso.")
        y += 1


def pesquisar_contato(agenda, nome):
    for contato in agenda:
        if nome == contato[0]:
            print(f"Nome = {contato[0]}, telefone {contato[1]}, aniversário {contato[2]}")


def contatos_cadastrados(agenda):
    print("-" * 117)
    print(f"{'-' * 50}Lista de contatos{'-' * 50}")
    print("-" * 117)
    print(f"{'-' * 20}Nome{'-' * 20} | {'-' * 12}Telefone{'-' * 12} | {'-' * 12}Aniversário{'-' * 12}")
    print("-" * 117)
    for contato in agenda:
        print(f' {contato[0]} | {contato[1]}  | {contato[2]}')
        print("-" * 117)


def listar_contatos_inicial(agenda, letra):
    for contato in agenda:
        for i in contato[0]:
            if i == letra:
                print(f'{contato[0]} | {contato[1]} | {contato[2]} ')


def aniversariantes(agenda, mes):
    for contato in agenda:
        _, var = contato[2].split("/")
        if mes == var:
            print(f'{contato[0]} | {contato[1]} | {contato[2]} ')


def menu_principal(agenda):
    while True:
        print("=" * 117)
        print('Agenda de contatos')
        print('Selecione a opção desejada:')
        print('> 1 - Inserir um contato')
        print('> 2 - Deletar um contato')
        print('> 3 - Pesquisar um contato pelo nome')
        print('> 4 - Listar todos os conatos')
        print('> 5 - Pesquisar contatos pela primeira letra do nome')
        print('> 6 - Imprimir lista de aniversariantes do mes')
        print('> 7 - Sair e Salvar')
        opcao = int(input('Digite a opção desejada: '))
        print("=" * 117)
        if opcao == 1:
            print("Cadastrar um contato")
            nome = input("Digite o nome do contato: ")
            telefone = input(f"Digite o telefone de {nome}: ")
            mm = abs(int(input(f"Digite o mês do aniversário de {nome}: ")))
            dd = abs(int(input(f"Digite o dia do aniversário de {nome}: ")))
            if ((mm > 0) and (mm < 13)) and ((dd > 0) and (dd < 32)):
                mes = str(mm)
                dia = str(dd)
                if len(mes) != 1:
                    pass
                else:
                    mes = "0" + mes
                if len(dia) != 1:
                    pass
                else:
                    dia = "0" + dia
                aniversario = dia + "/" + mes
            cadastrar_contato(agenda, nome, telefone, aniversario)

        elif opcao == 2:
            print('Deletar um contato')
            contato = input('> Contato a ser removido.......: ')
            remover_contato(agenda, contato)

        elif opcao == 3:
            print('Pesquisar contato pelo nome')
            nome = input('> Contato a ser pesquisado.......: ')
            pesquisar_contato(agenda, nome)

        elif opcao == 4:
            contatos_cadastrados(agenda)

        elif opcao == 5:
            print('Pesquisar contatos pela primeira letra do nome')
            letra = input('> Primeira letra do nome.......: ').upper()
            listar_contatos_inicial(agenda, letra)

        elif opcao == 6:
            print('Aniversariantes do mês')
            mm = abs(int(input('> Digite o mês.......: ')))
            if 0 < mm < 13:
                mes = str(mm)
                if len(mes) != 1:
                    pass
                else:
                    mes = "0" + mes
            aniversariantes(agenda, mes)

        elif opcao == 7:
            return
        else:
            print("Opção inválida!")


try:
    agenda = pickle.load(open('l13_ex25_agenda.bin', 'rb'))
    menu_principal(agenda)
    print('\nSalvando cadastro...')
    pickle.dump(agenda, open('l13_ex25_agenda.bin', 'wb'))
except FileNotFoundError:
    print('Criando cadastro...')
    agenda = []
    menu_principal(agenda)
    pickle.dump(agenda, open('l13_ex25_agenda.bin', 'wb'))
except IOError:
    print('Problemas no arquivo de cadastro.')
