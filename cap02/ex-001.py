numeros = list(range(1,101))

# Percorre a lista e verifica se um numero é par e divisivel por 4
for numero in numeros:
    if numero % 2 == 0 and numero % 4 == 0:
        print(numero)
