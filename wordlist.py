

#funções
import time as t
from itertools import product

#redes
import socket as sk
import socketserver as sks
import requests as rts
import urllib3 as url 
import websocket as ws
import w3lib as wb

#automação
import pyautogui as py

#analise de dados
import pandas as p

#deep learning
import keras as ks

enreco_ip = sk.gethostname
endereco_ip = sk.gethostname



""""
                    -world  list-
            
"""

scale = input(" \033[32m[*]  Digite o tamanho da scala [EX 1 ate 8= [1:8]:  ")

print(" \033[1;33;44m Para parar o processo digite [CTRL + C]! \033[m ")
t.sleep(2)

comeco = int(scale.split(':')[0])
fim = int(scale.split(':')[1])

t.sleep(0.5)


info_pessoais = str(input("\n \033[32m[*] Deseja colocar informações pessoais? [s ou n]  :  "))
if info_pessoais == 's':
    primeiro_nome = str(input("\n \033[36m[*]Primeiro nome:  "))
    sobrenome = str(input("\n \033[36m[*] Sobrenome:  "))
    aniversario = str(input("\n \033[36m[*] Data do aniversario:   "))
    mes = str(input("\n \033[36m[*] Digite o mês:   "))
    ano = str(input("\n \033[36m[*]Digite o ano:  "))
    chars = primeiro_nome + sobrenome + aniversario + mes + ano



else:
    chars = 'abcdefghijklmnopqrstuvwxyz'
    pass


chars_maiosculo = chars.upper()
chars_numero = '0123456789'
chars_especiais = '!\][/?.,~-="; :><@#$%&*()_+ \ ' 

t.sleep(0.5)

arquivo_nome = input("\n \033[36m[!] Digite o nome para seu arquivo de lista de palavras!:   ")
arquivo = open(arquivo_nome, 'w')

if input("\n Apenas numeros? [s ou n]:  ") == 's':
    chars = chars_numero
else:
    if input("\n \033[36m[?] Deseja usar caracteres maiosculos? [s ou n]:   ") == 's':
        chars = '' .join([chars , chars_maiosculo])

    if input("\n \033[36m[?] Deseja usar caracteres especiais? [s ou n ]:   ") == 's':
        chars = '' .join([chars, chars_especiais ])

    if input("\n \033[36m[?] Deseja usar numeros? [s ou n ]:   ") == 's':
        chars = ''.join([chars ,chars_numero ])


try:
    for i in range(comeco , fim +1):

        cont = 0
        

        for j in product(chars, repeat=i):
            tempo = t.strftime("%H:%M:%S")


            temp = '' .join(j)
            print(f" \033[36m <<<==========   \033[32m[  {temp}  ]\033[m  \033[36m ==========>>> \033[m  \033[30;43;1m {cont} \033[m   \033[34;42;1m {tempo} \033[m  ")
            arquivo.write(temp + ' \n')
            cont += 1
            

except(KeyboardInterrupt):
    print(" \033[31m Usuario interrompeu o processo \033[m ") 
    print(f"Senhas registradas \033[1;32m {cont} \033[m  tempo termino \033[1;36m {tempo} \033[m  ")
    arquivo.close()
  
