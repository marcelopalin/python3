# -*- coding: utf-8 -*-
"""  
    Description: Existe um erro na passagem de Tipos para a função
    get_first_name

    O Objetivo aqui é que você isntale o pacote **mypy**
    sudo python3 -m pip install mypy

    Depois execute o comando:

    mypy ex04.py onde será indicado onde está o erro do código.

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
    from typing import Dict, Iterator, List
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


def get_first_name(full_name: str) -> str:
    return full_name.split(" ")[0]

if __name__ == '__main__':
    
    if sys.version_info[0] < 3:
        print(
            "Execute o script da seguinte maneira"
            " python3 <nome_script>.py"
        )
        print("Você executou a versão:" + platform.python_version())
        sys.exit()

    
    nome_ficticio: Dict[str, str] = {
        "first_name": "UserFirstName",
        "last_name": "UserLastName"
    }

    raw_name: str = input("Please enter your name: ")
    # Espera receber uma string
    first_name: str = get_first_name(raw_name)

    # Se o usuario não digitar nada será utilizado o 
    # nome_ficticio que é um Dicionário com duas Strings.
    # Porem, ao utilizarmos o MyPy ele deverá acusar um erro
    # pois estamos passando um Tipo Errado para o Método get_first_name
    if not first_name:
        first_name = get_first_name(nome_ficticio)

    print(f"Olá, {first_name}!")