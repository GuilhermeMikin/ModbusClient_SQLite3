from pyModbusTCP.client import ModbusClient
from time import sleep


class ClienteMODBUS():
    """
    Classe Cliente MODBUS
    """

    def __init__(self, server_ip, porta, scan_time=1):
        """
        Construtor
        """
        self._cliente = ModbusClient(host=server_ip, port=porta)
        self._scan_time = scan_time

    def atendimento(self):
        """
        Método para atendimento do usuário
        """
        try:
            self._cliente.open()
            print('Cliente conectado..')

        except Exception as e:
            print('\033[31mERRO: ', e.args, '\033[m')

        try:
            atendimento = True
            while atendimento:
                print('-' * 34)
                print('Cliente Mosbus'.center(34))
                print('-' * 34)
                sel = input("Qual serviço? \n1- Leitura \n2- Escrita \n3- Configuração \n4- Sair \nServiço: ")
                if sel == '1':
                    print('\nQual tipo de dado deseja ler?')
                    print("1- Coil Status \n2- Input Status \n3- Holding Register \n4- Input Register")
                    while True:
                        tipo = int(input("Type: "))
                        if tipo > 4:
                            print('\033[31mDigite um tipo válido..\033[m')
                            sleep(0.8)
                        else:
                            break
                    addr = input(f'Address: ')
                    leng = input(f'Length: ')
                    nvezes = input('Quantidade de leituras: ')
                    print('\nComeçando leitura..')
                    sleep(1)
                    for i in range(0, int(nvezes)):
                        print(f'\033[33mLeitura {i + 1}:\033[m {self.lerDado(int(tipo), int(addr), int(leng))}')
                        sleep(self._scan_time)
                    print('Fim de leitura..\n')
                    sleep(0.8)

                elif sel == '2':
                    sleep(1)
                    print('\nQual tipo de dado deseja escrever? \n1- Coil Status \n2- Holding Register')
                    sleep(0.5)
                    while True:
                        tipo = int(input("Tipo: "))
                        if tipo > 2:
                            print('\033[31mDigite um tipo válido..\033[m')
                            sleep(0.8)
                        else:
                            break
                    addr = input(f'Digite o endereço: ')
                    valor = int(input(f'Digite o valor que deseja escrever: '))
                    print('\nEscrevendo..')
                    sleep(1.5)
                    self.escreveDado(int(tipo), int(addr), valor)

                elif sel == '3':
                    scant = input('Novo tempo de varredura [s]: ')
                    self._scan_time = float(scant)

                elif sel == '4':
                    sleep(0.5)
                    print('\n\033[32mFechando sistema..\033[m')
                    sleep(1)
                    self._cliente.close()
                    atendimento = False

                else:
                    sleep(0.3)
                    print('\033[31mSeleção inválida..\033[m\n')
                    sleep(0.7)
        except Exception as e:
            print('\033[31mERRO: ', e.args, '\033[m')


    def lerDado(self, tipo, addr, leng):
        """
        Método para leitura MODBUS
        """
        if tipo == 1:
            return self._cliente.read_coils(addr - 1, leng)
        elif tipo == 2:
            return self._cliente.read_discrete_inputs(addr - 1, leng)
        elif tipo == 3:
            return self._cliente.read_holding_registers(addr - 1, leng)
        elif tipo == 4:
            return self._cliente.read_input_registers(addr - 1, leng)
        else:
            print('Tipo de leitura inválido..')

    def escreveDado(self, tipo, addr, valor):
        """
        Método para escrita MODBUS
        """
        try:
            if tipo == 1:
                print(f'\033[33mValor {valor} escrito no endereço {addr}\033[m\n')
                return self._cliente.write_single_coil(addr - 1, valor)
            elif tipo == 2:
                print(f'\033[33mValor {valor} escrito no endereço {addr}\033[m\n')
                return self._cliente.write_single_register(addr - 1, valor)
            else:
                print('Tipo de escrita inválido..\n')

        except Exception as e:
            print('\033[31mERRO: ', e.args, '\033[m')
