import requests
import pandas as pd

# Endpoint da API
url = "https://remotive.com/api/remote-jobs"

# Filtro por categoria (ex: Data, Software Development etc.)
params = {
    "category": "data"
}

# Requisição
response = requests.get(url, params=params)
data = response.json()

# Extrair lista de vagas
jobs = data.get("jobs", [])

# Converter para DataFrame
df = pd.DataFrame(jobs)

# Exibir as primeiras colunas úteis
print(df[["title", "company_name", "category", "job_type", "url"]].head())

# (Opcional) Salvar como CSV
df.to_csv("scraper/remotive_jobs_data.csv", index=False)
