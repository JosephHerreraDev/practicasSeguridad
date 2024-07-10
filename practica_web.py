import requests
from bs4 import BeautifulSoup

url = "https://listado.mercadolibre.com.mx/macbook#D[A:macbook]"

response = requests.get(url)

if response.status_code == 200:
    print("Se obtuvo la informacion correcta de la pagina")
    soup = BeautifulSoup(response.text, 'html.parser')
    productos = soup.find_all('div', class_ = "andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16")
    print(len(productos))

    for producto in productos:
        titulo = producto.find('h2', class_ = "ui-search-item__title")
        if titulo:
            print(titulo.text.strip())
else:
    print("No se pudo obtener la informacion de la pagina")


