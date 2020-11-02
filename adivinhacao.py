def jogar():
    import random

    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")
    print()
    print('Qual o nível de dificuldade?')
    print('[1] fácil [2] médio [3] Difícl')

    nivel = int(input('Defina o nível: '))
    numero_secreto = random.randrange(1, 101)
    pontos = 1000
    pontos_perdidos = 0

    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute = int(input("Digite o seu número: "))
        print("Você digitou o número:", chute)

        if chute < 1 or chute > 100:
            print("O número deve estar entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior_que = chute > numero_secreto
        menor_que = chute < numero_secreto

        if acertou:
            print("Você acertou e fez {} pontos!".format(pontos))
            print("Você acertou!")
            break
        else:
            if maior_que:
                print("Você errou! seu chute foi maior que o número secreto.")
                pontos = pontos - pontos_perdidos
            elif menor_que:
                print("Você errou! seu chute foi menor que o número secreto.")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

        # rodada = rodada + 1

    print("Fim do jogo.")

    random.random()


if __name__ == '__main__':
    jogar()
