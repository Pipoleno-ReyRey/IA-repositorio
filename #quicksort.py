
def quicksort(listaPrincipal: list[int]):
    if len(listaPrincipal) <= 1:
        return listaPrincipal
    else:
        pivote = listaPrincipal[0]
        listaMenores = []
        listaIguales = []
        listaMayores = []
        for x in listaPrincipal:
            if x < pivote:
                listaMenores.append(x)
        for x in listaPrincipal:
            if x == pivote:
                listaIguales.append(x)
        for y in listaPrincipal:
            if y > pivote:
                listaMayores.append(y)

        return quicksort(listaMenores) + listaIguales + quicksort(listaMayores)



        
print(quicksort([1,3,4,2,5,6,-1,9,11,7]))

