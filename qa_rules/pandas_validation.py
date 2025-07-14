import pandas as pd
from datetime import datetime, timedelta

# Função de validação por linha
def validar_vaga(row):
    score = 0
    motivos = []

    # 1. Título claro
    if any(term in row["title"].lower() for term in ["data", "scientist", "engineer", "analytics"]):
        score += 1
    else:
        motivos.append("Título genérico")

    # 2. Salário informado
    salario = str(row.get("salary", "")).lower()
    if salario and ("competitive" in salario or any(char.isdigit() for char in salario)):
        score += 1
    else:
        motivos.append("Sem salário claro")

    # 3. Descrição longa
    if len(str(row["description"])) > 500:
        score += 1
    else:
        motivos.append("Descrição curta")

    # 4. Link funcional
    if str(row["url"]).startswith("http"):
        score += 1
    else:
        motivos.append("Link inválido")

    # 5. Tags técnicas relevantes
    tags_str = str(row["tags"]).lower()
    if any(kw in tags_str for kw in ["python", "sql", "spark", "ml", "machine learning"]):
        score += 1
    else:
        motivos.append("Poucas techs relevantes")

    # 6. Publicação recente
    try:
        pub_date = pd.to_datetime(row["publication_date"])
        if pub_date >= datetime.now() - timedelta(days=15):
            score += 1
        else:
            motivos.append("Vaga antiga")
    except:
        motivos.append("Erro na data")

    return pd.Series({
        "pontuacao": score,
        "motivos": "; ".join(motivos)
    })

# Carrega o CSV
df = pd.read_csv("./scraper/data/remotive_jobs_data.csv")

# Aplica validação
df_validado = df.copy()
df_validado[["pontuacao", "motivos"]] = df_validado.apply(validar_vaga, axis=1)

# Vagas com nota 5 ou 6
df_top = df_validado[df_validado["pontuacao"] >= 5][
    ["title", "company_name", "salary", "pontuacao", "url"]
].sort_values(by="pontuacao", ascending=False)

df_top.reset_index(drop=True).head(10)

# (Opcional) Salvar o resultado
df_validado.to_csv("remotive_validado.csv", index=False)
