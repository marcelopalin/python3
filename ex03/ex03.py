# -*- coding: utf-8 -*-
"""  
    Description: Definindo o @nome_da_funcao.setter
    Este decorator permite que façamos atribuições a um ATRIBUTO
    decorado com @property.

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


class PeopleHeight:
    def __init__(self, height = 150):
        self._height = height

    def convert_to_inches(self):
        return (self.height * 0.3937)

    @property
    def height(self):
        print("@property funciona como um getter! Pegando o valor da altura!")
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("A altura de uma pessoa NÃO PODE SER NEGATIVA!")
        print("Foi atribuido o valor da altura com sucesso!")
        self._height = value


if __name__ == '__main__':
    
    if sys.version_info[0] < 3:
        print(
            "Execute o script da seguinte maneira"
            " python3 <nome_script>.py"
        )
        print("Você executou a versão:" + platform.python_version())
        sys.exit()

    #info()

    p = PeopleHeight()
    print('-'*50)
    print("Altura da Pessoa {}".format(p.height))
    print('-'*50)

    print("\nDefinindo a altrua igual a 200 cm")
    p.height = 200
    print('-'*50)
    print("Altura da Pessoa {}".format(p.height))
    print('-'*50)
    
    print("Definindo a altura igual a -100 cm! O decorator deverá causar um Erro! Não pode haver altura negativa!")
    p.height = -100
    print('-'*50)
    print("Altura da Pessoa {}".format(p.height))
    print('-'*50)