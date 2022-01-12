equipamentos=[]
valores=[]
seriais=[]
inventario=[]
departamentos=[]
resp="s"
while resp=="s":
    equipamentos.append(input("Equipamento: ")) 
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Numeros seriais: ")))
    departamentos.append(input("Departamento: "))
    resp=input("Digite S para continuar: ").upper()


for index in range(0,len(equipamentos)):   
    print("Equipamento..: ",(index+1))
    print("Nome.....:",equipamentos[index])
    print("Valor..."[index])
    print("Serial...:",seriais[index])
    print("Departamentos.:",departamentos[index])




busca=input("Digite o nome do equipamento: ")
for index in range(0,len(equipamentos)):
    if busca==equipamentos[index]:
        print("valor..: ",valores[index])
        print("seriais..: ",seriais[index])

seriais=input("Insira o serial a ser excluido: ")
for index in range(0,len(seriais)):
    if seriais[index]==seriais:
        del departamentos[index]
        del equipamentos[index]
        del seriais[index]
        del valores[index]
        break
for index in range(0,len(equipamentos)):   
    print("Equipamento..: ",(index+1))
    print("Nome.....:",equipamentos[index])
    print("Valor..."[index])
    print("Serial...:",seriais[index])
    print("Departamentos.:",departamentos[index])
