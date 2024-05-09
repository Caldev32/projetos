
print("((( tipos de pulverizaçao ))) \n 1- erva daninhas \n 2 - gafanhotos \n 3 - Broca \n 4 - Todos")
tipo = int(input("Tipo: ")) 
acres = float(input("Total de acres: "))
if tipo ==1:
    preco = acres*500
elif tipo == 2:
    preco = acres*1000
elif tipo == 3:
    preco = acres*1500
elif tipo == 4:
    preco = acres*2500
else:
    raise ValueError("invalido")
print(f"{preco} R$")
>>>>>>> d284460155be172dbacb94c39cdc1629b0230eee