# pyModbusClient
 Um cliente Modbus com pyModbusTCP..
    Agora lendo também valores float no padrão IEEE754

----------------------------------
          Cliente Mosbus
----------------------------------
Qual serviço? 
1- Leitura    
2- Escrita    
3- Configuração
4- Sair
Serviço: 1

Qual tipo de dado deseja ler?
1- Coil Status
2- Input Status
3- Holding Register
4- Input Register
Type: 2
Address: 2
Length: 10
Quantidade de leituras: 2

Começando leitura..
Leitura 1: [True, True, False, False, True, True, False, False, False, False]
Leitura 2: [True, True, False, False, False, False, False, False, False, False]
Fim de leitura..

----------------------------------
          Cliente Mosbus
----------------------------------
Qual serviço?
1- Leitura
2- Escrita
3- Configuração
4- Sair
Serviço: 2

Qual tipo de dado deseja escrever?
1- Coil Status
2- Holding Register
Tipo: 1
Digite o endereço: 004
Digite o valor que deseja escrever: 1

Escrevendo..
Valor 1 escrito no endereço 4

----------------------------------
          Cliente Mosbus
----------------------------------
Qual serviço?
1- Leitura
2- Escrita
3- Configuração
4- Sair
Serviço: 2

Qual tipo de dado deseja escrever?
1- Coil Status
2- Holding Register
Tipo: 2
Digite o endereço: 106
Digite o valor que deseja escrever: 6666

Escrevendo..
Valor 6666 escrito no endereço 106
