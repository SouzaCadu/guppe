"""
Try / Except / Else / Finally


Toda a entrada de dados, principalmente do usuário, deve ser tratada!

Else: É executado apenas se não acontecer o erro

try:
    num = int(input("Informe um número: "))
except ValueError:
    print("Valor incorreto.")
else:
    print(f"Você digitou {num}.")

Finally: É sempre executado, ocorrendo a exceção ou não. Geralmente é utilizado para
         fechar uma conexão com banco de dados, um arquivo lido durante o código.

try:
    num = int(input("Informe um número: "))
except ValueError:
    print("Você não digitou um valor válido.")
else:
    print(f"Você digitou {num}.")
finally:
    print("Executando o finally")

Tratamento individual das entradas em uma função

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return "O valor deve ser numérico."
    except ZeroDivisionError:
        return "Não é possível dividir por zero."


num1 = input("Informe o primeiro número: ")
num2 = input("Informe o segundo número: ")

print(dividir(num1, num2))

Tratamento semi-genérico

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f"Ocorreu um erro {err}."


num1 = input("Informe o primeiro número: ")
num2 = input("Informe o segundo número: ")

print(dividir(num1, num2))

"""



