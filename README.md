Código simples em Python com a finalidade de escanear portas abertas nos hosts informados pelo usuário através de um range ('primeiro IP' e 'ultimo IP')
O scan é feito usando a lib socket e os sockets são enviados apenas nas portas já passadas pelo array 'portas', sendo elas 22, 80, 443, 8080, 8843,
há um timeout de 1 segundo para conexão com a porta para que não gere um tempo muito grande de tentativas em cada host.
