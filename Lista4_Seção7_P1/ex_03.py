"""
leia um conjunto de números reais, armazenado como um vetor
calcular o quadrado de cada componente e armazenar em outro vetor
os vetores devem ter 10 elementos
"""

v1 = []
v2 = []

for i in range(10):
    v1.append(i)
    v2.append(i ** 2)
print(f"O primeiro vetor é {v1}\n"
      f"O segundo vetor é {v2}.)")
