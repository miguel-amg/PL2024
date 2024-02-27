""" Name: Miguel Guimarães
    University: Universidade do Minho
    Processamento de Linguagens 2024 / Language processing 2024 """ 

# Imports
import re
import sys

# Expressão para detetar as flags
exp = r"(?i)on|off|\d+|="

# Váriveis temporarias
soma = 0 # Resultado final
ativado = False # Diz o estado do on-off

# Iterar cada linha do texto
for line in sys.stdin:
    array = re.findall(exp, line)
    
    for elem in array:
        if(elem.lower() == 'off'): # Detetar o off
            ativado = False
        if(elem.lower() == 'on'): # Detetar o on
            ativado = True
        if(elem[0].isdigit()): # Detetar numeros
            if(ativado == True):
                soma += int(elem)
        if(elem == '='): # Detetar igual
            print("Soma:" + str(soma))
