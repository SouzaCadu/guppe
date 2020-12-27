"""
Definindo funções

- Funções são pequenos blocos de código que realizam ações específicas.
- Podem ou não ter parâmetros de entrada ou retornos de saída.
- São reutilizáveis
- Devem realizar apenas uma função, evite criar funções que executem
  muitas tarefas
- Facilita o uso do princípio DRY (don't repeat yourself)

Já utilizamos funções como:
- print()
- len()
- max()
- min()
- count()

São definidas como:

def nome_da_função(parâmetros de entrada):
    bloco da função

Onde:

- nome_da_função - sempre em minúsculo, se composto, utiliza-se under score.
- parâmetro_de_entrada - opcional, são inputs para a função, se houver mais de um
  separar por vírgula
- bloco_da_função - é onde o processamento acontece, podendo ou não ter retorno

Para definir uma função utiliza-se a palavra reservada def, o bloco
de código é aberto com dois pontos (:), e os blocos são indentados

"""

# Exemplo de utilização de funções:

cores = ["verde", "amarelo", "branco", "azul"]
print(cores)  # print recebe parâmetros de entrada

curso = "Programação em Python: Essencial do básico ao avançado."
print(curso)

cores.append("laranja")
print(cores)

cores.clear()  # clear não recebe parâmetros de entrada
print(cores)


# Definindo uma função

def hello_world():
    print("Hello world!")


hello_world()  # chamada de execução


def cantar_parabens():
    print("\nParabéns pra você!"
          "\nNessa data querida"
          "\nmuitas felicidades"
          "\nmuitos anos de vida!"
          "\nViva o aniversariante!!!")


for i in range(5):
    cantar_parabens()

"""
1 - Dentro de uma função podemos executar outras funções
2 - A função executa apenas uma tarefa
3 - Essa função não recebe nenhum parâmetro de entrada
4 - Essa função não tem retorno, apenas executa o print
"""

#  Uma função pode ser atribuida a uma variável
#  o que não é tão comum, se necessário volte e
#  mude o nome da função