"""util.py
'yyyy-mm-dd hh:ii:ss'
'dd/mm/yyyy hh:ii:ss'
def data_to_mysql(data: str):
    pass
def mysql_to_data(data: str):"""

def data_to_mysql (data: str):
    print (data)
    data_formatada = data.split(" ") #transforma em um array, com dois elementos.
    print (data_formatada)
    data_formatada = data_formatada[0].split("/")
     print (data_formatada)
    
    