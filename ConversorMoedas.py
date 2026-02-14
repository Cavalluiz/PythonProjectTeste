def conversor_de_moedas():
    real = float(input('Digite o valor em reais: R$: '))
    taxa_cambio = float(input('Informe a taca de câmbio atual(exemplo: 1 USD para BRL): '))
    dolar = real / taxa_cambio
    print(f'O valor em dólares é: ${dolar:.2f}')

conversor_de_moedas()