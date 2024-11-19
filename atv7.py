def soma_quadrados_dos_digitos(numero):
    return sum(int(digito) ** 2 for digito in str(numero))


def lista_soma_quadrados(limite):
    lista = []
    for num in range(1, limite + 1):
        lista.append((num, soma_quadrados_dos_digitos(num)))
    return lista


limite = 20
resultado = lista_soma_quadrados(limite)

for num, soma in resultado:
    print(f"Número: {num}, Soma dos quadrados dos dígitos: {soma}")
