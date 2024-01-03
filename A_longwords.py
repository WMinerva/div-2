for i in range(0,int(input())):
    word = input()
    l = len(word)
    if l > 10:
        # print(word[0],l-2,word[l-1],sep="")
        print(f"{word[0]}{l-2}{word[l-1]}")
    else:
        print(word)
