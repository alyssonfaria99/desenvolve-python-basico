import os
import sys

print(os.getcwd())
print(os.curdir)
print(os.listdir())

name = os.path.abspath('aupla.py')
print(name)

print(sys.version)
print(sys.path)

argumentos = sys.argv[1:]

if not argumentos:
    print('Informe o nome do arquivo.')
    sys.exit()

arquivo = argumentos[0]
if not os.path.isfile(arquivo):
    print('Arquivo não existe.')
print(argumentos)

##principais funcoes: open, write, read, close;


f = open('exemplo.txt','r+',encoding='utf-8')

with open('arquivo.txt') as f:
    ...
