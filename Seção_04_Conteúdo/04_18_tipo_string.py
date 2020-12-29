"""
Tipo string

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre aspas simples
- Estiver entre aspas duplas
- Estiver entre aspas simples triplas

nome = 'Geek University'
nome1 = "China"
nome2 = '''USA '''

print(nome, type(nome),
      nome1, type(nome1),
      nome2, type(nome2))

restaurant = "Gina's Bar"
print(restaurant, type(restaurant))

atriz = "Angelina \n Jolie"
print(atriz, type(atriz))

prof = "geek university"
print(prof.upper(), prof.lower(), prof.title(), prof.split())

prof = 'Geek University'
lista = prof.split()
print(lista[0].upper(), lista[1].title())
print(prof[0:4], prof[5:], lista)
print(prof[:: -1]) # Imprimir na ordem inversa
print(prof.isupper(), prof.islower(), prof.istitle())
print(prof.replace('e', 'o'))

texto = 'socorram me subindo onibus em marrocos'
print(texto)
print(texto[:: -1])
"""
