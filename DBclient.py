# import sqlite3
# from threading import Lock
# import time
# import datetime
#
#
# class DBclient():
#     """
#     Classe para manipulação
#     """
#
#     def __init__(self, dbpath, tags, tablename='dataTable'):
#         """
#         Construtor
#         :param dbpatth:
#         :param tags:
#         :param tablename:
#         """
#         self._dbpath = dbpath
#         self._tablename = tablename
#         self._con = sqlite3.connect(self._dbpath, check_same_thread=False)
#         self._cursor = self._con.cursor()
#         self._col_names = tags.keys()
#         self._lock = Lock()
#         self.createTable()
#
#     def __del__(self):
#         self._con.close()
#
#     def createTable(self):
#         """
#         Método que cria a tabela para armazenamento dos dados caso ela não exista
#         :return:
#         """
#         try:
#             sql_str = f"""
#             CREATE TABLE IF NOT EXISTS {self._tablename} (
#                 id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#                 timestamp TEXT NOT NULL,)
#                 """
#             for n in self._col_names:
#                 sql_str += f'{n} REAL,'
#
#             sql_str = sql_str[:-1]
#             sql_str += ');'
#             self._lock.acquire()
#             self._cursor.execute(sql_str)
#             self._con.commit()
#             self._lock.release()
#         except Exception as e:
#             print('\033[31mERRO: ', e.args, '\033[m')
#
#         def inserirDB(self, data):
#             """
#             Método para inserção dos dados no BD
#             :param self:
#             :param data:
#             :return:
#             """
#             try:
#                 self._lock.acquire()
#                 timestamp = str(data['timestamp'])
#                 str_cols = 'timestamp,' + ','join(data['values'].keys())
#                 str_values = f"'{timestamp}'," + ','.join([str('values'[k]) for k in data['values'].key()])
#                 sql_str = f'INSERT INTO {self.tablename} ({str_cols}) VALUES ({str_values});'
#                 self._cursor.execute(sql_str)
#                 self._con.commmit()
#                 self._lock.release()
#             except Exception as e:
#                 print('\033[31mERRO: ', e.args, '\033[m')
#
#         def selectData(self, cols, init_t, final_t):
#             """
#             Método que realiza a busca no DB entre 2 horários especificados
#             :param self:
#             :param cols:
#             :param init_t:
#             :param final_t:
#             :return:
#             """
#






# #conn = sqlite3.connect('databasesql')
# #cursor = conn.cursor()
#
# date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime("%Y-%m-%d %H:%M:%S"))
#
# file = open("datevalue.txt","w")
# file.write(date)
# file.close()
#
# # sql = 'SELECT * FROM pointvalues WHERE ID = ?'
#
# def creat_table():
#      cursor.execute("CREATE TABLE IF NOT EXISTS POINTVALUES (ID integer, valor real, timestamp1 blob)")
#
#
# def inserir(ID, valor=0):
#     #cursor.execute("INSERT INTO pointvalues VALUES (111, '2021-05-3')")
#     date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime("%Y-%m-%d %H:%M:%S"))
#     cursor.execute('INSERT INTO pointvalues (ID, valor, timestamp1) VALUES (?, ?,?)',(ID, valor, date))
#     conn.commit()
#
#
# def lerTudo():
#     cursor.execute("SELECT * FROM pointvalues")
#     print(cursor.fetchall())
#

# msa_drivers = [x for x in pyodbc.drivers()]
# print(f'MS-Access Drivers: {msa_drivers}')
