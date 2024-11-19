def sao_anagramas(palavra1, palavra2):
    return sorted(palavra1) == sorted(palavra2)


def encontrar_anagramas(palavra, lista_palavras):
    return [p for p in lista_palavras if sao_anagramas(palavra, p)]


palavra = "listen"
lista_palavras = ["enlist", "google", "inlets", "banana", "silent"]

anagramas = encontrar_anagramas(palavra, lista_palavras)

print("Anagramas encontrados:", anagramas)
