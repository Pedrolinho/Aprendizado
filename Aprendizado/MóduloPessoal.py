def somar(x, y):
    print(x + y)


def IMC(altura, peso):

    indice = peso / ((altura / 100)** 2)
    print(f'O seu índice IMC é: {indice}')

    if indice >= 40:
        print('O estado é de obesidade grave.')
    elif indice >= 30:
        print('O estado é de obesidade.')
    elif indice >= 25:
        print('O estado é de sobrepeso.')
    elif indice >= 18.5:
        print('O estado é normal.')
    else:
        print('O estado é de magreza.')
