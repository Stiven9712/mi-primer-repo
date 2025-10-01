def lista_potencia (n,lst):
    nueva_lista = []
    for x in lst:
          potencia = x**n
          nueva_lista.append(potencia)
    return nueva_lista

exponente = 2
lista_numeros = [1,2,3,4,5]

resultado = lista_potencia(exponente,lista_numeros)

print(resultado)