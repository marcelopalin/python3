#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""  
    Description: Entendendo Decorator 1.1

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
# "Criador" de funções de potência
def cria_potencia(x):
    def potencia(num):
        return x ** num
    return potencia
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

    # Potência de 2 e 3
    print(
        "Chamando uma função que executa outra função dentro"
        " dela para calculo da potência de um número."
     )

    num_1 = 3
    num_2 = 4

    func_potencia_criada_01 = cria_potencia(num_1)
    func_potencia_criada_02 = cria_potencia(num_2)

    print("Atenção: o método cria_potencia() retorna uma função!")
    print("Para você ter uma ideia basta imprimi-la no terminal: ")
    print(func_potencia_criada_01)

    print(
        "Para utiliza-la temos que passar outro parâmetro para a função"
        " criada chamada potencia(num)"
    )

    # Calcularemos a Potencia de 2 dos numeros 3 e 4
    # pot(3,2) = 3 * 3 = 3 ** 2 = 9
    # pot(4,2) = 4 * 4 = 4 ** 2 = 16

    pot = 2
    # Resultado
    print("{0} elevado a {1} = {2}".format( num_1, pot, func_potencia_criada_01(pot) ))
    print("{0} elevado a {1} = {2}".format( num_2, pot, func_potencia_criada_02(pot) ))
    