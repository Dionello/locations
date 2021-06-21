# Criação da classe Locations, que representa a árvore de hierarquia dos locais
# como uma lista de adjacências. A chave do dicionário é o nome do local, e seu
# valor é uma lista representando quais locais que têm relação de primeiro grau
# com o local chave. Caso o seu valor seja uma lista vazia, o local é um nó folha.

class Locations:
    def __init__(self, localName):
        self.names = dict()
        self.names[localName] = []
    # Adiciona um local filho
    def addLocal(self, localName, fatherName):
        self.names[fatherName].append(localName)
        self.names[localName] = []
    # Retorna a quantidade de locais hiraquicamente abaixo de um local
    def localSize(self, localName):
        children = self.names[localName]
        s = 0
        if children != []:
            for l in children:
                s += 1 + self.localSize(l)
        return s
    # Retorna um dicionário contando o nome do local como chave, e quantidade de
    # locais dependentes como valor
    def dependencies(self):
        dep = dict()
        for local in sorted(self.names):
            dep[local] = self.localSize(local)
        return dep
