#tipos de produtos
    #alimentos, limpeza e bebidas
#digitar o tipo do produto
#preço produto
#gasto produto produtos
#qual tipo de produto teve o maior gasto
limpeza = []
alimento = []
bebidas = []

def produtos(n):
    for i in range(n):
        tipo = str(input("Qual o tipo de produto? Limpeza, Alimento ou Bebidas?"))
        preco = float(input("Qual o preço do seu produto?"))
        if tipo == "Limpeza":
            limpeza.append(preco)
        elif tipo == "Alimento":
            alimento.append(preco)
        elif tipo == "Bebidas":
            bebidas.append(preco)
    for produt in limpeza:
        print(f"{produt}, Na area de Limpeza")
    print(f"com um total total gasto de R${sum(limpeza)} em limpeza")
    for produt in bebidas:
        print(f"{produt}, Na area de Bebidas")
    print(f"com um total total gasto de R${sum(bebidas)} em bebidas")
    for produt in alimento:
        print(f"{produt}, Na area de Alimentos")
    print(f"com um total total gasto de R${sum(alimento)} em alimentos")
    somal = sum(limpeza)
    somaa = sum(alimento)
    somab = sum(bebidas)
    print(f"com um total gasto de R${somal + somaa + somab }")



numero = int(input("Quantos produtos você irá cadastrar?"))
produtos(numero)
