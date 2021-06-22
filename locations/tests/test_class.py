import sys, pytest
sys.path.insert(0, '../Class')
from Locations import Locations

@pytest.fixture
def local_pai():
    return Locations('ABC')

@pytest.fixture
def locais_config1():
    loc = Locations('ABC')
    loc.addLocal('BCD','ABC')
    loc.addLocal('CDE','ABC')
    return loc

@pytest.fixture
def locais_config2():
    loc = Locations('ABC')
    loc.addLocal('BCD','ABC')
    loc.addLocal('CDE','BCD')
    return loc

def test_inicializacao_classe(local_pai):
    assert local_pai.names == {'ABC':[]}

def test_erro_classe_sem_nome():
    with pytest.raises(TypeError):
        Locations()

def test_adiciona_local(local_pai):
    local_pai.addLocal('BCD', 'ABC')
    assert local_pai.names == {'ABC':['BCD'], 'BCD':[]}

def test_adiciona_local_sem_pai_existente(local_pai):
    with pytest.raises(KeyError):
        local_pai.addLocal('BCD', 'XYZ')

def test_tamanho_com_local_nao_existente(local_pai):
    with pytest.raises(KeyError):
        local_pai.localSize('XYZ')

def test_tamanho0(local_pai):
    assert local_pai.localSize('ABC') == 0

def test_tamanho1(locais_config1):
    assert locais_config1.localSize('ABC') == 2
    assert locais_config1.localSize('BCD') == 0
    assert locais_config1.localSize('CDE') == 0

def test_tamanho2(locais_config2):
    assert locais_config2.localSize('ABC') == 2
    assert locais_config2.localSize('BCD') == 1
    assert locais_config2.localSize('CDE') == 0

def test_dependencias0(local_pai):
    assert local_pai.dependencies() == {'ABC':0}

def test_dependencias1(locais_config1):
    assert locais_config1.dependencies() == {'ABC': 2 ,'BCD': 0 ,'CDE': 0}

def test_dependencias2(locais_config2):
    assert locais_config2.dependencies() == {'ABC': 2 ,'BCD': 1 ,'CDE': 0}
