# pyModbusClient
 Um cliente Modbus com pyModbusTCP.
 - Com banco de dados SQLite

Reading modbus displays:

 - Decimal;
 - Floating Point;
 - Float (Swapped);


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
 
Type: 3

 1- Decimal
 2- Floating Point
 3- Float Swapped
 
Leitura: 3

 Address: 1
 Length: 4
 Quantidade de leituras: 1

Começando leitura FLOAT..

Leitura 1:
  360.28
  10.1
  -13.5
  0.0

Fim de leitura FLOAT..

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
