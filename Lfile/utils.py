from pathlib import Path
from os import system, name
from json import load
from colorama import Fore

error_mensage = "infelizmente o arquivo passado não é um json"


def IdentificarExtensao(name):
    """
usa a biblioteca pathlib para verificar qual a extensâo do arquivo, 
e depois retorna a extensão
    """
    file_path = Path(name)
    extension = file_path.suffix
    if extension == ".json":
        return extension
    else:
        print(error_mensage)
        return


def list_convert(value):
    if type(value) == list:
        sasa = ", ".join(value)
        return sasa
    else:
        return value


def limpar_terminal():
    match name:
        case "nt": system("cls")
        case _: system("clear")


def abrir_arquivo(caminho):
    with open(caminho, "r") as arquivo:
        json = load(arquivo)
    return json

def sasa(caminho):
    limpar_terminal()
    IdentificarExtensao(caminho)
    json = abrir_arquivo(caminho)
    return json


def exibir_auxiliar(value):
    """
função auxiliar para formatar a exibição dos valores de um json que contem mais de um objeto
    """
    for x in value:
        print(f"{Fore.YELLOW + x + Fore.RESET}: {list_convert(value[x])}")
    print(" ")
