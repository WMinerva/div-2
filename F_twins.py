def moneda(num_coins):
    monedas = list(map(int,input().split()))
    
    def suma_coins(monedas, num_coins):
        suma = 0
        for i in range(0,num_coins):
            suma += monedas[i]
        return suma

    valor_total_coins = suma_coins(monedas,num_coins)
    coin_sort = sorted(monedas)
    coin_sort.reverse()
    # print(*coin_sort)
    coin_bro = 0
    i = 0
    while coin_bro < valor_total_coins//2 + 1:
        coin_bro += coin_sort[i]
        i+=1
    return print(i) 
moneda(int(input()))
