"""
24) Implemente um controle simples de mercadorias em umas despensa domésticas. Para cada produto armazene um código
    numérico, descrição e quantidade atual. O programa deve ter opções para entrada e retirada de produtos, bem como
    um relatório geral e um de produtos não disponíveis. Armazene os dados em arquivo binário.
"""

dict_produto = {}.fromkeys(["produto1"], ["código", "descrição", "quantidade"])
print(dict_produto, type(dict_produto))