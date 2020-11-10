'''
Arquivo de mensagens para jogos do pacote de jogos em python.
Mensagens específica serão identificadas com um sufixo no fim do nome da função.
'''

''' 
Mensagem inicial para os todos os jogos.
Recebe variável tipo string para concatenar na mensagem, identificando o jogo    
'''
def mensagem_inicial(jogo):
    print("*********************************")
    print("Bem vindo ao jogo de {}!".format(jogo))
    print("*********************************")


# Mensagem de sucesso
def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


''' 
Mensagem de insucesso. 
Recebe variável tipo para concatenar na mensagem. Caso seja uma
string, exiber mensagem do jogo forca, senão mensagem do jogo de
adivinhação de números.
'''
def imprime_mensagem_perdedor(var):
    if type(var) == str:
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(var))
    elif type(var) == int:
        print("O número era {}".format(var))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


# De acordo com o número de erros, imprime uma porçao do boneco na forca.
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
        print(" |            ")
        print("_|___         ")
        print()


# Mensagem de fim de jogo
def fim():
    print('Fim de jogo')
