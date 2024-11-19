
def contar_vogais_consoantes(palavra):
    vogais = "aeiouAEIOU"
    contagem_vogais = 0
    contagem_consoantes = 0

    for letra in palavra:
        if letra.isalpha():
            if letra in vogais:
                contagem_vogais += 1
            else:
                contagem_consoantes += 1

    return (contagem_vogais, contagem_consoantes)


def lista_contagem_vogais_consoantes(lista_palavras):
    return [contar_vogais_consoantes(palavra) for palavra in lista_palavras]


palavras = ["banana", "abacaxi", "melancia", "uva", "goiaba"]

resultados = lista_contagem_vogais_consoantes(palavras)

for palavra, (vogais, consoantes) in zip(palavras, resultados):
    print(f"Palavra: {palavra}, Vogais: {vogais}, Consoantes: {consoantes}")
