# Ljson

a Lson é uma biblioteca local feita por mim para facilitar a manipulação de arquivos json, ela é feita principalmente encima da própria biblioteca json do feito, que fornece funções "básicas" para manipular json, como:
- conversão de objeto json em dicionário python
- conversão de string em objeto json
por isso a Lson tem como objetivo funcionalidades mais diretas envolvendo json, como `exibir_json()` que abre um arquivo json lê seu conteúdo, e por fim exibe na tela o as chaves e valores json de maneira formatada.

## funções

### exibir json
função que exibe as chaves:valor de um objeto json de maneira formatada, por hora apenas funciona com arquivos json que contém apenas um objeto, caso sejam vários exibe os dicionários sem formatação.
```python
#saída padrão
sese: {"name": "nathan", "idade": "19"}

#saida formatada
name: nathan
idade: 19
```

```python
from Ljson import *

exibir_json("sukuna.json")
```


### exibir json lista 
variação da função exibir json, feita para funcionar com arquivos json com mais de um objeto seguindo o modo lista de objetos, percorre todos os objetos e exibe cada um deles.


```python
from Ljson import *

exibir_json("sukuna.json")
```
### exibir json cv
variação da função exibir json, feita para funcionar com arquivos json com mais de um objeto seguindo o modo objetos chave única, percorre todos os objetos e exibe cada um deles.


```python
from Ljson import *

exibir_json("sukuna.json")
```

### gravar json
percorre o objeto json e escreve as chaves:valor em um arquivo txt.

```json
{
    "name": "lvdstr",
    "age": 30,
    "height": 1.90,
    "weight": 88.60,
    "city": "New York",
    "languages": [
        "python",
        "javascript",
        "php",
        "c",
        "java",
        "c++",
        "c#",
        "kotlin"
    ],
    "library": [
        "random",
        "time",
        "json",
        "os",
        "colorama",
        "tinydb",
        "pathlib",
        "datetime",
        "abs",
        "rich",
        "openpyxl"
    ]
}
```


```txt
aparencia do txt

Name: lvdstr
Age: 30
Height: 1.9
Weight: 88.6
City: New York
Languages: python, javascript, php, c, java, c++, c#, kotlin
Library: random, time, json, os, colorama, tinydb, pathlib, datetime, abs, rich, openpyxl
```


```python
from Ljson import *

gravar_json("sukuna.json", "a.txt")
```
### converter json
converter_json
obtém o objeto json, converte em um dicionário python e retorna ele
parãmetros: caminho do arquivo json


```python
from Ljson import *

converter_json("sukuna.json")
```
