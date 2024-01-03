# dado una entrada string verificar si dice "hello"
def cadena(texto):
    word_pass = "hello"
    cod = 0
    for char in range(len(texto)):
        if word_pass[cod] == texto[char]:
            cod += 1
        if cod == 5:
            break
    if cod == 5:
        print("YES")
    else:
        print("NO")
cadena(input())
