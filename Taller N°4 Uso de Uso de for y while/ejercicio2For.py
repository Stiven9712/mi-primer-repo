contador = 0 
numero = 2
for _ in range (1, 1000):
    if contador == 20:
        break
    es_primo = True
    for i in range (2, int(numero ** 0.5)+1):
        if numero % i == 0:
                es_primo = False
                break
    if es_primo:
         print(numero)
         contador += 1
    numero += 1