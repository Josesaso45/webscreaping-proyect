import requests

from bs4 import BeautifulSoup

url= 'https://cuantoestaeldolar.pe/'

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

    print('Compra: ',buy, " | Venta: ",sell)