#-*- coding: utf-8 -*-
import random
import unidecode
# Programação Orientada a Objetos

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
	def __init__(self, word):

		
	# Método para adivinhar a letra
	def guess(self, letter):
		
		
	# Método para verificar se o jogo terminou
	def hangman_over(self):
		
		
	# Método para verificar se o jogador venceu
	def hangman_won(self):
		

	# Método para não mostrar a letra no board
	def hide_word(self):
		
		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
	with open('palavras.txt', 'rt', encoding='utf-8') as palavras:
		arq = (palavras.readlines())
		banco = [cada.rstrip('\n') for cada in arq]
		original= banco[random.randint(0,len(banco)-1)]
		pal = unidecode.unidecode(original)
		palavra=[letra.upper() for letra in pal]
		return palavra

# Função Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	

	# Verifica o status do jogo
	game.print_game_status()	

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.word)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()
