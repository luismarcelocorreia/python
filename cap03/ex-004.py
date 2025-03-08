num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
operacao = input("Selecione uma operação (+, -, *, /): ")

if operacao == "+":
    res = num1 + num2
    print("Resultado: ", res)
elif operacao == "-":
    res = num1 - num2
    print("Resultado: ", res)
elif operacao == "*":
    res = num1 * num2
    print("Resultado: ", res)
elif operacao == "/":
    res = num1 / num2
    print("Resultado: ", res)
else:
    print("Operação invalida")

