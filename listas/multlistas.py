equipamentos=["impressora"]
valores=[1]
seriais=[2]
busca=input("Digite o nome do equipamento: ")
for index in range(0,len(equipamentos)):
    if busca==equipamentos[index]:
        print("valor..: ",valores[index])
        print("seriais..: ",seriais[index])