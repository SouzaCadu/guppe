"""
Avaliação do aluno por nota e número de faltas
"""

print("Tabela de avaliação: \n"
      "Nota             | Conceito (até 20 faltas) | Conceito (+ 20 faltas) \n"
      "Entre 9.0 e 10.0 |        A                 |        B  \n"
      "Entre 7.5 e 8.9  |        B                 |        C  \n"
      "Entre 5.0 e 7.4  |        C                 |        D  \n"
      "Entre 4.0 e 4.9  |        D                 |        E  \n"
      "Entre 0.0 e 3.9  |        E                 |        E  \n")
print()

nota = float(input("Digite a nota do aluno:"))
print()
faltas = int(input("Digite a quantidade de faltas:"))
print()

if 0.0 <= nota <= 3.9:
    print("Conceito E")
elif 4.0 <= nota <= 4.9:
    if faltas < 20:
        print("Conceito D")
    else:
        print("Conceito E")
elif 5.0 <= nota <= 7.4:
    if faltas < 20:
        print("Conceito C")
    else:
        print("Conceito D")
elif 7.5 <= nota <= 8.9:
    if faltas < 20:
        print("Conceito B")
    else:
        print("Conceito C")
if nota >= 9.0:
    if faltas < 20:
        print("Conceito A")
    else:
        print("Conceito B")
