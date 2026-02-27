import requests

BASE_URL = "https://us-central1-dlthub-analytics.cloudfunctions.net/data_engineering_zoomcamp_api"

# Liste des endpoints possibles à tester
endpoints = ["TEST"]

for endpoint in endpoints:
    url = f"{BASE_URL}/{endpoint}?page=1"
    try:
        response = requests.get(url)
        data = response.json()
        
        # Si c'est une liste, afficher la longueur
        if isinstance(data, list):
            print(f"✅ {endpoint}: {len(data)} enregistrements")
            if data:
                print(f"   Colonnes: {list(data[0].keys())}")
        else:
            print(f"⚠️  {endpoint}: Réponse non-liste")
    except Exception as e:
        print(f"❌ {endpoint}: Erreur - {e}")
    print()