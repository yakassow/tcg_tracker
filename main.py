import requests
import pandas as pd
from datetime import datetime

def fetch_and_clean_card_data(card_name):
    # 1. API-Anfrage an die öffentliche TCG Datenbank stellen (REST-API)
    url = f"https://db.ygoprodeck.com/api/v7/cardinfo.php?name={card_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        raw_data = response.json()
        
        # 2. Relevante JSON-Ebenen extrahieren
        card_info = raw_data['data'][0]
        prices = card_info['card_prices'][0]
        
        # 3. Daten in ein strukturiertes Pandas DataFrame transformieren
        df = pd.DataFrame([{
            "Card Name": card_info['name'],
            "Archetype": card_info.get('archetype', 'N/A'),
            "Cardmarket Price (€)": float(prices['cardmarket_price']),
            "TCGPlayer Price ($)": float(prices['tcgplayer_price']),
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }])
        
        return df
    else:
        print("Fehler beim Abrufen der API.")
        return None

# Pipeline ausführen mit einer Beispielkarte
if __name__ == "__main__":
    target_card = "The Phantom Knights of Rusty Bardiche"
    
    print("Starte Daten-Pipeline...")
    cleaned_df = fetch_and_clean_card_data(target_card)
    
    if cleaned_df is not None:
        print("\nBereinigter Datensatz:")
        print(cleaned_df)
        
        # 4. Export als CSV für Power BI / Excel
        filename = "tcg_market_data.csv"
        cleaned_df.to_csv(filename, index=False)
        print(f"\nErfolg: Daten wurden in '{filename}' gespeichert und sind bereit für Power BI.")
