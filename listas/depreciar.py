depreciar=input("Digite o nome do equipamento depreciado:")
equipamentos=["impressora"]
valores=[int(input("Insira o valor: "))]
seriais=input("Insira o serial: ")
for index in range(0,len(equipamentos)):
    if depreciar==equipamentos[index]:
        print("Valor antigo",valores[index])
        valores[index]=valores[index]*0.9
        print("Novo valor:" ,valores[index])