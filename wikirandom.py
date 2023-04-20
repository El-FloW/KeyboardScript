import requests
import json

def GetRandomInfo():
    # URL de l'article en question
    url = "https://fr.wikipedia.org/api/rest_v1/page/random/summary"

    # Effectuer une requête GET sur l'API de Wikipédia
    response = requests.get(url)

    # Extraire les données JSON de la réponse
    data = json.loads(response.text)

    # Récupérer le titre et l'extrait de l'article
    title = data["title"]
    extract = data["extract"]

    # Afficher le titre et l'extrait
    return extract