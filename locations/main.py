import sys
from Class.location import Locations

# abre um arquivo com os valores de entrada, processa e cria o dicionario de
# dependencias
def processDependencies(path):
    with open(path) as file:
        root = file.readline().rstrip('\n')
        locations = Locations(root)

        for line in file.readlines():
            localName, father = line.rstrip('\n').split(' ')
            locations.addLocal(localName, father)
            file.close()

    dependecies = locations.dependencies()
    return dependecies

# Cria um texto a partir de um dicionario de dependencias
def printDependecies(dependecies):
    text = []
    for local in dependecies:
        text.append(local + ' ' + str(dependecies[local]))
    text = '\n'.join(text)
    return text

def main(args):
    dep = processDependencies(args[0])
    # Imprime o texto no terminal
    text = printDependecies(dep)
    print(text)

if __name__ =='__main__':
    main(sys.argv[1:])
