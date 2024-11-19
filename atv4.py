def substrings(s):
    lista_substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            lista_substrings.append(s[i:j])
    return lista_substrings


string = "abc"
resultado = substrings(string)

print(resultado)
