from clientModbus import ClienteMODBUS
import time
import datetime

date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime("%Y-%m-%d %H:%M:%S"))

dbpath = "C:\\Users\\Guilherme B. Lopes\\Documents\\GitHub\\pyModbusClient\\DB\\database.db"

c = ClienteMODBUS('localhost', 502, date=date, dbpath=dbpath)
c.atendimento()


