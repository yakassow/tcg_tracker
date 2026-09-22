# TCG Market Tracker: Automated API Data Pipeline 

> **Note:** This repository demonstrates a practical data engineering workflow, focusing on data extraction, transformation, and load (ETL) processes using Python.

## Project Overview
Monitoring the secondary market for Trading Card Games (TCGs) requires processing unhandled JSON data into structured formats. This project implements an automated pipeline that queries a public REST API for Yu-Gi-Oh! card data, extracts relevant pricing metrics, and cleans the dataset using `pandas`. 

The output is a structured CSV file, optimized to be ingested by reporting tools like **Power BI** or **Tableau** for interactive dashboarding.

## Tech Stack & Tools
* **Language:** Python
* **Data Processing:** `pandas` for data structuring and cleansing
* **Network & API:** `requests` for REST API integration
* **Output:** `.csv` generation for downstream data visualization

## The Pipeline 
1. **API Integration:** Connects to the public YGOPRODeck REST API.
2. **Data Extraction:** Parses nested JSON responses to isolate specific market values (e.g., Cardmarket and TCGPlayer prices).
3. **Data Cleansing (Pandas):** Structures the raw data into a relational DataFrame, normalizes data types (floats/strings), and appends a timestamp.
4. **Export:** Saves the cleaned, validated dataset ready for business intelligence tools.
