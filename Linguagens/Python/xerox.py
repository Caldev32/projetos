#ler o valor do xerox
quantidade = 1
valor = 0.06
tabela = []

while quantidade <= 100 and valor <= 6:
    valor += 0.06
    tabela.append(valor)
    quantidade += 1
    tabela.append(quantidade)
print(tabela)
