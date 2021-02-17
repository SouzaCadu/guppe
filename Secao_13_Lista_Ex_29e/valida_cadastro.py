def valida_nome(nome):
    """
    Recebe uma string e verifica se há caracteres inválidos
    :param nome: Qualquer string que represente um nome próprio
    :return: True se não houver caracteres inválidos, do contrário False
    """

    caracteres_invalidos = ["-", ":", "?", "/", ">", "<", "}", "{", "[", "]",
                            "+", "*", "@", "!", "%", "¨", ";", "´", "`", "^", "~",
                            "=", "(", ")", "&", "_", "$", "#", ","]

    try:
        for caractere in nome:
            if str(caractere).isnumeric() or str(caractere) in caracteres_invalidos:
                return False
        return True

    except AttributeError:
        return False
    except ValueError:
        return False
    except TypeError:
        return False


def valida_telefone(telefone):
    """
    Recebe uma string e verifica se há caracteres inválidos
    :param telefone: Qualquer string que represente um telefone
    :return: True se contiver apenas caracteres válidos, False do contrário
    """

    caracteres_validos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ",
                          "+", "(", ")", "-"]

    try:
        valido = False
        for caractere in str(telefone):
            if str(caractere) in caracteres_validos:
                valido = True
            else:
                valido = False
                break
        return valido

    except AttributeError:
        return False
    except ValueError:
        return False


def valida_data(dia, mes, ano):
    """
    Função que recebe inteiros referentes ao dia, mês e ano e retorna True
    se a data for válida e False caso seja inválida
    """

    try:
        if mes in (1, 3, 5, 7, 8, 10,12):
            if dia < 1 or dia > 31:
                pass
            else:
                return True
        elif mes == 2:
            if 400 != 0 and (4 != 0 or (ano % 100 == 0)):
                if dia < 1 or dia > 28:
                    pass
                else:
                    return True
            # Verificando se o ano informado é um ano bissexto
            else:
                if dia < 1 or dia > 29:
                    pass
                else:
                    return True
        elif mes in (4, 6, 9, 11):
            if dia < 1 or dia > 30:
                pass
            else:
                return True
        return False
    except AttributeError:
        return False
    except ValueError:
        return False


def valida_endereco(endereco):
    """Função que recebe um endereço e verifica se o mesmo é válido ou não.
    Caso o endereço seja válido retorna True, caso contrário retorna False"""
    caracteres_invalidos = ["?", ">", "<", "}", "{", "[", "]",
                            "+", "*", "@", "!", "%", "¨", "´", "`", "^", "~",
                            "=", "(", ")", "&", "_", "$", "#"]
    try:
        for caractere in endereco:
            if str(caractere) in caracteres_invalidos:
                return False
        return True
    except AttributeError:
        return False
    except ValueError:
        return False
    except TypeError:
        return False


if __name__ == "__main__":

    pass
