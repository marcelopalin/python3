#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""  
    Description: Decorator

    O Decorator @tempo_execucao é um método que recebe uma função de parâmetro
    insere linhas adicionais antes da execução da função, executa-a e
    depois imprime o tempo gasto na execução da função.

    Ou seja, ele modificou o comportamento da função que ficar abaixo dele.

    Uso: 
    @tempo_execucao
    def funcao_a_ser_alterada()
      print("fui alterada")

    Atenção: a partir da versão 3.3 do python ocorreram modificações
    no pacote time - foram criados os métodos process_time e perf_counter
    Veja: https://docs.python.org/3/library/time.html#module-time

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
    import time
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


# Define nosso decorator
def tempo_execucao(funcao):
    def wrapper():
        # Calcula o tempo de execução
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()

        # Formata a mensagem que será mostrada na tela
        print("[{funcao}] Tempo total de execução: {tempo_total}".format(
            funcao=funcao.__name__,
            tempo_total=str(tempo_final - tempo_inicial))
        )

    return wrapper

# -----------------------------------------------------
#  Utilizando o Decorator @tempo_execucao que criamos
# -----------------------------------------------------
@tempo_execucao
def funcao_loop():
    for n in range(0, 10000000):
        pass # Nao executa nada, apenas roda o loop

if __name__ == "__main__":

    if sys.version_info[0] < 3:
        print(
            "Execute o script da seguinte maneira"
            " python3 <nome_script>.py"
        )
        print("Você executou a versão:" + platform.python_version())
        sys.exit()

    print(" - CHAMANDO A FUNCAO DECOARADA - ")
    funcao_loop()    

    print("Observe que a função foi alterada pelo Decorator!")