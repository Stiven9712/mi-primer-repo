contador = 0
numero = 2
while contador < 20:
    es_primo = True
    divisor = 2
    while divisor <= int(numero ** 0.5):
        if numero % divisor == 0:
            es_primo = False
            break
        divisor += 1
    if es_primo:
        print(numero)
        contador += 1
    numero += 1