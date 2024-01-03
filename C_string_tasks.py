# cadena = input()
# print (cadena.lower())
def consonantes(texto):
    only_consonante = ""
    for char in texto.lower():
        if char not in "aeiouy":
            # only_consonante = only_consonante + char
            only_consonante += char
    return only_consonante
def adi_punto(texto):
    cadena_final = ""
    for char in texto:
        cadena_final = cadena_final+"."+char
    return cadena_final
def tasks(texto):
    texto = consonantes(texto)
    texto_puntos = adi_punto(texto)
    return texto_puntos

print(tasks(input()))
