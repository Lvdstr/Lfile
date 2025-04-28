from os import system, path, name
from pathlib import Path
from mimetypes import guess_type


def IdentificarExtensao(name):
	"""
usa a biblioteca pathlib para verificar qual a extensâo do arquivo, 
e depois retorna a extensão
	"""
	file_path = Path(name)
	extension = file_path.suffix
	return extension


def limpar_terminal():
	"""
verifica qual é o sistema operacional e dependendo de qual é usa o comando
correspondente para limpar a tela do terminal 
	"""
	match name:
		case "nt": system("cls")
		case _: system("clear")


def exibir_diretório():
	"""
verifica qual é o sistema operacional e dependendo de qual é usa o comando
correspondente para exibir todos os arquivos do diretório atual
	"""
	if name == "nt": system("dir")
	else: system("ls")


def list_verify(value):
	if type(value) == list: 
		print("sim")
	else:
		return False


def existOrNot(value):
	if path.exists(value):
		return True
	else:
		print("o arquivo não existe para que essa função seja executada nele")
		return


def is_binary_by_mime(filename):
    """
verifica se o arquivo é um binário ou texto simples
    """
    mime_type, _ = guess_type(filename)
    return mime_type is None or not mime_type.startswith("text/")