import math


def mdc(a, b):
    return math.gcd(a, b)


def mmc_lista(n):
    mmc = 1
    for i in range(1, n + 1):
        mmc = mmc * i // mdc(mmc, i)
    return mmc


def divisiveis_por_todos(n):
    mmc = mmc_lista(n)
    multiplos = []

    for i in range(1, n+1):
        multiplos.append(mmc * i)
    return multiplos


n = 6
resultado = divisiveis_por_todos(n)

print(f"Múltiplos do MMC de 1 até {n}: {resultado}")
