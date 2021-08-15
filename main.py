from clientModbus import ClienteMODBUS

dbpath = "C:\\Users\\mikin\\GitHubRepository\\pyModbusClient\\DB\\database1.db"

c = ClienteMODBUS('127.0.0.1', 502, 1, dbpath=dbpath)
c.atendimento()

