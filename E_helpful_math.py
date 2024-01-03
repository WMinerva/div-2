def quitar_simb(numeros):
    only_num = ""
    for char in numeros:
        if char not in "+":
            only_num += char
    return list(only_num)
def orden_adi_simb(only_num):
    num_ord = sorted(only_num)
    return num_ord
def tasks(texto):
    texto_final = orden_adi_simb(quitar_simb(texto))
    return print(*texto_final,sep="+")

tasks(input())
