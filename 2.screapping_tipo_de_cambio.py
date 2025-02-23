import requests
from bs4 import BeautifulSoup
from datetime import datetime  # Importa el módulo datetime


url= 'https://cuantoestaeldolar.pe/'

fecha_hora_actual = datetime.now() # Obtiene la fecha y hora actual 

fecha_hora_formateada = fecha_hora_actual.strftime("%Y-%m-%d %H:%M") # Formatea la fecha y hora

print("Fecha y hora: ", fecha_hora_formateada) # Imprime la fecha y hora

response = requests.get(url) # Realiza una petición GET a la página web

if response.status_code == 200: 
    soup = BeautifulSoup(response.text, 'html.parser')

    # Obtiene el tipo de cambio compras y ventas
    empresas_all = soup.find_all('div',class_='ExchangeHouseItem_item_col__gudqq')
    #print(empresas_all[0])

    # Obtiene el tipo de cambio compras
    div_buy = empresas_all[0].find('div',class_='ValueCurrency_content_buy__Z9pSf')
    buy = div_buy.find('p').getText()

    # Obtiene el tipo de cambio ventas
    div_sell = empresas_all[0].find('div',class_='ValueCurrency_content_sale__fdX_P') # Obtiene el
    sell = div_sell.find('p').getText() # Obtiene el texto del tag p

    # Obtiene el nombre de la empresa
    img = empresas_all[0].find('img')
    compamy = img['alt']

    print("Empresa: " + compamy, "Compra: ",buy, " | Venta: ",sell) # Tipo de cambio

#Los siguientes pasos es la generacion de listas para generar un archivo csv o dataframe