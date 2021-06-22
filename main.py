from clientModbus import ClienteMODBUS

dbpath = "C:\\Users\\Guilherme B. Lopes\\Documents\\GitHub\\pyModbusClient\\DB\\database.db"

c = ClienteMODBUS('127.0.0.1', 502, 1, dbpath=dbpath)
c.atendimento()

