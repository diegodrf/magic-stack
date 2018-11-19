import requests
from sys import argv
import json


j = '{'
for i in range(1, len(argv)):
    if i < len(argv) - 1:
        j += '"{}":"{}",'.format(i, argv[i])
    else:
        j += '"{}":"{}"'.format(i, argv[i])
j += '}'

j = json.loads(j)

res = requests.post(j['1'], data=j)
res.raise_for_status()
print(res.json())
