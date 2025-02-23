import requests
from bs4 import BeautifulSoup
from datetime import datetime  # Importa el módulo datetime


url= 'https://cuantoestaeldolar.pe/'

fecha_hora_actual = datetime.now() # Obtiene la fecha y hora actual 

fecha_hora_formateada = fecha_hora_actual.strftime("%Y-%m-%d %H:%M") # Formatea la fecha y hora

print("Fecha y hora: ", fecha_hora_formateada) # Imprime la fecha y hora

response = requests.get(url) # Realiza una petición GET a la página web

companies = [] # Lista para almacenar las empresas
buys = [] # Lista para almacenar los precios de compra
sells = [] # Lista para almacenar los precios de venta
fecha_de_extraccion = [] # Lista para almacenar la fecha y hora de extracción

if response.status_code == 200: 
    soup = BeautifulSoup(response.text, 'html.parser')

    #Los siguientes pasos es la generacion de listas para generar un archivo csv o dataframe

    # Obtiene el tipo de cambio compras y ventas
    empresas_all = soup.find_all('div',class_='ExchangeHouseItem_item_col__gudqq')
    #print(empresas_all[0])

    for empresa in empresas_all:
        # Obtiene el tipo de cambio compras
        div_buy = empresa.find('div',class_='ValueCurrency_content_buy__Z9pSf')
        buy = div_buy.find('p').getText()
        buys.append(buy)

        # Obtiene el tipo de cambio ventas
        div_sell = empresa.find('div',class_='ValueCurrency_content_sale__fdX_P')
        sell = div_sell.find('p').getText()
        sells.append(sell)

        # Obtiene el nombre de la empresa
        img = empresa.find('img')
        company = img['alt']
        companies.append(company)   

        fecha_de_extraccion.append(fecha_hora_formateada)

# Imprime las empresas listadas para generar un archivo csv o dataframe
print(companies)


