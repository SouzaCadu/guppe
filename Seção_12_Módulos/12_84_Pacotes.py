"""
Pacotes

Módulo é um arquivo Python com diversas funções, enquanto um pacote é um diretório com diversos módulos.

Nas versões 2.x do Python, um pacote precisava conter dentro dele um arquivo __init__.py, esse arquivo tornou-se
dispensável a partir da versão 3.x, mas ainda assim são criados para manter a compatibilidade entre as versões.

Estrutura de pacotes com módulos e submódulos

dir
    __init__.py
    arq1.py
    arq2.py

    dir 1
        __init__.py
        arq3.py
        arq4.py

        dir 1.1
            __init__.py
            arq5.py
            arq6.py
    dir 2
        __init__.py
        arq7.py
        arq8.py

from dir import arq1, arq2

from dir.dir1 import arq3, arq4

from dir.dir 1.dir 1.1 import arq5

from dir.dir 1.dir 1.1.arq5 import funcao


"""

