import math


def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def gerar_primos(limite):
    primos = []
    for num in range(2, limite + 1):
        if eh_primo(num):
            primos.append(num)
    return primos


def produtos_de_tres_primos(limite):
    primos = gerar_primos(limite)
    produtos = []

    for i in range(len(primos)):
        for j in range(i + 1, len(primos)):
            for k in range(j + 1, len(primos)):
                produto = primos[i] * primos[j] * primos[k]
                produtos.append(produto)

    return produtos


limite = 30
resultado = produtos_de_tres_primos(limite)

print(f"Produtos de três primos distintos até {limite}:")
print(resultado)
