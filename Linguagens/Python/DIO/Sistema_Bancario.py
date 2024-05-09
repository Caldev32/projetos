

#
saldo = .0
saquesd = 3

extrato = ""
while True:
    op = int(input("""
                    |      OPERAÇÕES DISPONIVEIS       |
                    |                                  |
                    |      1 - DEPOSITOS               | 
                    |      2 - SAQUE                   | 
                    |      3 - EXTRATO DA CONTA        | 
                    |                                  | 
                    |##################################| 
                    |                                  | 
                    |       Insira a operação          |
                                    """))
    #deposito: somente valores positivos, todos devem ser armazenadas em uma variavel e exibidos em extrato 
    if op == 1:
        valord = float(input("Insira o valor do deposito desejado:"))
        if valord > 0:
            saldo += valord
            extrato += f"\n + R$ {valord}"
        else:
            print("valor invalido")
    #saque: 3 saques diarios, com um limite de 500 reais, caso o usuario não tenha saldo exibir uma mensagem dizendo que não tem saldo, todos saques devem ser armezanos em extrato e retirados de saldo
    elif op == 2:
        valors = float(input("Insira o valor do saque desejado: "))
        if valors > 0 and valors <= 500:
            if saquesd > 0:
                if saldo - valors > 0:
                    saquesd -= 1
                    saldo -= valors
                    extrato += f"\n - R$ {valors}"
                else:
                    print("Saldo Insuficiente")                       
            else:
                print("Você já atingiu o seu limite de saques diarios! ")

        else:
            print("valor invalido")
    #extrato exibe a string que foi concatenada e a soma de saldo
    elif op == 3:
        print(f"""
                {extrato} 

                Saldo atual: R$ {saldo}
                """)
    continua = input("Deseja continuar? (S/N) ")
    continua = continua.lower()
    if continua == "s":
        pass
    else:
        break

print("Obrigado por ultilizar nosso sistema!")
