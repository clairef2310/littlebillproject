from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

# URL de l'API externe qui renvoie la liste des clients au format JSON
api_url = "https://techtest.hiboutik.com/docapi/json/clients"

# API va retourner la liste des clients enregistrés dans le logiciel de caisse pour un “nom” donné
@app.get("/clients/")
async def get_clients_by_name(nom: str):
    try:

        headers = {
            "Authorization": "2OZ58K8MYZV56SFA59NG2PQ2HYW4C6280IT",
            "X-User-Email": "techtest@gmail.com",
            "User-Agent": "techtest"
        }


        params = {
            "nom": nom
        }


        response = requests.get(api_url, headers=headers, params=params)
        response.raise_for_status()

        clients_data = response.json()


        if "clients" in clients_data:

            matched_clients = clients_data["clients"]
            return matched_clients
        else:

            return []

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail="Impossible de récupérer les données des clients depuis l'API.")


@app.get("/ventes/{client_id}")
async def get_ventes_by_client(client_id: int):
    try:

        headers = {
            "Authorization": "2OZ58K8MYZV56SFA59NG2PQ2HYW4C6280IT",
            "X-User-Email": "techtest@gmail.com",  # Remplacez par votre adresse e-mail
            "User-Agent": "techtest"
        }
        # Paramètres pour la requête GET, en incluant l'identifiant du client
        params = {
            "client_id": client_id
        }

        # Appel à l'API externe pour récupérer la liste des ventes pour le client donné
        response = requests.get(api_url, headers=headers, params=params)
        response.raise_for_status()  # Vérifier si la requête s'est bien déroulée

        # Récupérer les données JSON de la réponse
        ventes_data = response.json()

        # Assurez-vous que la réponse contient des données de ventes
        if "ventes" in ventes_data:
            # La clé "ventes" contient la liste des ventes pour le client donné
            ventes_client = ventes_data["ventes"]
            return ventes_client
        else:
            # Si la clé "ventes" n'est pas présente, cela signifie qu'il n'y a pas de ventes pour ce client
            return []

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail="Impossible de récupérer les données des ventes depuis l'API.")
