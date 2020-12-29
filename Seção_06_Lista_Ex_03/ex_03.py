"""
Contagem regressiva de 10 até 0, com while, exibindo "FIM"
"""

x = 10
while x >= 0:
    print(x, end=" ")
    x = x - 1
    if x == 0:
        print("FIM!")
        break
