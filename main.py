__all__ = ["IdentificarExtensao", "criar_arquivo", "criar_multiplos_arquivos", 
"deletar_arquivo", "deletar_multiplos", "renomear_arquivo", "renomear_multiplos",
"ler_arquivo", "ler_arquivos", "copiar", "copiar_arquivos", "acresentar_arquivo"]


from shutil import copy
from os import rename, remove
from utils import *


def criar_arquivo(nome):
	"""
cria um arquivo usando o parâmetro nome
	"""
	limpar_terminal()
	try:
		if path.exists(nome) == True:
			print("o arquivo já existe")
		else:
			with open(nome, "w") as arquivo:
				print(f"{nome} criado com sucesso")
	except Exception as error:
		print(error)


def criar_multiplos_arquivos(nome, extensao,  quantidade):
	"""
cria determinado número de arquivos usando uma combinação de nome + extensão
	"""
	limpar_terminal()
	contador = 1
	while contador <= quantidade:
		nome_arquivo = nome + str(contador) + extensao
		with open(nome_arquivo, "w") as arquivo:
			contador += 1


def deletar_arquivo(nome_arquivo):
	"""
verifica se um arquivo existe, se existir apaga ele
	"""
	try:
		limpar_terminal()
		if existOrNot(nome_arquivo) == True:
			remove(nome_arquivo)
	except FileNotFoundError as error:
		print(f" o arquivo: {error} não existe")


def deletar_multiplos(extensao):
	"""
deleta multiplos arquivos com uma mesma extensão
	"""
	try:
		limpar_terminal()
		system(f"rm *{extensao}")
	except Exception as error:
		print(error)


def renomear_arquivo(antigo_nome, novo_nome):
	"""
verifica se um arquivo existe, se sim renomeia ele
	"""
	try:
		limpar_terminal()
		if existOrNot(antigo_nome):
			rename(antigo_nome, novo_nome)
			exibir_diretório()
	except FileNotFoundError as error:
		print(f' o arquivo: {error} não existe')


def renomear_multiplos(nomes, novos_nomes):
	"""
percorre a lista de nomes, verificando se cada arquivo existe, se sim renomeia ele
usando um item de index correpondente da lista de novos nomes
	"""
	limpar_terminal()
	contador = 0
	novos_nomes = list(novos_nomes)
	try:
		for x in nomes:
			if existOrNot(x):
				rename(x, novos_nomes[contador])
				contador += 1
	except PermissionError as error:
		print("não a permissão para fazer modificação/ões")
	except FileNotFoundError as error:
		print(f"o arquivo: {error} não existe")
	

def ler_arquivo(nome):
	"""
verifica se um arquivo existe, se existe exibe o conteúdo na tela
	"""
	try:
		limpar_terminal()
		if name == "nt":
			"""
			resolver isso dps
			"""
			print("é windows mané")
		else:
			if existOrNot(nome):
				system("cat " + nome)
	except Exception as error:
		"""
		atualizar dps pra ler apenas texto simples
		"""
		print(error)


def ler_arquivos(arquivos):
	"""
percorre uma lista de arquivos, verifica se o item atual existe
exibe o conteúdo na tela
	"""
	try:
		limpar_terminal()
		if name == "nt":
			print("é windows mané")
		else:
			for x in arquivos:
				"""
				mema coisa da ler arquivos
				"""
				if existOrNot(x):
					system("cat " + x)
	except Exception as error:
		print(error)


def copiar(arquivo, arquivo_copia):
	try:
		if existOrNot(arquivo):
			copy(arquivo, arquivo_copia)
			print(f"arquivo: {arquivo} copiado com sucesso")
	except Exception as error:
		print(f"erro encontrado: {error}")


def copiar_arquivos(arquivos, cópias):
	for x in [arquivos, cópias]:
		a = list_verify(x)
		if a ==  True:
			limpar_terminal()
			contador = 0
			try:
				for x in arquivos:
					if existOrNot(x):
						copy(x, cópias[contador])
						contador += 1
			except Exception as error:
				print(error)
		else:
			print("perdeu, perdeu fudeu")


def acresentar_arquivo(arquivo, conteudo):
	try:
		if existOrNot(arquivo):
			with open(arquivo, "a") as sasa:
				conteudo = "\n" + conteudo
				sasa.write(conteudo)
	except Exception as error:
		print(f"erro encontrado: {error}")