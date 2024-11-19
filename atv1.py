def transposta(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    matriz_transposta = [[matriz[j][i]
                          for j in range(linhas)] for i in range(colunas)]

    return matriz_transposta


matriz = [
    [100, 200, 300],
    [400, 500, 600],
    [700, 800, 900]
]

matriz_transposta = transposta(matriz)

for linha in matriz_transposta:
    print(linha)
