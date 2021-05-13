Sub sleep(Timesec)
    Set objwsh = CreateObject("WScript.Shell") 
    objwsh.Run "Timeout /T " & Timesec & " /nobreak" ,0 ,true
    Set objwsh = Nothing
End Sub

Sub ChangeValue(valor)
    PV.innerHTML = Cstr(valor)
End Sub

Sub LerMDB()

	cmd = "python clientModbus.py"
	
	for i = 1 to 10
		set objShell = CreateObject("WScript.Shell")
		objShell.Run cmd, 0, true
		Set objShell = Nothing
		
		Set objFileToRead = CreateObject("Scripting.FileSystemObject").OpenTextFile("modbusvalues.txt",1)
		strFileText = objFileToRead.ReadAll()
		objFileToRead.Close
		Set objFileToRead = Nothing
		ChangeValue strFileText
		InserirDB(strFileText)
		sleep 1
	next
End Sub

Sub LerMDB()
    VL.innerHTML = Cstr(" ")
    LerMDB
    VL.innerHTML = Cstr("Valores lidos e inseridos no Banco de Dados com sucesso!!")
End Sub

Sub InserirDB(valor)
	Dim Connection
    Dim Command
    Dim SQL
    
    cmd = "python pyScriptDB.py"
    set objShell = CreateObject("WScript.Shell")
	objShell.Run cmd, 0, true
	Set objShell = Nothing

    Set objDateToRead = CreateObject("Scripting.FileSystemObject").OpenTextFile("datevalue.txt",1)
	strDateText = objDateToRead.ReadAll()
	objDateToRead.Close
	Set objDateToRead = Nothing

    SQL = "INSERT INTO POINTVALUES (VALOR, TIMESTAMP1) VALUES ("& valor &", '"& strDateText &"')"

    Set Connection = CreateObject("ADODB.Connection")
    Set Command = CreateObject("ADODB.Command")

    'Abrindo a conexão com ODBC SQLite3:
    Connection.Open "DSN=SQLiteODBCServer"
    Command.ActiveConnection = Connection
    Command.CommandText = SQL
    Command.Execute

    Set Command = Nothing

    Connection.Close
    Set Connection = Nothing

End Sub

