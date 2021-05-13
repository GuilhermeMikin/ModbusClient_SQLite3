from pandas.io import html
import pandas as pd
import numpy as np

def criatabelahtml():
    """
    Método para escrita de tabela no HTML
    """
    try:
        colunas="Valor TimeStamp".split()
        linhas = "40001 40002 40003 40004 40005".split()
        dadoss = np.random.randint(390,410,len(colunas)*len(linhas)).reshape(len(linhas),len(colunas))
        tabela = pd.DataFrame(data=dadoss, index=linhas, columns=colunas)
        html = tabela.to_html()
        arq = open("index2.html", "w")
        arq.write("""
<html>
<head>
<title> Sist. Monitoramento </title> 
<meta charset="utf-8"/>
<HTA:APPLICATION
    APPLICATIONNAME="Modbus Client"
    ID="MyHTMLapplication"
    VERSION="1.0"
    BORDER="thick"
    INNERBORDER="yes"
    CAPTION="yes"
    SYSMENU="yes"
    MAXIMIZEBUTTON="yes"
    MINIMIZEBUTTON="yes"
    SCROLL="no"
    SCROLLFLAT="yes"
    SINGLEINSTANCE="no"
    CONTEXTMENU="no"
    />

<script language="VBScript" scr="SistMon.vbs">
</script>
</head>
        <img src="sismon.png" height="32%" width="100%"></>
        <br/><br>
        <h5> Um sistema integrado de monitoramento de variaveis de processo e indicadores de desempenho para otimizacao de linhas de producao em Industrias 4.0 </h5>
        <link rel="stylesheet" href="style.css">
<br>
</script>
<link rel="stylesheet" href="style.css">
</head>

<body bgcolor= #C1C1C1>
<!--Add your controls here--> 
        <nav id="menu">
            <ul>
                <li>
                    <a href="">Coil Status</a>
                </li>
                <li>
                    <a href="">Input Status</a>
                </li>
                <li>
                    <a href="">Holding Register</a>
                </li>
                <li>
                    <a href="">Input Register</a>
                </li>
            </ul>
        </nav>
            <center>
            <font size="5"><b> Cliente Modbus </b></font>
            
<br /><br>

<h3> 
<div id=PV> Esperando Leitura...  </div>
</h3> 

<br>
<Input ID="LerMDB"  onclick="LerMDB()" type="button" value="Iniciar Leitura">

<br /><br /><br>

<H3> 
</H3> 
                    """)
        arq.write(html)
        arq.write("""
<br /><br>
</center>
<br /><br /><br>
</body>
</html>
                    """)
        arq.close()
        print(dadoss)
    except Exception as e:
        print('\033[31mERRO: ', e.args, '\033[m')

criatabelahtml()
