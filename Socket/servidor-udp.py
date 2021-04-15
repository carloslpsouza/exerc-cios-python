import socket
ip = '127.0.0.1'
porta = 2000
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
escuta = (ip, porta)
servidor.bind(escuta)
print("Servidor rodando na porta: " + str(porta))
while True:
    mensagem_recebida, origem = servidor.recvfrom(2048)
    mensagem_recebida = mensagem_recebida.decode()
    print(mensagem_recebida, origem)
    mensagem_recebida = mensagem_recebida.encode().upper()
    servidor.sendto(mensagem_recebida, origem)
    print(mensagem_recebida.decode(), origem)

servidor.close()
