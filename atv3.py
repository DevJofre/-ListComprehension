def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Verifica até a raiz quadrada de n
        if n % i == 0:
            return False
    return True


def lista_primos_quadrado_cubo(limite):
    lista = []
    for i in range(2, limite + 1):
        if eh_primo(i):
            lista.append((i, i**2, i**3))
    return lista


limite = 20
resultados = lista_primos_quadrado_cubo(limite)

for numero, quadrado, cubo in resultados:
    print(f"Número: {numero}, Quadrado: {quadrado}, Cubo: {cubo}")
