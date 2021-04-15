import socket
ip = '127.0.0.1'
porta = 2000
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destino = (ip, porta)

print("Para sair pressione CTRL+X\n")
while True:
    mensagem = input("Digite a mensagem: ")
    mensagem = mensagem.encode()
    servidor.sendto(mensagem ,destino)
    retorno, origem = servidor.recvfrom(2048)
    print(retorno.decode(), origem)
servidor.close()
