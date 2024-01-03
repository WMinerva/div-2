word_a = input().lower()
word_b = input().lower()
lista = [word_a, word_b]
lista_two = sorted(lista)
# print(*lista_two)
if lista[0] == lista[1]:
    print(0)
elif lista[0]==lista_two[0]:
    print(-1)
else:
    print(1)
