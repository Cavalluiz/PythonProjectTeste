def imprimir_tabuleiro(board):
    for i, linha in enumerate(board):
        print(f' {linha[0]} | {linha[1]} | {linha[2]}')
        if i < 2:
            print('---+---+---')

def verificar_vitoria(board, jogador):
    #linhas, colunas e diagonais
    vitoria = [[(i, j) for j in range(3)] for i in range(3)] + \
              [[(j, i) for j in range(3)] for i in range(3)] + \
              [[(i, i) for i in range(3)], [(i, 2 - i) for i in range(3)]]
    return any(all(board[r][c] == jogador for r,  c in caminho) for caminho in vitoria)

def jogo_da_velha():
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    jogador_atual = 'X'
    jogadas = 0

    print('--- Jogo da Velha: ---')

    while jogadas < 9:
        imprimir_tabuleiro(tabuleiro)
        try:
            escolha = int(input(f'\nJogador {jogador_atual}, escolha uma posição(1-9): ')) - 1
            row, col = divmod(escolha, 3)

            if tabuleiro[row][col] != ' ':
                print('Posição já ocupada! Tente novamente.')
                continue
        except (ValueError, IndexError):
            print('Entrada inválida! Digite um número de 1 a 9.')
            continue

        tabuleiro[row][col] = jogador_atual
        jogadas += 1

        if verificar_vitoria(tabuleiro,  jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f'\nParabéns! O jogador {jogador_atual} venceu!')
            return
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

    imprimir_tabuleiro(tabuleiro)
    print('\nEmpate!')
if __name__ == '__main__':
    jogo_da_velha()