import requests
from bs4 import BeautifulSoup
import time

url="https://listado.mercadolibre.com.mx/macbook#D[A:macbook]"

for i in range(10):
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Pagina {i+1}: Datos obtenidos correctamente')
        soup = BeautifulSoup(response.text, 'html.parser')
    else:
        print(f'Pagina {i+1}: Error al obtener datos')

        time.sleep(1)