"""
Métodos mágicos

São todos os métodos que utilizam "dunder" (double undersocer).

Implementar métodos existentes do Python para trabalhar da forma que precisarmos. São métodos da classe
object.

"""


class Livro:

    # método construtor de objetos em Python
    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    # Representação do objeto
    def __repr__(self):
        return f"{self.__titulo} escrito por {self.__autor}."

    # Representação do objeto com string
    # tem prioridade sobre o __repr__ na execução
    def __str__(self):
        return f"{self.__titulo}."

    def __len__(self):
        return self.__paginas

    # gerar alerta para exclusão em memória
    def __del__(self):
        print("Um objeto da classe livro foi apagado da memória.")

    # alterando o comportamento da função concatenar
    def __add__(self, other):
        return f"{self} - {other}"

    # alterando o comportamento da função concatenar
    def __mul__(self, other):
        if isinstance(other, int):
            msg = " "
            [print(" " + str(self)) for i in range(other)]
        return "Não é possível multiplicar"


livro1 = Livro("Python para todos", "Geek University", 400)
livro2 = Livro("Python para desenvolvedores", "Geek University", 550)

print(livro1, livro2)
print("--" * 10)
print(len(livro1), len(livro2))
print("--" * 10)
print(livro1 + livro2)
print("--" * 10)
print(livro1 * 3)
print("--" * 10)