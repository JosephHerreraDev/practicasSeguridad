from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://listado.mercadolibre.com.mx/iphone-13-pro#D[A:iphone%2013%20pro]"

response = requests.get(url)

if response.status_code == 200:
   print("Inicio a scrapear la página")
   soup = BeautifulSoup(response.text, 'html.parser')

   productos = soup.find_all('div', class_="ui-search-result__wrapper")
   
   nombres = []
   precios = []
   enlaces = []

   for producto in productos:
       nombre = producto.find('h2', class_="ui-search-item__title")
       nombre = nombre.text.strip() if nombre else "Nombre no disponible"
       nombres.append(nombre)

       precio = producto.find('span', class_="andes-money-amount__fraction")
       precio = precio.text.strip() if precio else "Precio no disponible"
       precios.append(precio)

       enlace = producto.find('a', class_="ui-search-item__group__element ui-search-link__title-card ui-search-link")
       enlace = enlace['href'] if enlace else "Enlace no disponible"
       enlaces.append(enlace)

       # Dataframe con los datos extraídos
       df = pd.DataFrame({
           'Nombre': nombres,
           'Precio': precios,
           'Enlace': enlaces
       })

       df.to_excel('productos.xlsx', index=False)
       print("Datos exportados correctamente a productos.xlsx")
   print("Termino de scrapear la página")
else:
   print("Error al obtener la información de la página")
