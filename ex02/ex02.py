# -*- coding: utf-8 -*-
"""  
    Description: Decorator Embutido @property

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

    Python @property é um dos decoradores embutidos. 
    O objetivo principal de QUALQUER DECORATOR é mudar seus métodos/funções 
    ou atributos de classe de tal forma que o usuário 
    da sua classe não precise fazer qualquer alteração em seu código.

    O conceito de decorator provê uma maneira simples de modificar 
    o comportamento de uma função sem necessariamente alterá-la.
    """
    
    def __init__(self, nome, pontos):
        self.nome = nome
        self.pontos = pontos
        self.pontosganhos = self.nome + ' obteve ' + self.pontos + ' pontos'

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
    print(st.pontosganhos)
    print('-'*50)

    # O que acontece se quero mudar o atributo 'nome'
    print('\n')
    st.nome = "Pedro"
    st.pontos = 33
    print(st.nome)
    print(st.pontos)
    print('-'*50)
    print(st.pontosganhos) 
    print('-'*50)

    print('Observe que o Atributo pontos ganhos não foi atualizado!')