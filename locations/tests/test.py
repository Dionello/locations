import main
import os

# Importa arquivo
def importFile(path):
    file = open(path)
    file = file.read()
    # Retira último caractere da entrada, para normalizar
    file = file[:-1]
    return file

# Compara o resultado obtido pelo arquivo de teste
def compareResult(inFile, outFile):
    return inFile == outFile

######
# importa o nome dos arquivos da pasta tests, separa entre entradas e saídas
testfiles = os.listdir('tests_files')

infile = []
outfile = []

prefix = 'tests_files/'

for file in testfiles:
    if file.endswith('.in'):
        infile.append(prefix + file)
    else:
        outfile.append(prefix + file)
#######
# Compara os resultados obtidos pelos arquivos de testes
for i in range(len(infile)):
    input = main.processDependencies(infile[i])
    input = main.printDependecies(input)
    output = importFile(outfile[i])
    print("Comparing %s result..." %infile[i])
    if compareResult(input, output):
        print("        Result %s OK" %outfile[i])
    else:
        print("**********Result %s failed**********" %outfile[i])
