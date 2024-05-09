tempo = float(input("Qual o tempo de empresa: ")) 
salario = float(input("Qual o valor do salario: "))

if salario <= 1000: 
    if tempo <= 3:
        salario = salario + salario*0.05
    else:
        salario = salario + salario*0.1
elif salario <= 3000:
    if tempo <= 5:
        salario =  salario + salario*0.15
    else:
        salario =  salario + salario*0.2
else:
    if tempo < 10:
        salario = salario + salario*0.25
    else:
        salario = salario + salario*0.3
        
print(f"o seu novo salario é {salario}")