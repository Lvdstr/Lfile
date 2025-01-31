__name__ = "moduloLocal_json"
__all__ = ["exibir_json", "gravar_json", "converter_json", "exibir_json_lista", "exibir_json_cv"]


from utils import *

    
def exibir_json(caminho):
    """
exibe o conteudo de um arquivo json que contem apenas um objeto
    """
    json = sasa(caminho)

    for x in json:
        chave = x.capitalize()
        valor = list_convert(json[x])
        dados = f"{Fore.YELLOW + chave + Fore.RESET}: {valor}"
        print(dados)


def gravar_json(caminho, novo_arquivo, tipo=None):
    """
escreve o conteudo de um objeto json em um arquivo txt
    """
    json = sasa(caminho)

    try:
        novo = open(novo_arquivo, "w")
        for x in json:
            chave = x.capitalize()
            valor = list_convert(json[x])
            dados = f"{chave}: {valor}"
            novo.write(dados + "\n")
        novo.close()
        print("arquivo criado com sucesso")
    except:
        print("erro na criação do arquivo")


def converter_json(caminho):
    """
transforma todas as chaves e valores de um objeto json em um dicionário python
    """
    json = sasa(caminho)
    dados = dict(json)
    return dados


def exibir_json_lista(caminho):
    """
exibe o conteudo de um arquivo json que segue o estilo lista de objetos
    """
    lista = []
    json = sasa(caminho)
    for x in json:
        lista.append(x)
    for x in lista:
        exibir_auxiliar(x)


def exibir_json_cv(caminho):
    """
exibe o conteudo de um arquivo json que segue o estilo chave única
    """
    lista = []
    json = sasa(caminho)
    a = json.keys()
    for x in json:
        item = json[x]
        lista.append(item)
    for x in lista:
        exibir_auxiliar(x)
