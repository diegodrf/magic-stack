# -*- coding: utf-8 -*-
import requests
from sys import argv

# script de comunicação universal para o magic_stack.

# Recebe os argumentos independente do tamanho e monta um dicionário chave:valor.
j = {}
for i in range(1, len(argv)):
    j[str(i)] = argv[i]

# Envia um post para a URL informada no primero campo (Este item é obrigatório) e adiciona o json no corpo.
res = requests.post(j['1'], data=j)
res.raise_for_status()
print(res.json())
