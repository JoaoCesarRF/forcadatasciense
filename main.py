#-*- coding: utf-8 -*-
import random
import unidecode


def pegar_palavra():
    with open('palavras.txt', 'rt', encoding='utf-8') as palavras:
        arq = (palavras.readlines())
        banco =[cada.rstrip('\n') for cada in arq]
        return banco[random.randint(0,len(banco)-1)]
banco=['''
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

if __name__ == '__main__':
    original = pegar_palavra()
    pal = unidecode.unidecode(original)
    palavra=[letra.upper() for letra in pal]
    #print("".join(palavra).center(15))
    qnts_letras=len(palavra)
    letras_ja_inseridas = []
    linha = ['_' for n in range(qnts_letras)]
    acertos=0
    erros=0
    while True:
        print(banco[erros])
        print(f'{"".join(linha)}\n {qnts_letras:^} letras')
        print('Letras ja inseridas \n'," ".join(letras_ja_inseridas))
        letra = input('Digite uma letra').upper()
        while True:
            if letra in letras_ja_inseridas:
                print('letra repitida')
                letra = input('Digite uma letra diferente').upper()
                continue
            else:
                break
        letras_ja_inseridas.append(letra)
        for i in range(qnts_letras):
            if palavra[i] == letra:
                linha[i]=letra
        if letra in palavra:
            acertos += 1
        else:
            erros += 1

        print(erros)
        if acertos == qnts_letras:
            print(f'\nPARABENS !!!!\na palavra e "{original}"')
            break
        elif erros == 6:
            print(f'MMMOOOORRRRRRREEEEEEEEEEUUUUUU \n {banco[erros]}')
            break




