"""
Usando decoradores para forçar determinados tipos de dados

def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for (valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))  # str("Geek"), int("3")
            return funcao(*novo_args, **kwargs)

        return converte

    return decorador


@forca_tipo(str, int)
def repete_msg(msg, vezes):
    [print(msg) for vez in range(vezes)]


repete_msg("Geek", "3")


@forca_tipo(float, float)
def dividir(a, b):
    print(a / b)


dividir(3, 4)


"""

