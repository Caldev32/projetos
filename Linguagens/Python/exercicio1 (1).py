preco = float(input("Informe o preço do produto: "))
dep = int(input("Informe o departamento do produto: \n 1-A \n 2-B \n 3-C \n "))
cor = int(input("Informe a cor da entiqueta: \n 1-Azul \n 2-Branca \n 3-Verde \n 4-Preta \n"))
if dep == 1:
    match(cor):

        case 1:
            preco = preco - preco * 0.06
        case 2:
            preco = preco - preco * 0.07
        case 3:
            preco = preco - preco * 0.08
        case 4:
            preco = preco - preco * 0.09
        case _:
            print("valor invalido")

elif dep == 2:
    match(cor):

        case 1:
            preco = preco - preco * 0.063
        case 2:
            preco = preco - preco * 0.074
        case 3:
            preco = preco - preco * 0.082
        case 4:
            preco = preco - preco * 0.091
        case _:
            print("valor invalido")
            
elif dep == 3:
    match(cor):

        case 1:
            preco = preco - preco * 0.056
        case 2:
            preco = preco - preco * 0.067
        case 3:
            preco = preco - preco * 0.078
        case 4:
            preco = preco - preco * 0.109
        case _:
            print("valor invalido")
            
else :
    print("departamento invalido")

print(f"O valor do produto é {round(preco,2)} R$")
