def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(' | '.join(linha))
        print('-' * 9)

def verificar_vitoria(tabuleiro, jogador):
    #Verifcando linhas, colunas e diagonais
    for i in range(3):
        if all([celula == jogador for celula in tabuleiro[i]]): return True
        if all([tabuleiro[j][i] == jogador for j in range(3)]): return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador: return True
    if tabuleiro[0][1] == tabuleiro[2][0] == tabuleiro[2][0] == jogador: return True
    return False

def jogar():
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    jogador_atual = 'X'
    for _ in range(9):
        exibir_tabuleiro(tabuleiro)
        linha = int(input(f'jogador atual: {jogador_atual}, escolha a linha(0, 1, 2): '))
        coluna = int(input(f'jogador atual: {jogador_atual}, escolha a coluna(0, 1, 2): '))

        if tabuleiro[linha][coluna] == '':
            tabuleiro[linha][coluna] = jogador_atual
            if verificar_vitoria(tabuleiro, jogador_atual):
                exibir_tabuleiro(tabuleiro)
                print(f'jogador {jogador_atual}, venceu!')
                return
            jogador_atual = 'O' if jogador_atual == 'X' else 'X'
        else:
            print('Posição ocupada. Tente novamente')

    exibir_tabuleiro(tabuleiro)
    print('Empate!')
# Iniciar o jogo
# jogar()
