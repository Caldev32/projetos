# cpf : {nome: , data de nascimento: , endereço: , }
def criar_conta(agencia, conta, usuarios):
    cpf = int(input("Informe seu cpf(somente numeros): "))
    verifica = filtrar_usuarios(cpf, usuarios)
    if verifica:
        print("conta criada com sucesso!")
        return{"agencia":agencia, "conta":conta, "usuario": verifica}
    
    print("Não foi encontrato um usuario, por favor fça seu cadastro novamente")


def criar_usuario(usuarios):
    cpf = int(input("Informe seu CPF: "))
    verifica = filtrar_usuarios(cpf, usuarios)
    if verifica:
        print("Já existe um usuario com esse cpf!")
        return
    
    nome = input("Informe o seu nome: ")
    data_de_nascimento = input("Informe sua data de nascimento (DD-MM-AAAA): ")
    cep = int(input("Informe seu CEP (Somente Numeros): "))

    usuarios.append({"cpf":cpf,"nome":nome,"nascimento":data_de_nascimento, "CEP":cep })
    print("Cadastro feito com sucesso!")

    

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuarios for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None



def saque(*,saquesd, limite):
    valors = float(input("Insira o valor do saque desejado: "))
    global saldo
    global extrato
    if valors > 0 and valors <= limite:
        if len(saquesd) > 0:
            if saldo - valors > 0:
                saquesd.pop()
                saldo -= valors
                extrato += f"\n - R$ {valors}"
            else:
                print("Saldo Insuficiente")                       
        else:
            print("Você já atingiu o seu limite de saques diarios! ")
    else:
            print("valor invalido")
    return extrato, saldo

def deposito():
    valord = float(input("Insira o valor do deposito desejado:"))
    global saldo
    global extrato
    if valord > 0:
        saldo += valord
        extrato += f"\n + R$ {valord}"
    else:
        print("valor invalido")
    return saldo, extrato
    

def tirar_extrato():
    global saldo
    global extrato
    print(f"""
            {extrato} 

            Saldo atual: R$ {saldo}
                """)
#
saldo = .0
saquesd = [0, 1, 2]
extrato = ""
limite = 500
usuarios = []
conta = []
agencia = "0001"


while True:
    op = int(input("""
                    |      OPERAÇÕES DISPONIVEIS       |
                    |                                  |
                    |      1 - DEPOSITOS               | 
                    |      2 - SAQUE                   | 
                    |      3 - EXTRATO DA CONTA        | 
                    |      4 - NOVA CONTA              |
                    |      5 - NOVO USUARIO            |
                    |                                  | 
                    |##################################| 
                    |                                  | 
                    |       Insira a operação          |
                                    """))
    #deposito: somente valores positivos, todos devem ser armazenadas em uma variavel e exibidos em extrato 
    if op == 1:
        deposito()
    #saque: 3 saques diarios, com um limite de 500 reais, caso o usuario não tenha saldo exibir uma mensagem dizendo que não tem saldo, todos saques devem ser armezanos em extrato e retirados de saldo
    elif op == 2:
        saque(saquesd=saquesd, limite=limite)
    #extrato exibe a string que foi concatenada e a soma de saldo
    elif op == 3:
        tirar_extrato()
    elif op == 4:
        numero_conta = len(conta) + 1
        contas = criar_conta(usuarios=usuarios, conta=numero_conta, agencia=agencia)
        if contas:
            conta.append(contas)

    elif op == 5:
        criar_usuario(usuarios)

    


    continua = input("Deseja continuar? (S/N) ")
    continua = continua.lower()
    if continua == "s":
        pass
    else:
        break

print("Obrigado por ultilizar nosso sistema!")




