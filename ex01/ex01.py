#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""  
    Description: Entendendo Decorator

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

# ------------------------------------------------------------------
# Toda Função é um Objeto de Primeira Classe do Python
# ------------------------------------------------------------------
def party():
    '''
    Funções Aninhadas - Nested Functions

    - O fato de que tudo em Python é um Objeto define
    que as funções/métodos sejam Objetos de Primeira Classe
    '''
    
    print("Estou dentro da função party()!")

    def start_party():
        return("Início da Party! Uma função dentro da função party()!")

    def finish_party():
        return("Final da Party! Outra função dentro da função!")
        
    print(start_party())
    print(finish_party())
    # ------------------------------------------------------------------

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


if __name__ == "__main__":

    if sys.version_info[0] < 3:
        print(
            "Execute o script da seguinte maneira"
            " python3 <nome_script>.py"
        )
        print("Você executou a versão:" + platform.python_version())
        sys.exit()

    info()
    # Chamando o Método/Função 
    party()

    #Não é possível chamar a função que está dentro de party()
    start_party()
