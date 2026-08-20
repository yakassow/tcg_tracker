# TCG Market & Meta Tracker 🃏📊

> **Note:** This repository is currently being set up to organize and consolidate various local Python scripts and data analysis experiments I have been working on. 

## 📌 Project Overview
This project focuses on building an automated data pipeline to analyze the secondary market and meta-game representation of Trading Card Games (specifically Yu-Gi-Oh!). The goal is to extract raw data via REST APIs, clean and transform it using Python, and visualize market trends and archetype distributions (e.g., Phantom Knights) in a Power BI dashboard.

## 🛠️ Tech Stack & Tools
* **Data Extraction:** Python (Requests, JSON parsing)
* **Data Cleansing & Transformation:** Python (Pandas), Excel / Power Query
* **Data Visualization:** Power BI, DAX
* **Version Control:** Git / GitHub

## 🗄️ Data Sources
* **YGOPRODeck API:** For extracting comprehensive card data, sets, and current market prices (TCGplayer, Cardmarket).
* **Local CSVs:** Aggregated tournament results and meta distributions.

## 🚀 Key Features (In Development)
1. **API Integration:** Automated fetching of 10,000+ card records.
2. **Data Quality Control:** Handling missing values, standardizing naming conventions, and deduplicating database entries.
3. **Price Tracking:** Monitoring daily/weekly price fluctuations for specific competitive staples.
4. **Dashboarding:** Creating interactive visuals to correlate a card's tournament representation with its market value.

## 🚧 Current Status
*Work in Progress.* I am currently migrating the local data extraction scripts to this repository and setting up the data model for the final Power BI dashboard.
