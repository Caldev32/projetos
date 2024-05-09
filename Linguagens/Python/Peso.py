while True:
    salarioA = int(input("digite o seu salario em reais "))
    if salarioA <= 1000:
        salario = salarioA + (salarioA*0.15)
        print(f"o seu novo salario é R${salario}")
    elif salarioA <= 2000:
        salario = salarioA + (salarioA*0.10)
        print(f"o seu novo salario é R${salario}")

    elif salarioA <= 3000:
        salario = salarioA + (salarioA*0.5)
        print(f"o seu novo salario é R${salario}")
    else:
        salario = salarioA + (salarioA*0.3)
        print(f"o seu novo salario é R${salario}")

