import pandas as pd
from textblob import TextBlob
import requests
from bs4 import BeautifulSoup

def extract_and_analyze_reviews(url):
  response = requests.get(url)

  if response.status_code == 200:
    print("Obtenido correctamente los datos de la pagina")
    soup = BeautifulSoup(response.text, 'html.parser')

    reviews = soup.find_all('div', class_="a-fixed-right-grid-col a-col-left")
    review_titles = []
    sentiments = []

    for review in reviews:
      titulo = review.find('span', class_="a-size-base review-text review-text-content")
      if titulo:
        cleaned_title = titulo.text.strip()
        review_titles.append(cleaned_title)

        sentiment = 'Positivo' if TextBlob(cleaned_title).sentiment.polarity > 0 else (
            'Neutral' if TextBlob(cleaned_title).sentiment.polarity == 0 else 'Negativo')
        sentiments.append(sentiment)

  else:
    print(f"Unexpected status code: {response.status_code}")
    return pd.DataFrame()

  df = pd.DataFrame({'Titulo': review_titles, 'Sentimiento': sentiments})
  return df

url = "https://www.amazon.com.mx/port%C3%A1til-DOXUNGO-antirrobo-aud%C3%ADfonos-pulgadas/product-reviews/B0788FS5PJ/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
df = extract_and_analyze_reviews(url)

if not df.empty:
  df.to_excel('comentarios_sentimientos.xlsx', index=False)
  print("Datos guardados en el archivo comentarios_sentimientos.xlsx")
else:
  print("No se encontraron reseñas o hubo un error al procesar la pagina")
