#palindromos

palabras: list[str] = ['agua', 'rotor', 'perla', 'reconocer', 'ojo', 'peso']

def palindromo(lista: list[str]):
    palindromos = []
    for x in lista:
        palabra = ""
        for y in range(len(x)-1, -1, -1):
            palabra += x[y]
        if x == palabra:
            palindromos.append(x)
    
    print(palindromos)
    return palindromos
        


palindromo(palabras)
