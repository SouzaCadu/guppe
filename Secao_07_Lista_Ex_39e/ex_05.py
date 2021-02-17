"""
leia um vetor de 10 posições.
conte e escreva quantos valores pares ele possui
"""

v1 = []

for i in range(10, 19):
    v1.append(i)

count = 0

for i in v1:
    if i % 2 == 0:
        count += 1
print(count)
