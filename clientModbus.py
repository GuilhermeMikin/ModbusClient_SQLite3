from pyModbusTCP import client
from pyModbusTCP.client import ModbusClient
from time import sleep
import time
import datetime
import sqlite3
from threading import Lock


class ClienteMODBUS():
    """
    Classe Cliente MODBUS
    """

    def __init__(self, server_ip, porta, device_id, scan_time=0.5, valor=0, dbpath="C:\database3.db"):
        """
        Construtor;
        """
        self._cliente = ModbusClient(host=server_ip, port=porta, unit_id=device_id)
        self._scan_time = scan_time
        self._server_ip = server_ip
        self._device_id = device_id
        self._port = porta
        
        self._dbpath = dbpath
        self._valor = valor
        self._con = sqlite3.connect(self._dbpath)
        self._cursor = self._con.cursor()

    def atendimento(self):
        """
        Método para atendimento do usuário
        """
        try:
            self._cliente.open()
            print('\n\033[33m --> Cliente Modbus conectado..\033[m\n')

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
                    self.createTable()
                    print('\nQual tipo de dado deseja ler?')
                    print("1- Coil Status \n2- Input Status \n3- Holding Register \n4- Input Register")
                    while True:
                        tipo = int(input("Type: "))
                        if tipo > 4:
                            print('\033[31mDigite um tipo válido..\033[m')
                            sleep(0.8)
                        else:
                            break

                    if tipo == 3 or tipo == 4: 
                        while True:
                            val = int(input("\n1- Decimal \n2- Floating Point \n3- Float Swapped \nLeitura: "))
                            if val > 3:
                                print('\033[31mDigite um tipo válido..\033[m')
                                sleep(0.8)
                            else:
                                break
                        if val == 1: #valores INTEGER
                            addr = int(input(f'\nAddress: '))
                            leng = int(input(f'Length: '))
                            nvezes = input('Quantidade de leituras: ')
                            print('\nComeçando leitura Decimal..\n')
                            sleep(1)
                            try:
                                for i in range(0, int(nvezes)):
                                    print(f'\033[33mLeitura {i + 1}:\033[m')
                                    self.lerDado(int(tipo), int(addr), leng)
                                    sleep(self._scan_time)
                                print('\nValores lidos e inseridos no DB com sucesso!!\n')
                                sleep(0.8)
                            except Exception as e:
                                print('\033[31mERRO: ', e.args, '\033[m')
                                try:
                                    sleep(0.5)
                                    print('\033[33m\nSegunda tentativa..\033[m')
                                    if not self._cliente.is_open():
                                        self._cliente.open()
                                    sleep(2)
                                    for i in range(0, int(nvezes)):
                                        print(f'\033[33mLeitura {i + 1}:\033[m')
                                        self.lerDado(int(tipo), int(addr), leng)
                                        sleep(self._scan_time)
                                    print('\nValores lidos e inseridos no DB com sucesso!!\n')
                                    sleep(0.8)
                                except Exception as e:
                                    print('\033[31mERRO: ', e.args, '\033[m')
                                    print('\nO Cliente não conseguiu receber uma resposta.. \nVoltando ao menu..\n\n')
                                    sleep(1.5)

                        elif val == 2: #valores FLOAT
                            addr = input(f'\nAddress: ')
                            leng = int(input(f'Length: '))
                            nvezes = input('Quantidade de leituras: ')
                            print('\nComeçando leitura FLOAT..\n')
                            sleep(1)
                            try:
                                for i in range(0, int(nvezes)):
                                    print(f'\033[33mLeitura {i + 1}:\033[m')
                                    self.lerDadoFloat(int(tipo), int(addr), leng)
                                    sleep(self._scan_time)
                                print('\nValores lidos e inseridos no DB com sucesso!!\n')
                                sleep(0.8)
                            except Exception as e:
                                print('\033[31mERRO: ', e.args, '\033[m\n')
                                print('O Cliente não conseguiu receber uma resposta.. \nVoltando ao menu..\n\n')
                                sleep(1.5)

                        elif val == 3: #valores FLOAT SWAPPED 
                            addr = input(f'\nAddress: ')
                            leng = int(input(f'Length: '))
                            nvezes = input('Quantidade de leituras: ')
                            print('\nComeçando leitura FLOAT SWAPPED..\n')
                            sleep(1)
                            try:
                                for i in range(0, int(nvezes)):
                                    print(f'\033[33mLeitura {i + 1}:\033[m')
                                    self.lerDadoFloatSwapped(int(tipo), int(addr), leng)
                                    sleep(self._scan_time)
                                print('\nValores lidos e inseridos no DB com sucesso!!\n')
                                sleep(0.8)
                            except Exception as e:
                                print('\033[31mERRO: ', e.args, '\033[m\n')
                                print('O Cliente não conseguiu receber uma resposta.. \nVoltando ao menu..\n\n')
                                sleep(1.5)

                        else:
                            sleep(0.3)
                            print('\033[31mSeleção inválida..\033[m\n')
                            sleep(0.7)

                    else:
                        addr = input(f'\nAddress: ')
                        leng = int(input(f'Length: '))
                        nvezes = input('Quantidade de leituras: ')
                        print('\nComeçando leitura..\n')
                        sleep(1)
                        try:
                            for i in range(0, int(nvezes)):
                                print(f'\033[33mLeitura {i + 1}:\033[m')
                                self.lerDado(int(tipo), int(addr), leng)
                                sleep(self._scan_time)
                            print('\nValores lidos e inseridos no DB com sucesso!!\n')
                            sleep(0.8)
                        except Exception as e:
                            print('\033[31mERRO: ', e.args, '\033[m\n')
                            print('O Cliente não conseguiu receber uma resposta.. \nVoltando ao menu..\n\n')
                            sleep(1.5)

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
                    try:
                        print('\nEscrevendo..')
                        sleep(1.5)
                        self.escreveDado(int(tipo), int(addr), valor)
                    except Exception as e:
                        print('\033[31mERRO: ', e.args, '\033[m')
                        print('\nO Cliente não conseguiu escrever.. \nVoltando ao menu..\n\n')
                        sleep(1.5)

                elif sel == '3':
                    print('\nQual tipo de configuração deseja fazer? \n1- Endereço IP \n2- Porta TCP \n3- Device ID \n4- ScanTime \n5- Voltar')
                    config = int(input("Configuração: "))
                    if config == 1:
                        ipserv = str(input('Novo endereço IP: '))
                        try:
                            self._server_ip = ipserv
                        except Exception as e:
                            print('\033[31mERRO: ', e.args, '\033[m')
                            print('\nNão foi possível alterar o endereço IP.. \nVoltando ao menu..\n\n')
                            sleep(0.5)
                    elif config == 2:
                        porttcp = input('Nova porta TCP: ')
                        try:
                            self._port = int(porttcp)
                        except Exception as e:
                            print('\033[31mERRO: ', e.args, '\033[m')
                            print('\nNão foi possível alterar a porta.. \nVoltando ao menu..\n\n')
                            sleep(0.5)
                    elif config == 3:
                        iddevice = input('Novo device ID: ')
                        try:
                            self._device_id = int(iddevice)
                        except Exception as e:
                            print('\033[31mERRO: ', e.args, '\033[m')
                            print('\nNão foi possível alterar o ID do device.. \nVoltando ao menu..\n\n')
                            sleep(0.5)
                    elif config == 4:
                        scant = input('Novo tempo de varredura [s]: ')
                        try:    
                            self._scan_time = float(scant)
                        except Exception as e:
                            print('\033[31mERRO: ', e.args, '\033[m')
                            print('\nNão foi possível alterar o tempo de varredura.. \nVoltando ao menu..\n\n')
                            sleep(0.5)
                    elif config == 5:
                        print('Voltando ao menu inicial..')
                    else:
                        sleep(0.3)
                        print('\033[31mSeleção inválida..\033[m\n')
                        sleep(0.7)

                elif sel == '4':
                    sleep(0.2)
                    print('\n\033[32mFechando sistema..\033[m')
                    sleep(0.5)
                    self._cliente.close()
                    atendimento = False

                else:
                    sleep(0.3)
                    print('\033[31mSeleção inválida..\033[m\n')
                    sleep(0.7)
        except Exception as e:
            print('\033[31mERRO: ', e.args, '\033[m')


    def createTable(self):
        """
        Método que cria a tabela para armazenamento dos dados, caso ela não exista
        """
        try:
            sql_str = f"""
            CREATE TABLE IF NOT EXISTS pointValues (
                ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Endereço NUMERIC, Tipo TEXT, Valor REAL, TimeStamp1 TEXT NOT NULL)
                """
            self._cursor.execute(sql_str)
            self._con.commit()
        except Exception as e:
            print('\033[31mERRO: ', e.args, '\033[m')


    def inserirDB(self, addrs, tipo, value):
        """
        Método para inserção dos dados no DB
        """
        try:
            date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime("%Y-%m-%d %H:%M:%S"))
            str_values = f"{addrs}, {tipo}, {value} , '{date}'"
            sql_str = f'INSERT INTO pointValues (Endereço, Tipo, Valor, TimeStamp1) VALUES ({str_values})'
            self._cursor.execute(sql_str)
            self._con.commit()
        except Exception as e:
            print('\033[31mERRO: ', e.args, '\033[m')

    def lerDado(self, tipo, addr, leng=1):
        """
        Método para leitura MODBUS
        """
        if tipo == 1:
            co = self._cliente.read_coils(addr - 1, leng)
            ic = 0
            while ic <= leng:
                if ic == leng:
                    break
                else:
                    value = co[0 + ic]
                    ic += 1
                    print(value)
                    if value == True:
                        value = 1
                    else:
                        value = 0
                    self.inserirDB(addrs=(00000+addr+ic-1), tipo="'Coil Status'",value=value)
            return 

        elif tipo == 2:
            di = self._cliente.read_discrete_inputs(addr - 1, leng)
            idi = 0
            while idi <= leng:
                if idi == leng:
                    break
                else:
                    value = di[0 + idi]
                    idi += 1
                    print(value)
                    self.inserirDB(addrs=(10000+addr+idi-1), tipo="'Input Status'",value=value)
            return 

        elif tipo == 3:
            hr = self._cliente.read_holding_registers(addr - 1, leng)
            sleep(1)
            ihr = 0
            while ihr <= leng:
                if ihr == leng:
                    break
                else:
                    value = hr[0+ihr]
                    ihr += 1
                    print(value)
                    self.inserirDB(addrs=(40000+addr+ihr-1), tipo="'Holding Register'",value=value)
            return 

        elif tipo == 4:
            ir = self._cliente.read_input_registers(addr - 1, leng)
            iir = 0
            while iir <= leng:
                if iir == leng:
                    break
                else:
                    value = ir[0 + iir]
                    iir += 1
                    print(value)
                    self.inserirDB(addrs=(30000+addr+iir-1), tipo="'Input Register'",value=value)
            return 

        else:
            print('Tipo de leitura inválido..')

    def lerDadoFloat(self, tipo, addr, leng):
        """
        Método para leitura FLOAT MODBUS
        """
        i = 0
        g = 0
        e1 = []
        while i < leng:
            if tipo == 3:
                i1 = self._cliente.read_holding_registers(addr - 1 + g, 2)
                tipore = "'Holding Register'"
                ende = 40000
            elif tipo == 4:
                i1 = self._cliente.read_input_registers(addr - 1 + g, 2)
                tipore = "'Input Register'"
                ende = 30000
            else:
                print('Tipo inválido..')
            for x in i1:
                x = bin(x).lstrip("0b")
                e1.insert(0 + g, x)
            i += 1
            g += 2
        e = 0
        while e <= leng:
            e2 = ''
            for x in e1:
                e2 = str(f'{e2}{x.rjust(16, "0")} ')
            e += 1
        b2 = str(f'{e2}')
        e3 = b2.split()
        y = 0
        while y < len(e3):
            ieee = f'{e3[0+y]}{e3[1+y]}'
            sign = int(ieee[0])
            expo = str(ieee[1:9])
            expodec = 0
            expopot = 7
            for i in range(8):
                expodec = expodec + (int(expo[i]) * (2**expopot))
                expopot -= 1
            mant = str(ieee[9:])
            mantdec = 0
            mantpot = -1
            for i in range(23):
                mantdec = mantdec + (int(mant[i]) * (2 ** mantpot))
                mantpot -= 1
            value = ((-1)**sign)*(1+mantdec)*2**(expodec-127)
            print(f'{round(value, 3)}')
            y += 2
            self.inserirDB(addrs=(ende+addr+y-2), tipo=tipore, value=round(value, 3))
        return

    def lerDadoFloatSwapped(self, tipo, addr, leng):
        """
        Método para leitura FLOAT SWAPPED MODBUS
        """
        i = 0
        g = 0
        e1 = []
        while i < leng:
            if tipo == 3:
                i1 = self._cliente.read_holding_registers(addr - 1 + g, 2)
                tipore = "'Holding Register'"
                ende = 40000
            elif tipo == 4:
                i1 = self._cliente.read_input_registers(addr - 1 + g, 2)
                tipore = "'Input Register'"
                ende = 30000
            else:
                print('Tipo inválido..')
            i2 = i1[::-1]
            for x in i2:
                x = bin(x).lstrip("0b")
                e1.insert(0 + g, x)
            i += 1
            g += 2
        e = 0
        while e <= leng:
            e2 = ''
            for x in e1:
                e2 = str(f'{e2}{x.rjust(16, "0")} ')
            e += 1
        b2 = str(f'{e2}')
        e3 = b2.split()
        y = 0
        while y < len(e3):
            ieee = f'{e3[0+y]}{e3[1+y]}'
            sign = int(ieee[0])
            expo = str(ieee[1:9])
            expodec = 0
            expopot = 7
            for i in range(8):
                expodec = expodec + (int(expo[i]) * (2**expopot))
                expopot -= 1
            mant = str(ieee[9:])
            mantdec = 0
            mantpot = -1
            for i in range(23):
                mantdec = mantdec + (int(mant[i]) * (2 ** mantpot))
                mantpot -= 1
            value = ((-1)**sign)*(1+mantdec)*2**(expodec-127)
            print(f'{round(value, 3)}')
            y += 2
            self.inserirDB(addrs=(ende+addr+y-2), tipo=tipore, value=round(value, 3))
        return


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

    
