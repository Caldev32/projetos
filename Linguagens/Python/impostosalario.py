#programa que calcula o salario liquido
#se valor < 1200
#se valor => 1200 E valor < 2500 =  93%
#se valor <= 2500 E valor <= 4000 = 90%
#se valor > 4000
#salario = float(input("Qual o seu salario?"))

while True:
    def calc_imposto(s):
        if s < 1200:
            print(f"o seu salario liquido é de R${s}")
        elif s >= 1200 and s < 2500:
            print(f"o seu salario liquido é de R${s*(93/100)}")
        elif s <= 2500 and s <= 4000:
            print(f"o seu salario liquido é de R${s*(90/100)}")
        elif s > 4000:
            print(f"o seu salario liquido é de R${s*(85/100)}")

    salario = (float(input("Qual o seu salario?")))
    calc_imposto(salario)

#calc_imposto(float(input("Qual o seu salario?")))
