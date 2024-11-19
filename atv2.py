def is_palindromo(palavra):
    return palavra == palavra[::-1]


def filtrar_palindromos(lista):
    return [palavra for palavra in lista if is_palindromo(palavra)]


palavras = ["ana", "radar", "python", "level", "teste", "civic", "java"]

palindromos = filtrar_palindromos(palavras)

print("Palavras palíndromas:", palindromos)
