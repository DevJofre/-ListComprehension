def divisores_proprios(n):
    divisores = []
    for i in range(1, n):
        if n % i == 0:
            divisores.append(i)
    return divisores


def eh_perfeito(n):
    return sum(divisores_proprios(n)) == n


def numeros_perfeitos(limite):
    perfeitos = []
    for num in range(2, limite + 1):
        if eh_perfeito(num):
            perfeitos.append(num)
    return perfeitos


limite = 10000
resultado = numeros_perfeitos(limite)

print(f"Números perfeitos até {limite}:")
print(resultado)
