from funcoes import *


''' usuarios={}
opcao=input("O que deseja realizar: ?"
+"<I>- Para inserir um usuario: "
+"<P>- Para Pesquisar um usuario: "
+"<E>- Para Excluir um usuario: "
+"<L>- Para Listar um usuario: ").upper()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L" :
    if opcao=="I":
        chave=input("Digite o login: ").upper()
        usuarios[chave]=[input("Digite o nome:").upper(),
        input("Digite a ultima data de acesso: ").upper(),
        input("Qual a última estação acessada: ").upper()]
         usuarios[input("Digite o login: ").upper()]=[input("Digite o nome:").upper(),
        input("Digite a ultima data de acesso: ").upper(),
        input("Qual a última estação acessada: ").upper()] '

    opcao=input("O que deseja realizar: ?"
    +"<I>- Para inserir um usuario: "
    +"<P>- Para Pesquisar um usuario: "
    +"<E>- Para Excluir um usuario: "
    +"<L>- Para Listar um usuario: ").upper()'''

usuarios={}
opcao=perguntar()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L" :
    if opcao=="I":
        inserir(usuarios)
        opcao=perguntar()
    if opcao=="P":
       pesquisar(usuarios,input("Qual login deseja pesquisar? "))
    if opcao=="E":
       excluir(usuarios,input("Qual login deseja excluir? "))
    if opcao=="L":
       listar(usuarios)
    opcao=perguntar()