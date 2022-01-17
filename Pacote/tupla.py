ips={}
resp="S"
while resp=="S":
    ips[(input("Digite os dois primeiros octetos: "),
    input("Digite os dois ultimos octetos: "))]=input("Nome da maquina: ")
    resp=input("Digite <S> para continuar:").upper()


print("Exibindo máquinhas em uma mesma rede: ")
rede=input("Digite os dois primeiros octetos:")
for ip,nome in ips.items():
    print("Máquinas no mesmo endereço (redes diferentes)")
    if(ip[0]==rede):
        print(nome)

# print("Exibindo máquinhas com o mesmo endereço: ")
# pesquisa=input("Digite os dois últimos octetos:")
# for ip,nome in ips.items():
#     print("Máquinas no mesmo endereço (redes diferentes)")
#     if(ip[1]==pesquisa):
#         print(nome)

print("Exibindo ips: ")
for ip in ips.keys():
    print(ip[0]+"."+ip[1])