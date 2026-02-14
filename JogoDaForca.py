import random

def jogar_forca():
    print('Bem-vindo ao jogo da forca!')
    palavras = ['Python', 'Programação', 'Desenvolvimento', 'Tecnologia', 'Algoritmo']
    palavra_secreta = random.choice(palavras).lower()
    letras_descobertas = ['_' for _ in palavra_secreta]
    tentativas = 9
    letras_erradas = []

    while tentativas > 0 and '_' in letras_descobertas:
        print('\nPalavra: ', ' '.join(letras_descobertas))
        print(f'Tentativas restantes: {tentativas}')
        print(f'Letras descobertas: {letras_descobertas}')
        print(f'Letras erradas: {', '.join(letras_erradas)}')

        letra = input('Digite uma letra: ').lower()

        if len(letra) !=1 or not letra.isalpha():
            print('Por favor, insira apenas uma letra válida.')
            continue

        if letra in letras_descobertas or letra in letras_erradas:
            print('Você já tentou essa letra. Tente outra.')
            continue

        if letra in palavra_secreta:
            for i, l in enumerate(palavra_secreta):
                if l == letra:
                    letras_descobertas[i] = letra
            print('Boa! Você acertou uma letra.')
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            print('Ops! Essa letra não está na palavra.')
    if '_' not in letras_descobertas:
        print('\nParabéns! Você venceu! A palavra era: ', palavra_secreta)
    else:
        print('\nQue pena! Você perdeu! A palavra era: ', palavra_secreta)

jogar_forca()