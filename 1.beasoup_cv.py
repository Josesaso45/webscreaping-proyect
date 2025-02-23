import requests

from bs4 import BeautifulSoup

url= 'https://josesaso45.github.io/'

response = requests.get(url) # Realiza una petición GET a la página web

print(response.text) # Imprime el contenido HTML de la página

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser') # Parsea el contenido HTML de la página
    
    # Obtiene el título de la página
    title = soup.title
    print(title.get_text()) # Imprime el título de la página sin las etiquetas

    # Obtiene el contenido del body de la página
    body = soup.body
    print(body) # Imprime el body de la página
    print(body.get_text()) # Imprime el contenido del body sin las etiquetas

    h2_all = soup.find_all('h2') # Obtiene todas las etiquetas h2 de la página
    print(h2_all) # Imprime todas las etiquetas h2 de la página
    print(h2_all[2].get_text()) # Imprime el contenido de la primera etiqueta h2

    div_all = soup.find_all('div') # Obtiene todas las etiquetas div de la página
    print(div_all) # Imprime todas las etiquetas div de la página
    print(div_all[0].get_text()) # Imprime el contenido de la primera etiqueta div

    #Busqueda de elementos por etquetas y clases

    first_div = soup.find('div', class_='section') # Obtiene la primera etiqueta div con la clase 'first'
    print(first_div.get_text()) # Imprime el contenido de la primera etiqueta div con la clase 'first'
    print("jose")

    div_section = soup.find_all('div', class_='section') # Obtiene todas las etiquetas div con la clase 'section'
    print(div_section)

    #Busqueda de elementos por atributos

    link = soup.find('a', href= True) # Obtiene la primera etiqueta a con el atributo href
    print(link)

    text = soup.find_all('p', text= True) # Obtiene todas las etiquetas p con el atributo text
    print(text)

    html = str(soup) # Convierte el objeto BeautifulSoup a un string

    html_bonito = soup.prettify() # Convierte el objeto BeautifulSoup a un string con formato

    print(html_bonito) # Imprime el contenido HTML de la página con formato