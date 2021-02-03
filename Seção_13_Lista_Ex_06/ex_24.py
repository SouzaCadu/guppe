"""
24) Implemente um controle simples de mercadorias em umas despensa domésticas. Para cada produto armazene um
    código numérico, descrição e quantidade atual. O programa deve ter opções para entrada e retirada de produtos,
    bem como um relatório geral e um de produtos não disponíveis. Armazene os dados em arquivo binário.
"""

import pickle


def cadastrar_produto(cadastro, codigo, descricao, unidade):
    h = 20 - len(codigo)
    codigo += ' ' * h
    h = 20 - len(descricao)
    descricao += ' ' * h
    h = 20 - len(unidade)
    unidade += ' ' * h
    produto = [codigo, descricao, int(0), unidade]
    cadastro.append(produto)


def entrada_produto(cadastro, codigo, qtd):
    y = 0
    for produto in cadastro:
        if codigo == produto[0]:
            cadastro[y][2] += qtd
        y += 1


def retirada_produto(cadastro, codigo, qtd):
    y = 0
    for produto in cadastro:
        if codigo == produto[0]:
            if cadastro[y][2] < qtd:
                print(f'Produto possui apenas {cadastro[y][2]} {cadastro[y][3]}')
            else:
                cadastro[y][2] -= qtd
        y += 1


def listar_produtos(cadastro):
    print("-" * 117)
    print(f"{'-' * 51}Relatório Geral{'-' * 51}")
    print("-" * 117)
    print(f"{'-' * 10}Código{'-' * 10} | {'-' * 10}Produto{'-' * 10} | {'-' * 10}Quantidade{'-' * 10} | "
          f"{'-' * 9}Unidade{'-' * 9}")
    print("-" * 117)
    for produto in cadastro:
        print(f' {produto[0]} | {produto[1]}  | {produto[2]}  | {produto[3]}')
        print("-" * 117)


def produtos_indisponiveis(cadastro):
    print("-" * 117)
    print(f"{'-' * 49}Itens indisponíveis{'-' * 49}")
    print("-" * 117)
    print(f"{'-' * 10}Código{'-' * 10} | {'-' * 10}Produto{'-' * 10} | {'-' * 10}Quantidade{'-' * 10} | "
          f"{'-' * 9}Unidade{'-' * 9}")
    print("-" * 117)
    for produto in cadastro:
        if produto[2] == 0:
            print(f' {produto[0]} | {produto[1]}  | {produto[2]}  | {produto[3]}')
            print("-" * 117)


def menu_principal(cadastro):
    while True:
        print("=" * 117)
        print('Controle da despensa')
        print('Selecione a opção desejada:')
        print('> 1 - Cadastrar')
        print('> 2 - Entrada')
        print('> 3 - Retirada')
        print('> 4 - Relatório Geral')
        print('> 5 - Produtos Indisponíveis')
        print('> 6 - Sair e Salvar')
        opcao = int(input('Digite a opção desejada: '))
        print("=" * 117)
        if opcao == 1:
            print('Cadastro de Produto')
            cod = input('> Código.......: ')
            dsc = input('> Descrição....: ')
            uni = input('> Unidade......: ')
            cadastrar_produto(cadastro, cod, dsc, uni)

        elif opcao == 2:
            print('Entrada de Produto')
            cod = input('> Código.......: ')
            qtd = int(input('> Quantidade...: '))
            entrada_produto(cadastro, cod, qtd)

        elif opcao == 3:
            print('Retirada de Produto')
            cod = input('> Código.......: ')
            qtd = int(input('> Quantidade...: '))
            retirada_produto(cadastro, cod, qtd)

        elif opcao == 4:
            listar_produtos(cadastro)

        elif opcao == 5:
            produtos_indisponiveis(cadastro)

        elif opcao == 6:
            return
        else:
            print("Opção inválida!")


try:
    cadastro = pickle.load(open('l13_ex24_controle_despensa.bin', 'rb'))
    menu_principal(cadastro)
    print('\nSalvando cadastro...')
    pickle.dump(cadastro, open('l13_ex24_controle_despensa.bin', 'wb'))
except FileNotFoundError:
    print('Criando cadastro...')
    cadastro = []
    menu_principal(cadastro)
    pickle.dump(cadastro, open('l13_ex24_controle_despensa.bin', 'wb'))
except IOError:
    print('Problemas no arquivo de cadastro.')
