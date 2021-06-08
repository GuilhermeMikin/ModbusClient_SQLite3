from clientModbus import ClienteMODBUS

dbpath = "C:\\Users\\Guilherme B. Lopes\\Documents\\GitHub\\pyModbusClient\\DB\\database.db"

# c = ClienteMODBUS('192.168.100.180', 502, dbpath=dbpath)
c = ClienteMODBUS('localhost', 502, 1, dbpath=dbpath)
c.atendimento()

