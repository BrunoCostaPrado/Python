def perguntar():
    res=input(input("O que deseja realizar: ?"
    +"<I>- Para inserir um usuario: "
    +"<P>- Para Pesquisar um usuario: "
    +"<E>- Para Excluir um usuario: "
    +"<L>- Para Listar um usuario: ").upper())
    return res

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()]=[input("Digite o nome:").upper(),
        input("Digite a ultima data de acesso: ").upper(),
        input("Qual a última estação acessada: ").upper()]
def pesquisar(dicionario,chave):
    lista=dicionario.get(chave)
    if lista!=None:
        print("Nome...........:"+lista[0])
        print("Ultimo acesso..:"+lista[1])
        print("Ultima estação.:"+lista[2])
def excluir(dicionario,chave):
    if dicionario.get(chave)!=None:
        del dicionario[chave]
        print("Objeto Eliminado")

def listar(dicionario):
        for chave,valor in dicionario.itens():
            print("Objeto.......")
            print("Login: ",chave)
            print("Dados: ",chave)
