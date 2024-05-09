while True:
    l1 = float(input("Digite a medida do primeiro lado: "))
    l2 = float(input("Digite a medida do segundo lado: "))
    l3 = float(input("Digite a medida do terceiro lado: "))
    if (l1 + l2) > l3 and (l3 + l2) > l1 and (l1 + l3) > l2:
        if l1 == l2 == l3:
            print("o triangulo é equilatero.")
        elif l1 == l2 != l3 or l1 != l2 == l3 or l1 != l3 == l2:
            print("o triangulo é isosceles.")
        else:
            print("o triangulo é escaleno.")
    else:
        print("não é um triangulo")

