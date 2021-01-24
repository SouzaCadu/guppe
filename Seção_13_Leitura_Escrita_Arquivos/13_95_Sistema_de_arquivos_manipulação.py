"""
Manipulação de arquivos

import os

# Verifica se um arquivo existe
print(os.path.exists("texto.txt"))  # True
print(os.path.exists("lista_compras.txt"))  # True

# Verifica se um diretório existe
print(os.path.exists("teste"))  # True
print(os.path.exists("university"))  # False
print(os.path.exists("/Seção_12_Módulos"))  # False
print(os.path.exists("../Seção_12_Módulos"))  # True

# Criando arquivos

# Forma 1
open("arquivo_teste1.txt", "w").close()

# Forma 2
open("arquivo_teste2.txt", "a").close()

# Forma 3
with open("arquivo_teste3.txt", "w") as teste:
    pass

# Forma 4
os.mknod("arquivo_teste4.txt")  # Ococrerá um erro pq está sendo executado no macOS sem permissão de administrador

# Criando diretórios

#os.mkdir("templates")  # Cria um diretório caso ele não exista

# criando árvore de diretórios

os.makedirs("templates/geek/teste", exist_ok=True)

# Renomeando diretórios
os.rename("templates/geek/teste", "templates/geek/university")

# Renomeando arquivos
os.rename("templates/geek/university/Modulo_teste.py", "templates/geek/university/funcoes.py")

# Apagando arquivos
os.remove("templates/geek/university/funcoes.py")

# Apagando diretórios vazios
os.rmdir("templates/geek/university")

# Removendo árvore de diretórios
os.removedirs("templates/geek/teste")

Obs. Sempre que apagamos algo com Python não será enviado para lixeira, para que isso aconteça precisamos de um
pacote de terceiros

Criando um diretório temporário, abrindo e criando um arquivo dentro dele. O comando input no final é usado apenas para
manter o arquivo aberto dentro do bloco with.

with tempfile.TemporaryDirectory() as tmp:
    print(f"Criei um diretório temporário em {tmp}")
    with open(os.path.join(tmp, "arquivo_temporario.txt"), "w") as arquivo:
        arquivo.write("Geek University\n")
    input()

# Criando um arquivo temporário. Usa apenas dados binários, por isso inicia com "b"
with tempfile.TemporaryFile() as tmp:
    tmp.write(b"Geek University: Programacao em Python\n")
    tmp.seek(0)
    print(tmp.read())

"""

import os, tempfile





