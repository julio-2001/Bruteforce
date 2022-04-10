import random as rn
import string as sg

#analise de dados
import pandas as pd

#scanner de rede
import nmap as n

#automação
import pyautogui as py
import time as t

# deep learning
import keras as ks

char =  ''
chars_lista = list(char)


senha = py.password("Digite a senha;   ")
limite = py.write("Digite o limite:  ")
senha_a = ''


while True:
    cont = 0
    for c in chars_lista:
        t.sleep(0.001)
        for c1 in chars_lista:
            t.sleep(0.001)
            for c2 in chars_lista:
                cont += 1
                
                if len(senha) > 3:
                    y = c + c1 + c2.split
                    if y == senha:
                        print(f" senha encontrada ==>> 0 \33[1;32m {y} \033[m ")
                        file_senha = ''
                        senha_encontrada = open(file_senha , 'w')
                        exit()
                        break
                    
                    else:
                        print(f"<<<=== \033[1;31m  [ {y} ] ===>>> \033[m ")
                        file_senha = ''
                        senha_nao_aceita = open(file_senha , 'w')
                        if cont >= limite:
                            exit(f" limite {limite} atingido ")
                            break
                        


