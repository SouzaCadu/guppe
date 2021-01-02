"""
PEP8 - Python Enhancement Proposal

São propostas de melhoriana lingugem Python

The Zen of Python

import this

[1] Utilize Camel Case para nomes de clases
[2] Utilize nomes em minúsculo, separados por underline para funções ou variavéis
[3] Utilize 4 espaços para a identação
[4] Linhas em branco -
    2 linhas em branco entre classes
    1 linha em branco entre as definições de mesma classe
[5] Imports devem ser feitos em linhas separadas

# Import errado
import os, sys

# Import certo

import sys
import os

# Import de até 2 objetos da mesma biblioteca

from types import StringType, ListType

# Import de + 2 objetos da mesma biblioteca

from types import(
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo e logo depois do docstring
# antes de constantes e variavéis globais

[6] Espaço entre expressões e instruções
    função( algo[ 1 ], {outro: 2 } ) --> errado
    função(algo[1], {outro:2}) --> certo

[7] Termine sempre uma instrução com uma nova linha
"""

import this
