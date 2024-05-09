# calculadora 
n1 = float(input("Informe o primeiro numero: "))
n2 = float(input("Informe o segundo numero: "))
op = int(input("Informe o operador \n 1-Adição \n 2 Subtração \n 3-Multiplicação \n 4-Divisão \n"))
resultado = 0
match(op):
    case 1:
        resultado = n1 + n2
    case 2:
        resultado = n1 - n2
    case 3:
        resultado = n1 * n2
    case 4:
        resultado = n1 / n2
    case _:
        print("Operador invalido")

print(f"O seu resultado é {resultado}.")
