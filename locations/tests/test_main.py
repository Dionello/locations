import sys, pytest, os
sys.path.insert(0, '../')
from main import *

def test_processDependencies():
    dep = {'ABC': 4, 'BCD': 6, 'DFG': 1, 'DXZ': 0, 'HIJ': 0, 'KLM': 0, 'NOP': 0}
    assert processDependencies('short_input.in') == dep

def test_print_dependencies0():
    short_input_processed = processDependencies('short_input.in')
    short_input_processed = printDependecies(short_input_processed)
    short_input_out = open('short_input.out').read()
    assert short_input_processed == short_input_out

############ testes dos 100 arquivos #############

def importFile(path):
    file = open(path)
    file = file.read()
    return file

testfiles = os.listdir('tests_files')

infile = []
outfile = []

prefix = 'tests_files/'

for file in testfiles:
    if file.endswith('.in'):
        infile.append(prefix + file)
    else:
        outfile.append(prefix + file)

in_out_files = list(zip(infile,outfile))

@pytest.mark.parametrize("input, output", in_out_files)
def test_funcionamento_algoritmo(input, output):
    result = processDependencies(input)
    result = printDependecies(result)
    output = importFile(output)
    assert result == output
