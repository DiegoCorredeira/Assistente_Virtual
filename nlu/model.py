import yaml
import numpy as np

data = yaml.safe_load(open('train.yml', 'r', encoding='utf-8').read())

input = []
output = []

for comando in data['commands']:
    input.append(comando['input'])
    output.append('{}\{}'.format(comando['entidade'], comando['acao']))

caracteres = set()

for char in input + output:
    for char in input:
        if char not in caracteres:
            caracteres.add(char)

chartoindex = {}
indextochar = {}

for i, char in enumerate(caracteres):
    chartoindex[char] = i
    indextochar[i] = char
print(len(caracteres))

sequencia = max([len(x) for x in input])
print(sequencia)





# print(input)
# print(output)
