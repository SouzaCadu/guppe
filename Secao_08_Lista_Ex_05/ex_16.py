"""
Faça uma função chamada DesenhaLinha. Ele deve desenhar uma linha na tela usando
vários símbolos de igual (Ex.: ========). A função recebe por parâmetro quantos
sinais de igual serão mostrados.
"""


def desenha_linha(tamanho):
    """
    Desenha uma linha na tela usando vários símbolos de igual
    :param tamanho: Quantos sinais de igual serão mostrados
    :return: vários símbolos de igual (Ex.: ========)
    """
    print(f"{'=' * tamanho}")


print(desenha_linha(12))