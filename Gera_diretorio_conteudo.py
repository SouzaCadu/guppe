import os


def cria_arquivos(secao, cod_aula, total_aulas, descr):
    aula_ini = cod_aula
    for i in range(total_aulas):
        cod_aula_atu = aula_ini + i
        arquivo = os.path.join(os.getcwd(), secao + "_" + str(cod_aula_atu) + "_" + descr[i] + ".py")
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


diretorio = str(input("Informe o diretorio onde serão criados os arquivos no formato 'Seção_nn_descrição': "))
os.mkdir(os.path.join(os.getcwd(), diretorio))
os.chdir(os.path.join(os.getcwd(), diretorio))
secao = str(input("Informe o número da seção do curso no formato 'nn': "))
cod_aula = int(input(f"Informe o codigo da primeira aula da seção {secao}: "))
total_aulas = int(input(f"Informe o total de aulas da seção {secao}: "))

descr = []
count = 1
while count <= total_aulas:
    aux = str(input(f"Insira a descrição do conteúdo {count} de {total_aulas}: "))
    descr.append(aux)
    count += 1
print(f"Total de {total_aulas} conteúdos cadastrados com sucesso.")


cria_arquivos(secao, cod_aula, total_aulas, descr)
