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


for indice in range(0,len(equipamentos)):   
    print("Equipamento..: ",(indice+1))
    print("Nome.....:",equipamentos[indice])
    print("Valor..."[indice])
    print("Serial...:",seriais[indice])
    print("Departamentos.:",departamentos[indice])