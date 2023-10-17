# [PY-A05] Escreva uma função em Python que recebe uma lista de números inteiros e retorna a média aritmética dos valores:

numeros = []
def media_aritmetica(numeros):
    num = 1
    while num != 0:
        num = int(input("Insira um número inteiro (para encerrar digite 0): "))
        numeros.append(num)

    total = 0
    for numero in numeros:
        total += numero
    media = total / (len(numeros) - 1)

    print(f"A média aritmética da lista é {media}")

media_aritmetica(numeros)