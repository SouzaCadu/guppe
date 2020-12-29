"""
Dada a quilometragem e quantidade de litros consumidos
calcule o consumo em km/l
"""

print("Para saber a eficiência do carro informe:")

km = float(input("A distância em quilômetros:"))
l = float(input("A quantidade de litros de gasolina consumidos \n"
                "por quilômetro percorrido:"))

km_l = km / l

if km_l < 8.0:
    print("Venda o carro!")
elif 8.0 <= km_l <= 14.0:
    print("Econômico!")
else:
    print("Super econômico!")
