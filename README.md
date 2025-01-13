Código simples em Python com a finalidade de escanear portas abertas nos hosts informados pelo usuário através de um range ('primeiro IP' e 'ultimo IP')
O scan é feito usando a lib socket e os sockets são enviados apenas nas portas já passadas pelo array 'portas', sendo elas 22, 80, 443, 8080, 8843,
há um timeout de 1 segundo para conexão com a porta para que não gere um tempo muito grande de tentativas em cada host.

A simple Python script designed to scan open ports on hosts specified by the user through a range ('first IP' and 'last IP'). The scan is performed using the socket library, and the sockets are sent only to the ports specified in the 'ports' array, which are 22, 80, 443, 8080, and 8843. There is a 1-second timeout for connection attempts to ensure that each host does not take too long to process.
