# -*- coding: utf-8 -*-
"""  
    Description:  @property 2.1

    Introduzido no python 3.5 (Type Hints (dicas de Tipos) PEP 483 PEP 484)
    https://docs.python.org/3/library/typing.html
    Ele fornece uma maneira de anotar opcionalmente os tipos de funções, 
    argumentos e variáveis ​​do Python de uma maneira que pode ser usada 
    por várias ferramentas, tal como o PyCharm.


    Author:        @palin
    Last Update:   20/01/2018
    Created:       20/01/2018
    Copyright:     (c) MIT
    Version:       1.0
"""

import sys

try:
    import platform
    import os
    # New Python 3.5+_igual o Typescript -> facilita a vida do programador
    # Utilizar no pycharm ou o pacote MyPy
    # O PyCharm verificará se o programador está passando um argumento válido
    # senão já faz o alerta em tempo de desenvolvimento.
    import typing
except Exception as e:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print("#" * 80)
    print("# Description: " + str(e))
    print('# File Name: ' + str(exc_traceback.tb_frame.f_code.co_filename))
    print('# Code Line: ' + str(exc_traceback.tb_lineno))
    print('# Code Name: ' + str(exc_traceback.tb_frame.f_code.co_name))
    print('# Exception Type: ' + str(exc_type.__name__))
    print("#" * 80)
    sys.exit(0)

def info():
    print('-'*80)
    print("Nome deste Arquivo: {0}".format(__file__))
    print("Diretório deste arquivo:{0}".format(os.path.abspath(__file__)))
    print("Arquitetura do S.O.:{0}".format(platform.architecture()))
    print("S.O.:{0}".format(platform.system()))
    print("Python Executado.:{0}".format(platform.python_version()))
    print("Padrão do Sistema.:") 
    os.system("python -V")
    print('-'*80)


class Student:
    """
    Esta classe tem o objetivo de mostrar a funcionalidade do decorator
    @property.

    Corrigindo o problema do script ex02.py - onde o ATRIBUTO pontosganhos
    não foi atualizado. 

    - 1) Podemos substituí-lo por um MÉTODO no lugar de ATRIBUTO.
    - isso funciona como pode ver.
    """
    
    def __init__(self, nome: str, pontos: int):
        self.nome = nome
        self.pontos = pontos

    def pontosganhos(self) -> str:
        return self.nome + ' obteve ' + str(self.pontos) + ' pontos'

if __name__ == '__main__':
    
    if sys.version_info[0] < 3:
        print(
            "Execute o script da seguinte maneira"
            " python3 <nome_script>.py"
        )
        print("Você executou a versão:" + platform.python_version())
        sys.exit()

    #info()

    st = Student("Paulo", "25")
    print(st.nome)
    print(st.pontos)
    print('-'*50)
    #print(st.pontosganhos) #para corrigirmos o problema do ex02.py criamos um método
    # Note que precisamos chamar o metodo com os ()
    print(st.pontosganhos())
    print('-'*50)

    # O que acontece se quero mudar o atributo 'nome'
    print('\n')
    st.nome = "Pedro"
    st.pontos = 33
    print(st.nome)
    print(st.pontos)
    print('-'*50)
    #print(st.pontosganhos) #para corrigirmos o problema do ex02.py criamos um método
    # Note que precisamos chamar o metodo com os ()
    print(st.pontosganhos())
    print('-'*50)

    print('Observe que o Atributo pontos ganhos não foi atualizado!')