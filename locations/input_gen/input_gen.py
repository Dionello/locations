from string import ascii_uppercase
from itertools import combinations
from random import choice
import sys, os, shutil

# Cria uma lista com todos os nomes possiveis
alphabet = list(ascii_uppercase)
location_names = list(combinations(alphabet,3))
location_names = list(map(''.join,location_names))

# Gera exemplos aleatórios de entrada para o programa
def gen_exemple(size: int, locations):
    text = ''
    # loc_included guarda os nomes já incluídos no arquivo como candidatos para
    # os próximos locais pai
    loc_included = []

    father = choice(locations)

    text += father + '\n'
    loc_included.append(father)

    for i in range(size):
        new_location = choice(locations)
        father = choice(loc_included)
        loc_included.append(new_location)
        text += new_location + ' ' +  father + '\n'

    return text

# Deleta arquivos da pasta de inputs
def deleteFiles(folder):
    for file in os.listdir(folder):
        filepath = os.path.join(folder, file)
        os.unlink(filepath)

# Cria arquivos de inputs com valores aleatórios, limpando os arquivos anteriores
def main(args):
    folder = 'inputs'
    size = int(args[0])
    if len(args) == 1:
        quantity = 1
    else:
        quantity = int(args[1])
    deleteFiles(folder)
    for i in range(1, quantity+1):
        path = f'{folder}/{i}.in'
        f = open(path, 'w')
        f.write(gen_exemple(size, location_names))
        f.close()

if __name__ =='__main__':
    main(sys.argv[1:])
