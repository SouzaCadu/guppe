"""
Considerando o tempo de serviço e o valor do salário
determine o aumento total do funcionário
"""

print("Tabela de reajuste anual: \n"
      "Salário        | % Reajuste | Tempo de serviço | Bônus     \n"
      "Até R$ 500     |   25%      | Menor que 1 ano  | Sem Bônus \n"
      "Até R$ 1.000   |   20%      | De 1 a 3 anos    | 100       \n"
      "Até R$ 1.500   |   15%      | De 4 a 6 anos    | 200       \n"
      "Até R$ 2.000   |   10%      | De 7 a 10 anos   | 300       \n"
      "Acima R$ 2.000 |    0%      | Acima de 10 anos | 500         ")
print()

sal = float(input("Informe o valor do salário:"))
tempo = float(input("Informe o tempo de serviço em anos:"))

if sal < 500:
    if tempo < 1:
        novo_sal = sal * 1.25
        print(f"Novo salário é de R$ {novo_sal:.2f}.")
    elif 1 <= tempo <= 3:
        novo_sal = sal * 1.25 + 100
        print(f"Novo salário é de R$ {novo_sal:.2f}.")
    elif 4 <= tempo <= 6:
        novo_sal = sal * 1.25 + 200
        print(f"Novo salário é de R$ {novo_sal:.2f}.")
    elif 7 <= tempo <= 10:
        novo_sal = sal * 1.25 + 300
        print(f"Novo salário é de R$ {novo_sal:.2f}.")
    elif tempo > 10:
        novo_sal = sal + 500
        print(f"Novo salário é de R$ {novo_sal:.2f}.")
elif 500 <= sal <= 1000:
    if tempo < 1:
        novo_sal = sal * 1.2
        print(f"Novo salário é de R$ {novo_sal:.2f}.")
    elif 1 <= tempo <= 3:
        novo_sal = sal * 1.2 + 100
        print(f"Novo salário é de R$ {novo_sal:.2f}.")
    elif 4 <= tempo <= 6:
        novo_sal = sal * 1.2 + 200
        print(f"Novo salário é de R$ {novo_sal:.2f}.")
    elif 7 <= tempo <= 10:
        novo_sal = sal * 1.2 + 300
        print(f"Novo salário é de R$ {novo_sal:.2f}.")
    elif tempo > 10:
        novo_sal = sal + 500
        print(f"Novo salário é de R$ {novo_sal:.2f}.")
elif 1000 < sal <= 1500:
    if tempo < 1:
        novo_sal = sal * 1.15
        print(f"Novo salário é de R$ {novo_sal:.2f}.")
    elif 1 <= tempo <= 3:
        novo_sal = sal * 1.15 + 100
        print(f"Novo salário é de R$ {novo_sal:.2f}.")
    elif 4 <= tempo <= 6:
        novo_sal = sal * 1.15 + 200
        print(f"Novo salário é de R$ {novo_sal:.2f}.")
    elif 7 <= tempo <= 10:
        novo_sal = sal * 1.15 + 300
        print(f"Novo salário é de R$ {novo_sal:.2f}.")
    elif tempo > 10:
        novo_sal = sal + 500
        print(f"Novo salário é de R$ {novo_sal:.2f}.")
elif 1500 < sal <= 2000:
    if tempo < 1:
        novo_sal = sal * 1.1
        print(f"Novo salário é de R$ {novo_sal:.2f}.")
    elif 1 <= tempo <= 3:
        novo_sal = sal * 1.1 + 100
        print(f"Novo salário é de R$ {novo_sal:.2f}.")
    elif 4 <= tempo <= 6:
        novo_sal = sal * 1.1 + 200
        print(f"Novo salário é de R$ {novo_sal:.2f}.")
    elif 7 <= tempo <= 10:
        novo_sal = sal * 1.1 + 300
        print(f"Novo salário é de R$ {novo_sal:.2f}.")
    elif tempo > 10:
        novo_sal = sal + 500
        print(f"Novo salário é de R$ {novo_sal:.2f}.")
elif sal > 2000:
    if tempo < 1:
        print(f"Sem reajuste.")
    elif 1 <= tempo <= 3:
        novo_sal = sal + 100
        print(f"Novo salário é de R$ {novo_sal:.2f}.")
    elif 4 <= tempo <= 6:
        novo_sal = sal + 200
        print(f"Novo salário é de R$ {novo_sal:.2f}.")
    elif 7 <= tempo <= 10:
        novo_sal = sal + 300
        print(f"Novo salário é de R$ {novo_sal:.2f}.")
    elif tempo > 10:
        novo_sal = sal + 500
        print(f"Novo salário é de R$ {novo_sal:.2f}.")
