def soma_impares(numeros):
    total = 0
    for i in numeros:
        if i % 2 != 0:
            total += i
    return total  # return finaliza a função