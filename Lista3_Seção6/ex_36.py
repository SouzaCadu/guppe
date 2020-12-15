"""
faça um programa que a calcule a diferença entre a soma dos quadrados
dos primeiros 100 números naturais e o quadrado da soma
"""

print("Calcula a diferença entre a soma dos quadrados\n"
      "dos primeiros 100 números naturais e o quadrado da soma.")

soma_quad = 0
quad_soma = 0

for i in range(101):
    soma_quad += i ** 2
    quad_soma += i
print(f"O resultado é {soma_quad - (quad_soma ** 2)}")
