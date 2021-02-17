"""
para representar um ponto em uma grade 2D, implemente uma função que indique se um
ponto p está localizado dentro ou fora de um retângulo.
o retângulo é definido por seus vértices inferior esquerdo v1 e superior direito v2.
a função deve retornar 1 caso o ponto esteja localizado dentro do retângulo e 0 caso contrário.
"""


def dentro_ret(x1, y1, x2, y2, p1, p2):
    """
    Função que recebe as posições do vértice inferior esquerdo e superior direto de um
    retângulo
    :param x1: Posição da coordenada X do vértice inferior esquerdo
    :param y1: Posição da coordenada Y do vértice inferior esquerdo
    :param x2: Posição da coordenada X do vértice superior direito
    :param y2: Posição da coordenada Y do vértice superior direito
    :param p1: Posição da coordenada X do ponto indicado
    :param p2: Posição da coordenada Y do ponto indicado
    :return: Retorna 1 caso as coordenadas informadas esteja dentro do retângulo e 0 caso contrário.
    """

    if x1 <= p1 <= x2:
        if y1 <= p2 <= y2:
            return 1
    return 0


vertice_x1 = int(input("Local da coordenada x do vértice inferior esquerdo do retângulo: "))
vertice_y1 = int(input("Local da coordenada y do vértice inferior esquerdo do retângulo: "))
vertice_x2 = int(input("Local da coordenada x do vértice superior direita do retângulo: "))
vertice_y2 = int(input("Local da coordenada y do vértice superior direita do retângulo: "))

coordenada_p1 = int(input("Local da coordenada x do ponto: "))
coordenada_p2 = int(input("Local da coordenada y do ponto: "))

print(f"\n{dentro_ret(vertice_x1, vertice_y1, vertice_x2, vertice_y2, coordenada_p1, coordenada_p2)}")
