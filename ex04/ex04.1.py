# -*- coding: utf-8 -*-
"""  
    Description: 
    O objetivo aqui é mostrar como DEFINIR AS DICAS DE TIPOS (TYPING HINTS)
    E também como FAZER ANOTAÇÕES em MÉTODOS (FUNÇÕES)


    - O Tipos que podemos definir são: ITERATORS, LIST, DICT
    - Vamos aprender a definir se uma função receberá uma str ou None
    - Vamos aprender a comentar os atributos da função
   

    Author:        @palin
    Last Update:   20/01/2018
    Created:       20/01/2018
    Copyright:     (c) MIT
    Version:       1.0
"""

import sys, os, platform

try:

    from typing import Dict, List, Iterator, Union

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

# Exemplo 2: Union
# é usado para indicar que um tipo pode ser um dos vários tipos
# Neste caso pode receber um inteiro ou um float, e não retorna nada.
def print_number(value: Union[int, float]) -> None:  
    print(value + 1)


def print_list(names: List[str]) -> None:
    print( 'Olá, {}'.format(', '.join(names)) )

# Recebe uma lista de Numeros e converte em uma lista
# de strings
def stringify_list(numbers: List[int]) -> List[str]:
    return [str(number) for number in numbers]

# Recebe uma lista de Dicionarios key: int e value: str
def print_dic_data(attrs: Dict[str, int]) -> None:
    for key, value in attrs.items():
        print('{0}: {1}'.format(key, value))



def greeting(names: Union[List[str], Dict[int, List[str]]]) -> Union[
        List[str], Dict[int, List[str]]]:
    fmt = 'Hello, {}'
    if isinstance(names, dict):
        return [(k, fmt.format(', '.join(v))) for k, v in
                names.items()]
    else:
        return fmt.format(', '.join(names))




if __name__ == '__main__':
    
    if sys.version_info[0] < 3:
        print(
            "Execute o script da seguinte maneira"
            " python3 <nome_script>.py"
        )
        print("Você executou a versão:" + platform.python_version())
        sys.exit()
    

    #Esta função pode receber um inteiro ou float - Union
    print_number(156)
    print_number(14.343)

    #Esta função pode receber uma Lista de Strings
    # e retorna uma string
    print_list(['jane', 'john', 'judy'])


    # Outras Declarações de Tipo
    # A dictionary where the keys are strings and the values are ints
    # ATENÇÃO: as variáveis NÃO PODEM SER ANOTADAS - o que fazemos é
    # colocar um comentário na frente do tipo:
    name_counts = {"Adam": 10,"Guido": 12}  # type: Dict[str, int] 

    print('-'*50)
    print_dic_data(name_counts)
    print('-'*50)

    # A list of integers
    numbers = [1, 2, 3, 4, 5, 6] # type: List[int]

    # A list that holds dicts that each hold a string key / int value
    list_of_dicts = [
        {"key1": 1},
        {"key2": 2}
    ] # type: List[Dict[str, int]]

    print('-'*50)
    print(greeting(['jane', 'john', 'judy']))
    print(greeting(
        {10: ['jane', 'judy'],
        11: ['john'],
        12: ['judy', 'john']
        }
    ))
    
    