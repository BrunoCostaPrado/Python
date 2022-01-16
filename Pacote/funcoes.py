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