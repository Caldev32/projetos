salario = float(input("Salario em reais: "))
setor = int(input("informe o setor do funcionario \n 1 ou 2 \n"))

if salario > 1000 and setor == 1:
    valorref = 200
elif setor > 1000 and setor == 2:
    valorref = 100
if salario <= 1000 and setor == 1:
    valorref = 300
elif setor <= 1000 and setor == 2:
    valorref = 250

print(f"{valorref} R$ é o valor refeição")
