import requests
import time
from concurrent.futures import ThreadPoolExecutor

url = "https://listado.mercadolibre.com.mx/macbook#D[A:macbook]"

def fetch_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Datos obtenidos correctamente")
        else:
            print("Error al obtener datos")
    except requests.exceptions.RequestException as e:
        print(f"Error en la petición: {e}")

# Numero de peticiones
num_requests = 100

# Ejecutamos peticiones
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(fetch_data, url) for i in range(num_requests)}

    # Espera a que todas las peticiones se completen
    for future in futures:
        future.result()
print("")