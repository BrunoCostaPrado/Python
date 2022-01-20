with open("teste.txt","w") as arquivo:
   arquivo.write("Nunca foi tão facil criar um arquivo.")



with open("teste.txt","a") as arquivo:
    arquivo.write("\nContinação do texto.")


with open("teste.txt","r") as arquivo:
   conteudo=arquivo.read()
print("Tipo de dado da varialvel",type(conteudo))
print("Conteudo do arquivo",conteudo)