x=input("Digite o nível de acesso:\n").upper()
if x=="ADM" or x=="USR":
    y=input("Insira seu genero:\n").upper()
    if x=="ADM":
        if y=="FEMININO":
            print("Ola Administradora")
        else:
            print("Ola Administrador")
    else:
        if y=="FEMININO":
            print("Ola Usuaria")
        else:
            print("Ola Usuario")
elif x=="GUEST":
    print("Ola Visitante")
else:
    print("Login não encontrado")