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
