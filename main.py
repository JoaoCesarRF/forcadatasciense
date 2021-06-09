import random
import unidecode


def pegar_palavra():
    with open('palavras.txt', 'rt', encoding='utf-8') as palavras:
        arq = (palavras.readlines())
        banco =[cada.rstrip('\n') for cada in arq]
        return banco[random.randint(0,len(banco)-1)]

if __name__ == '__main__':
    original = pegar_palavra()
    pal = unidecode.unidecode(original)
    palavra=[letra.upper() for letra in pal]
    print("".join(palavra).center(15))
    qnts_letras=len(palavra)
    letras_ja_inseridas = []
    linha = ['_' for n in range(qnts_letras)]

    while True:
        print('\nJogo da Forca'.center(20))
        print("".join(palavra).center(15))
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




