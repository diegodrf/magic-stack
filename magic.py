import requests
from sys import argv
import json

# script de comunicação universal para o magic_stack.

# Recebe os argumentos independente do tamanho e monta um dicionário chave:valor.
j = '{'
for i in range(1, len(argv)):
    if i < len(argv) - 1:
        # Se argumento não for o último, adiciona vírgula no final.
        j += '"{}":"{}",'.format(i, argv[i])
    else:
        # Se for o último argumento, não adiciona a vírgula.
        j += '"{}":"{}"'.format(i, argv[i])
j += '}'

j = json.loads(j)

# Envia um post para a URL informada no primero campo (Este item é obrigatório) e adiciona o json no corpo.
res = requests.post(j['1'], data=j)
res.raise_for_status()
print(res.json())
