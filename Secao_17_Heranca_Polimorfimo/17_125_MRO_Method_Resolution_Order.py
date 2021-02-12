"""
Method Resolution Order

Quando temos mais de uma herança contendo o mesmo método a ordem da herança impacta na resolução, quem será
executado primeiro.

Há 3 formas para checar a MRO

- Via propriedade da classe .__mro__
Hibrido.__mro__
(<class 'MRO.Hibrido'>, <class 'MRO.Aquatico'>, <class 'MRO.Terrestre'>, <class 'MRO.Pokemon'>, <class 'object'>)


- Via método
 Hibrido.mro()
[<class 'MRO.Hibrido'>, <class 'MRO.Aquatico'>, <class 'MRO.Terrestre'>, <class 'MRO.Pokemon'>, <class 'object'>]


- Via help
help(Hibrido)
Help on class Hibrido in module MRO:

class Hibrido(Aquatico, Terrestre)
 |  Hibrido(nome)
 |
 |  Method resolution order:
 |      Hibrido
 |      Aquatico
 |      Terrestre
 |      Pokemon
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __init__(self, nome)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from Aquatico:
 |
 |  cumprimentar(self)
 |
 |  nadar(self)
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from Terrestre:
 |
 |  andar(self)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Pokemon:
 |
 |  __dict__


"""

