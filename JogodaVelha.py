from typing import Any

TAMANHO_DO_TABULEIRO = 3

#Função para exibir tabuleiro:
def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print('|'.join(linha if '' not in linha else ' ' for linha in linha))
        print('-'*(TAMANHO_DO_TABULEIRO * 2))

#Função para verificar se há um vencedor:
def verificar_vencedor(tabuleiro: object) -> Any | None:
    for i in range(TAMANHO_DO_TABULEIRO):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] !='':
            return tabuleiro[i][0]
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != '':
            return tabuleiro[0][i]
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] !='':
            return tabuleiro[0][0]
        if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] !='':
            return tabuleiro[0][2]
        return None

#Função para solicitar ao jogador a posição onde ele quer jogar
def obter_posicao_do_jogador():
    while True:
        try:
            linha, coluna = map(int, input('linha e coluna (1 a 3): ').split())
            return linha - 1, coluna - 1
        except ValueError:
            print('Entrada inválida! Certifique-se de digitar números separados por espaço.')

#Função para alternar entre jogadores
def alternar_jogador(jogador):
    return '0' if jogador == 'X' else 'X'

#Função principal do jogo da velha
def joga_da_velha():
    tabuleiro = [['' for _ in range(TAMANHO_DO_TABULEIRO)]]
    jogador = 'X'
    jogadas_restantes = TAMANHO_DO_TABULEIRO ** 2

    while jogadas_restantes > 0:
        mostrar_tabuleiro(tabuleiro)
        print(f'Vez do jogador {jogador}. Escolha posição: ')

        linha, coluna = obter_posicao_do_jogador()

        if linha not in range(TAMANHO_DO_TABULEIRO) or coluna not in range(TAMANHO_DO_TABULEIRO):
            print('Posição fora do tabuleiro! Tente novamente.')
            continue

        if tabuleiro[linha][coluna] != '':
            print('Posição já ocupada! Tente novamente.')
            continue

        tabuleiro[linha][coluna] = jogador
        vencedor = verificar_vencedor(tabuleiro)

        if vencedor:
            mostrar_tabuleiro(tabuleiro)
            print(f'Parabéns! O jogador {vencedor} venceu!')
            return
        jogador = alternar_jogador(jogador)
        jogadas_restantes -= 1

    mostrar_tabuleiro(tabuleiro)
    print('Empate! O jogo terminou sem vencedor.')

joga_da_velha()