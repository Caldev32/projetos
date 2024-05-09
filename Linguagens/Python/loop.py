def p(texto):
    print(texto)
while True:
    n = int(input("Quantos produtos você vai cadastrar? "))
    x = 1
    nomes = []
    while x <= n:
        nome = int(input("Digite o valor: "))
        nomes.append(nome)
        x += 1
    p(sum(nomes))
    pag = input("Qual a forma d pagamento \n cartao \n pix \n outros meios")
    if pag == "cartao":
        pag = int(input("1-cred \n 2-deb"))
        if pag == 1:
            p("aprovado")
        else:
            p("Aprovado")
    elif pag == "pix":
        p("Aprovado")
    else:
        p("mama")
