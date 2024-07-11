from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
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
    descripciones = []

    for producto in productos:
        nombre = producto.find('h2', class_="ui-search-item__title")
        nombre = nombre.text.strip() if nombre else "Nombre no disponible"
        nombres.append(nombre)

        precio = producto.find('span', class_="andes-money-amount__fraction")
        precio = precio.text.strip() if precio else "Precio no disponible"
        precio = precio.replace(",", "")
        precios.append(float(precio))

        enlace = producto.find('a', class_="ui-search-item__group__element ui-search-link__title-card ui-search-link")
        enlace = enlace['href'] if enlace else "Enlace no disponible"
        enlaces.append(enlace)

        descripcion = producto.find('p', class_="ui-search-item__description")
        descripcion = descripcion.text.strip() if descripcion else "Descripción no disponible"
        descripciones.append(descripcion)

    # Dataframe con los datos extraídos
    df = pd.DataFrame({
        'Nombre': nombres,
        'Precio': precios,
        'Enlace': enlaces,
        'Descripción': descripciones
    })

    # Mostrar información de los productos (en Excel)
    writer = pd.ExcelWriter('productos.xlsx')
    df.to_excel(writer, sheet_name='Productos')

    # Cálculo del precio promedio
    precio_promedio = df['Precio'].mean()
    print(f"\nPrecio promedio: ${precio_promedio:.2f}")

    # Generación del gráfico de distribución de precios
    plt.figure(figsize=(10, 6))
    plt.hist(df['Precio'], bins=20, edgecolor='black')
    plt.xlabel('Precio')
    plt.ylabel('Frecuencia')
    plt.title('Distribución de precios de iPhone 13 Pro')
    plt.grid(True)
    plt.savefig('distribucion_precios.png')
    print("Gráfico de distribución de precios generado en 'distribucion_precios.png'")

    # Exportación del DataFrame a Excel
    writer.save()
    print("Datos exportados correctamente a productos.xlsx")
    print("Termino de scrapear la página")

else:
    print("Error al obtener la información de la página")
