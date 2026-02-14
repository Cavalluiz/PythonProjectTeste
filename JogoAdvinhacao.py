import random

def jogo_advinhacao():
    print('Bem-vindo ao jogo da advinhação!')
    print('Estou pensando em um número entre 1 e 100.')

    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    while not acertou:
        try:
            palpite = int(input('Digite seu palpite: '))
            tentativas += 1

            if palpite<numero_secreto:
                print('Muit baixo! Tente novamente.')
            elif palpite>numero_secreto:
                print('Muito alto! Tente novamente.')
            else:
                print(f'Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas')
                acertou = True

        except ValueError:
            print('Por favor, insira um número válido.')
jogo_advinhacao()