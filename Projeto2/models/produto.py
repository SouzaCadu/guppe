from utils.helper import formata_float_str_moeda


class Produto:
    contador: int = 1

    def __init__(self: object, nome: str, preco: float) -> None:
        self.__codigo_produto: int = Produto.contador
        self.__nome: str = nome.title()
        self.__preco: float = preco
        Produto.contador += 1

    @property
    def codigo(self: object) -> int:
        return self.__codigo_produto

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def preco(self: object) -> float:
        return self.__preco

    def __str__(self: object) -> str:
        return f"Código do produto: {self.codigo} \nNome: {self.nome} \nPreço: {formata_float_str_moeda(self.preco)}."