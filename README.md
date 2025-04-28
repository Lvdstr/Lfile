## lfile

biblioteca com propósito de fornecer pequenas funções relacionadas a manipulação de arquivos, como criar, deletar e renomear

## funções
### criar arquivo
função para criar um arquivo, caso o arquivo venha com uma extensão especifica, cria o arquivo daquela extensão, caso contrário cria um arquivo padrão e comum de txt

```python
criar_arquivo("a.txt")
```
### criar arquivos
função para criar múltiplos arquivos, usando 3 parâmetros: 
- nome
- extensão
- quantidade
o nome e a extensão é o mesmo para todos os arquivos, a quantidade é sobre quantos arquivos serão criados assim como numerar cada arquivo para diferenciá-los.
```python
criar_multiplos_arquivo("a", ".txt", 10)
```

```txt
a1.txt
a2.txt
a3.txt
a4.txt
a5.txt
...
```

### deletar arquivo
verifica se o arquivo passado como parâmetro existe, caso sim apaga ele, caso  contrário exibe uma mensagem de erro

```python
deletar_arquivo("a.txt")
```

### deletar arquivos
deleta diversos arquivos de uma extensão

```python
deletar_multiplos(".py")
```

###  renomear arquivo
verifica se um arquivo existe, caso sim renomeia ele

sintaxe
```python
renomear_arquivo("a.txt")
```


### renomear arquivos
recebe duas listas, uma com nomes antigos de arquivos, e outra com nomes novos, percorre a lista de arquivos antigos, verificando se o arquivo atual existe, caso exista substitui o nome antigo do arquivo pelo nome da nova lista de nomes usando o index do item antigo.

sintaxe
```python
renomear_multiplos(["a.txt", "b.txt"], ["c.txt", "d.txt"])
```


```txt
lista antiga
[1,2,3,4,5,6,7,8,9]

lista nova
[11,22,33,44,55,66,77,88,99]

item atual da lista antiga: 5
index do item: 4

index correpondente da nova lista: 55
```

### ler arquivo
verifica se o arquivo existe, caso sim exibe seu conteúdo na tela

sintaxe
```python
ler_arquivo("a.txt")
```

### ler arquivos
verifica se um arquivo existe, caso sim  ,caso contrário 

sintaxe
```python
ler_arquivos(["a.txt", "b.txt"])
```


### copiar arquivo
verifica se um arquivo existe, caso sim  ,caso contrário 

sintaxe
```python
copiar_arquivo("a.txt", "acópia.txt")
```

### copiar_arquivos
verifica se um arquivo existe, caso sim  ,caso contrário 


### acresentar arquivos
verifica se um arquivo existe, caso sim  ,caso contrário 

```python
acresentar_arquivo("b.py", "texto")
```
