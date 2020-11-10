def jogar():
    import random
    import mensagens

    mensagens.mensagem_inicial('Adivinhação')

    total_tentativas = nivel_jogo()

    numero_secreto = random.randrange(1, 101)
    print(numero_secreto)
    pontos = 1000

    for rodada in range(1, total_tentativas + 1):
        #Conta e exibe o número de tentativas
        print("Tentativa {} de {}".format(rodada, total_tentativas))

        #Valida o chute do jogador
        chute = valida_chute()

        #Se o chute for válido, retornará um int, senão retorna um boolean
        if type(chute) == int:
            acertou = chute == numero_secreto
            maior_que = chute > numero_secreto
            menor_que = chute < numero_secreto

            if acertou:
                print("Você acertou e fez {} pontos!".format(pontos))
                mensagens.imprime_mensagem_vencedor()
                break
            else:
                if maior_que:
                    print("Você errou! seu chute foi maior que o número secreto.")
                elif menor_que:
                    print("Você errou! seu chute foi menor que o número secreto.")

            pontos = calcula_pontos(numero_secreto, chute, pontos)

        else:
            continue
        print('Você fez {} pontos'.format(pontos))

    if not acertou:
        mensagens.imprime_mensagem_perdedor(numero_secreto)


def valida_chute():
    chute = input("Digite o seu número: ")

    dig = 0
    while dig == 0:
        if chute.isdigit():
            print("Você digitou o número:", chute)
            chute = int(chute)
            status = False
            if chute < 1:
                print("O número deve ser maior que 0")
            elif chute > 100:
                print('Escolha um número entre 1 e 100')
            else:
                status = chute

            dig = 1
        else:
            print("Não é um número")
            chute = input("Digite um número: ")

    return status

def calcula_pontos(num_secreto, chute, pontos):
    pontos_perdidos = abs(num_secreto - chute)
    pontos = pontos - pontos_perdidos
    return pontos

def nivel_jogo():
    print('Qual o nível de dificuldade?')
    print('[1] fácil [2] médio [3] Difícil')

    nivel = int(input('Defina o nível: '))
    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5
    return total_tentativas

if __name__ == '__main__':
    jogar()
