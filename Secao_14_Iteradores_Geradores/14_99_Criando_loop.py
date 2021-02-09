"""
Criando sua própria função de loop

[print(i) for i in range(6)]

[print(i) for i in "Geek University"]


def meu_for(iterable):
    it = iter(iterable)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

print(meu_for("Geek University"))

"""

