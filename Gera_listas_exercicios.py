import os


def cria_lista_ex(qtde_ex):
    for i in range(1, qtde_ex + 1):
        print(i)
        arquivo = os.path.join(os.getcwd(), "ex" + "_" + str(i) + ".py")
        print(arquivo)
        try:
            with open(arquivo, "w", encoding='utf-8'):
                print("\nInformações inseridas no arquivo com sucesso!")
        except FileNotFoundError:
            print("\nO arquivo informado não foi encontrado ou o programa não tem permissão para criar um "
                  "diretório/pasta!")
        except OSError:
            print("\nO SO não aceita caracteres especiais em nomes de arquivo!")
        except ValueError:
            print("\nO modo que as informações se encontram no arquivo é inválido!")
        except IndexError:
            print("\nO modo que as informações se encontram no arquivo é inválido!")


diretorio = str(input("Informe o diretorio onde serão criados os arquivos no formato 'Secao_nn_Lista_Ex_nn': "))
os.mkdir(os.path.join(os.getcwd(), diretorio))
os.chdir(os.path.join(os.getcwd(), diretorio))
qtde_ex = int(input(f"Informe quantidade de exercícios a serem feitos: "))
cria_lista_ex(qtde_ex=qtde_ex)


