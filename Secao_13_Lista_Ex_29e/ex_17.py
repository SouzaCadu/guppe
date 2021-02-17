"""
17) Faça um programa que leia um arquivo que contenha as dimensões de uma matrix (linha e coluna), a quantidade de
    posições que serão anuladas, e as posições a serem anuladas (linha e coluna). O programa lê esse arquivo e,
    em seguida, produz um novo arquivo com a matriz com as dimensões dadas no arquivo lido, e todas as posições
    especificadas no arquivo ZERADAS e o restante recebendo o valor 1.

Ex: arquivo "matriz.txt"
3 3 2 /*3 e 3 dimensões da matriz e 2 posições que serão anuladas*/
1 0
1 2   /*Posições da matriz que serão anuladas.

arquivo "matriz_saida.txt"
saida:
1 1 1
0 1 0
1 1 1
"""

import os

print("Informe um arquivo contendo um conjunto de instruções para geração de uma matriz com as seguintes\n"
      "características:\n"
      "Primeira linha: Dimensões da matriz e posições que receberam valor 0 (zero)\n"
      "Ex. l1: 3 3 2 = Matriz 3 x 3 com 2 posições com valor 0 (zero)\n"
      "Segunda e terceira linhas: Coordenadas que terão o valor 0 (zero)\n"
      "Ex. l2: 1 0 Coordenadas da matriz que terão valores 0 (zero)\n"
      "    l3: 1 2 Coordenadas da matriz que terão valores 0 (zero)\n"
      "As posições não especificadas receberão valor 1."
      "No mesmo diretório será construido criado um arquivo com a matriz de acordo com as instruções fornecidas.\n")

path = input("Digite o caminho de um arquivo contendo as instruções para criação da matriz: ")

# captura o nome do arquivo informado pelo usuário
basename = os.path.basename(path)

# extrai o nome do arquivo e a extensão
arquivo_aux, extensao = (os.path.splitext(basename))[0], (os.path.splitext(basename))[1]

novo_arquivo = os.path.join(os.path.dirname(path), arquivo_aux + "_executado" + extensao)

path2 = os.path.dirname(path)

nome_aux = arquivo_aux + "_executado" + extensao


def ler_arquivo(arquivo):
    """
    Função que recebe um arquivo com as instruções para criar a matriz, como suas dimensões, quantos elementos
    serão zerados e quais são eles.
    Formato: n_linhas n_cols n_elems
             i1 j1
             i2 j2
    :param arquivo: Caminho com o arquivo de entrada com as instruções para criar a matriz
    :return: Se executado corretamente imprime o caminho com o novo arquivo gerado
    """

    def cria_matriz(arquivo2):
        """
        Função que gera uma matriz a partir das instruções fornecidas em arquivo pelo usuário.
        As coordenadas definidas pelo usuário recebem 0 (zero) as demais recebem 1.
        :param arquivo2: Arquivo de entrada que contém as instruções para gerar a matriz
        :return: Retorna a matriz geradas de acordo com as instruções do usuário
        """
        with open(arquivo2) as arq:
            info = arq.readlines()
        n_linhas, n_cols, n_elem = int(info[0].split()[0]), int(info[0].split()[1]), int(info[0].split()[2])
        elementos = [[int(n) for n in info[i].split()] for i in range(1, n_elem + 1)]

        # valida os inputs recebidos pelo usuário
        if any(filter(lambda el: el[0] > n_linhas - 1 or el[1] > n_cols - 1, elementos)):
            raise IndexError()

        matriz = [[0 if [i, j] in elementos else 1 for j in range(n_cols)] for i in range(n_linhas)]
        return matriz

    try:
        with open(novo_arquivo, 'w') as arq_out:
            for linha in cria_matriz(arquivo):
                count = 1
                for n in linha:
                    if count != len(linha):
                        arq_out.write(f'{n} ')
                    else:
                        arq_out.write(f'{n}\n')
                    count += 1
        print(f"Processo executado com sucesso em {path2}/{nome_aux}!")
        with open(novo_arquivo) as res:
            print(res.read())
    except FileNotFoundError:
        print("\nO arquivo informado não foi encontrado ou o programa não tem permissão para criar um diretório/pasta!")
    except OSError:
        print("\nO SO não aceita caracteres especiais em nomes de arquivo!")
    except IndexError:
        print("\nO modo que as informações se encontram no arquivo é inválido!")
    except ValueError:
        print("\nO modo que as informações se encontram no arquivo é inválido!")


ler_arquivo(path)
