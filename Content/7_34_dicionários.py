"""
Dicionários

São coleções do tipo chave/valor.

São representados por { } (chaves) - print(type({}))

Chave e valor são separados por " : " (dois pontos) e tanto chave quanto valor
podem ser de qualquer tipo de dado (lista, tupla, dicionário, boolean).

# Uso de dicionários

Oferece uma vantagem de acesso as informações quando comparada com listas e tuplas,
pois permite mais informação por variável.
Por exemplo, carrinho de compras em um e-commerce

paises = {"br": "Brasil", "eua": "Estados Unidos", "py": "Paraguai", "nz": "Nova Zelandia"}
print(paises)
print(type(paises))

countries = dict(br="Brasil", eua="Estados Unidos", py="Paraguai", fr="França")
print(countries)
print(type(countries))

# Acessando elementos, dicionários não são indexados

# Via chave, deve fazer parte do dicionário
print(paises["br"], paises["py"])

# Via get - forma recomendada - se não fizer do dicionário retorna "None"
# facilita o tratamento de erro, pois retorna um tipo de dados que é o "None"
# com o get é possível definir um valor padrão em caso de erro

print(countries.get("br"))
print(countries.get("nz"))

country = countries.get("nz")

if country == "Nova Zelandia":
    print("País encontrado")
else:
    print("País não encontrado")

country = countries.get("aus", "País não localizado")
print(country)

# Localizando objetos, através da chave, se ela está ou não em um dicionário
print("br" in paises)
print("Estados Unidos" in paises)

if "az" in countries:
    print("Australia")

# Definindo chaves em um dicionário
# tuplas tem a vantagem de serem imutáveis

localidades = {
    (35.6895, 39.6917): "Tóquio",
    (40.7128, 74.0060): "Nova York",
    (37.7789, 150.2310): "São Paulo"
}
print(localidades)

# Adicionando elementos em um dict

receita = {"jan": 100, "fev": 150, "abr": 200, "mar": 300}
print(receita)

# forma 1
receita["mai"] = 350
print(receita)

# forma 2
novo_mes = {"mai": 450, "jun": 550}
receita.update(novo_mes)
print(receita)

# A forma de atualizar e visualizar dados em um dict é a mesma
# Não podemos ter chaves repetidas, se passarmos uma chave que já existe os dados serão atualizados

# Como remover dados de um dict

# forma 1 (a mais comum, retorna um valor)
receita.pop("jun")  # precisa sempre passar a chave , se não existir retorna um erro
print(receita)

# ao remover um objeto o valor desse objeto deve sempre retornar um valor

# forma 2 (não retorna um valor)
del receita["mai"]
print(receita)

# Métodos para dicionários

# limpar um dicionário

receita.clear()
print(receita)

# Deep copy

countries_1 = countries.copy()
print(countries_1)
countries_1["jp"] = "Japan"
print(countries_1)

# Shallow copy

countries_2 = countries_1
print(countries_2)
countries_2["it"] = "Italia"
print(countries_2)
print(countries_1)

# Forma não usual de criar dicionários

dict1 = {}.fromkeys("a", "b")
print(dict1, type(dict1))

dict_user = {}.fromkeys(["nome", "e-mail", "endereço", "celular"], "desconhecido")
print(dict_user, type(dict_user))

dict_range = {}.fromkeys(range(1, 11), "novo")
print(dict_range, type(dict_range))

dict_string = {}.fromkeys("Geek University", "novo")  # não serão criadas chaves para letras repetidas
print(dict_string, type(dict_string))

# usando o método fromkeys é possivel criar dicionário passando dois valores
# um iterável (lista, tupla, dicionário, string) e um valor
# Para cada valor do iterável ele criará um chave e atribuirá o valor a essa chave

"""
