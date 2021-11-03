
def particao2(lista, i, j):
    pivo = lista[i]
    # item = i

    # print("Pivo ",pivo)

    # Caso Base
    if len(lista)==1:
        return 0

    while(j>=i):
        if(lista[i]<=pivo):
            i+=1
        elif(lista[j]>pivo):
            j-=1
        else:
            (lista[i],lista[j]) = (lista[j], lista[i])
            i+=1
            j-=1

    print("lista PIVO NÃ0 INSERIDO = ",lista)
    # print("j ",lista[j])

    # aux=1
    listaFinal=lista
    # while(aux<len(lista)):
    #     if(aux==i):
    #         listaFinal.append(pivo) 
    #     listaFinal.append(lista[aux])
    #     aux+=1
    (listaFinal[0],listaFinal[j]) = (listaFinal[j], listaFinal[0])

    if(len(listaFinal)!=len(lista)):
        listaFinal.append(pivo)

    print("lista Final = ",listaFinal)
    return i-1 

def particao(lista, i, j):
    pivo = lista[i]
    item = i
    # Caso Base
    if len(lista)==1:
        return 0

    print("item ",item)
    for x in range(i+1, j):
        if lista[x] <= pivo:
            item = item + 1
            (lista[item], lista[x]) = (lista[x], lista[item])
    
    (lista[item ], lista[i]) = (lista[i], lista[item ])
    print("lista depos = ",lista)
    return item 

if __name__ == '__main__':
    lista= [70,26,2,36,5]
    print("lista antes = ",lista)
    # print(particao(lista,0,len(lista)-1))
    print(particao2(lista,0,len(lista)-1))
    