from clientModbus import ClienteMODBUS

dbpath = "C:\\Users\\Guilherme B. Lopes\\Documents\\GitHub\\pyModbusClient\\DB\\database.db"

c = ClienteMODBUS('192.168.1.5', 502, dbpath=dbpath)
c.atendimento()

