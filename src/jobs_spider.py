import requests
import pandas as pd

# Endpoint da API
url = "https://remotive.com/api/remote-jobs"

# Filtro por categoria (ex: Data, Software Development etc.)
params = {
    "category": "data-science"
}

# Requisição dos dados do site
response = requests.get(url, params=params)
data = response.json()

# Extrair lista de vagas
jobs = data.get("jobs", [])

df = pd.DataFrame(jobs)

# Exibir as primeiras colunas uteis
print(df[["title", "company_name", "category", "job_type", "url"]].head())

# salvar CSV
df.to_csv("data/remotive_jobs_data.csv", index=False)
