import socket
resp="S"
while(resp=="S"):
    url=input("Digite uma url: ")
    ip=socket.gethostbyname(url)
    ip6=socket.getaddrinfo(url,None, socket.AF_INET6)
    print("O IPV4 referente á url informanda é: ",ip)
    print("O IPV6 referente á url informanda é: ",ip6)
    resp=input("Digite <s> para continuar: ").upper()
    