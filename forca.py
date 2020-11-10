import random
import mensagens

'''
Jogo de Forca
Author: Israel Silva de Souza
Date: 20201102
Describe: Jogo para adivinhação de palavras através de chutes únicos de letras. São 7 
    tentativas até a montagem do boneco na forca. O número de letras, posições e 
    acertos são demonstrados a cada iteração. 
'''
def jogar():
    mensagens.mensagem_inicial('Forca')
    palavra_secreta = escolhe_palavra()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = solicita_chute()

        # Todas as comparações são feitas em caixa alta e sem espaços
        chute = chute.strip().upper()

        # Verifica erros e acertos
        if chute in palavra_secreta:
            verifica_chute(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            mensagens.desenha_forca(erros)

        # Registra flag de erros e acertos para saída do loop
        enforcou = erros == 7
        acertou = '_' not in letras_acertadas

        print(letras_acertadas)

    # Reporta o resultado do jogo
    if acertou:
        mensagens.imprime_mensagem_vencedor()
    else:
        mensagens.imprime_mensagem_perdedor(palavra_secreta)

    mensagens.fim()


# Escolhe uma palavras aleatoriamente, entre as opções existentes em arquivo.
def escolhe_palavra():
    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


# Inicializa os espaços com o número de letras a serem acertadas
def inicializa_letras_acertadas(palavra):
    return ['_' for dig in palavra]


# Verifica se a letra escolhida está na lista e em quais posições
def verifica_chute(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


# Interage com o jogador verificando o chute
def solicita_chute():
    print('jogando')
    chute = input('Digite uma letra: ')
    return chute


if __name__ == '__main__':
    jogar()
