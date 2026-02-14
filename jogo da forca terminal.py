import random


def desenhar_forca(erros):
    estagios = [
        "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="
    ]
    return estagios[erros]


def jogar():
    palavras = ['python', 'programacao', 'algoritmo', 'computador', 'desenvolvedor']
    palavra = random.choice(palavras).upper()
    letras_descobertas = ["_" for _ in palavra]
    letras_erradas = []
    tentativas = 6

    print("--- BEM-VINDO AO JOGO DA FORCA ---")

    while tentativas > 0 and "_" in letras_descobertas:
        print(desenhar_forca(6 - tentativas))
        print(f"\nPalavra: {' '.join(letras_descobertas)}")
        print(f"Erros: {', '.join(letras_erradas)}")

        chute = input("Digite uma letra: ").upper().strip()

        if not chute or len(chute) > 1 or not chute.isalpha():
            print("Digite apenas uma letra válida!")
            continue

        if chute in letras_descobertas or chute in letras_erradas:
            print("Você já tentou essa letra!")
            continue

        if chute in palavra:
            for i, letra in enumerate(palavra):
                if letra == chute:
                    letras_descobertas[i] = chute
        else:
            letras_erradas.append(chute)
            tentativas -= 1

    print(desenhar_forca(6 - tentativas))
    if "_" not in letras_descobertas:
        print(f"\nParabéns! Você venceu. A palavra era: {palavra}")
    else:
        print(f"\nVocê perdeu! A palavra era: {palavra}")


if __name__ == "__main__":
    jogar()
