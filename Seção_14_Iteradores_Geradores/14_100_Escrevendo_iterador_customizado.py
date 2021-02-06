"""
Escrevendo um iterador customizado

# Exemplo de iteração com o range
[print(i) for i in range(11)]


# Criando um iterador customizado
class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration


con = Contador(1, 61)
print(con.menor, con.maior)  # menor acessa 1 e maior acessa 61
it = iter(con)
print(next(it))
print(next(it))

# comparando os dois métodos
[print(i) for i in range(61)]
[print(i) for i in Contador(1, 61)]

"""
