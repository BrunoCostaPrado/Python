with open("pagina.html","w") as pagina:
    pagina.write("<head><title>HTML criado em python</title> </head>")
    pagina.write("<body><h1>Esse e um teste para paginas WEB </h1>")
    pagina.write("<br><h2> abaixo seguem alguns nomes importantes para o projeto: </h2>")
    pagina.write("<h3>")
    nome=""
    while nome!="SAIR":
      nome=input("Digite seu nome ou SAIR:" ).upper()
      if nome!="SAIR":
         pagina.write("<br>"+nome)
pagina.write("</h3></body>")