numeros = list(range(1,101))

# Usa a list comprehension para gerar uma lista somente com números pares e divisíveis por 4
pares_div4 = [numero for numero in numeros if numero %2 == 0 and numero % 4 == 0]
print(pares_div4)