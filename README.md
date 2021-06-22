# Organização de localizações por hierarquia

---

Este projeto desenvolve um algoritmo desenvolvido em python para solução do problema 'locations', descrito em detalhes PDF na pasta ./docs/locations (en).pdf, proposto pela empresa HVAR Consulting para o processo seletivo.

## Pré-requisitos

* Interpretador python pré-instalado na máquina local;
* Biblioteca pyteste pré-instalada através do pip.

## Guia de utilização

### Programa principal
Após baixar o repositório, executar o terminal na pasta 'locations', e executar o arquivo 'main.py' seguido do endereço do arquivo que se encontra o input para função. Por exemplo:
```
> python main.py input_gen/inputs/1.in
```

### Geração de inputs
A pasta 'locations/input_gen' contém o programa input_gen.py, que gera arquivos de inputs aleatórios para o problema.  
Para utilizar, basta executir o terminal na pasta, e executar o arquivo 'input_gen.py' seguido da quantidade de nós para o exemplo, e a quantidade de exemplos. O exemplo abaixo gera 5 arquivos com 10000 nós, por exemplo:

```
> python input_gen.py 10000 5
```

### Teste
A pasta 'locations/tests' possui os arquivos para teste do programa, implementados utilizando a biblioteca pytest. Basta executar o terminal e digitar 'pytest' para que rodar os testes e visualizar os resultados.  
Foram realizados testes para todos os métodos das classes, funções do main, e funcionamento do algorítimo para os 100 inputs propostos pela HVAR Consulting.
