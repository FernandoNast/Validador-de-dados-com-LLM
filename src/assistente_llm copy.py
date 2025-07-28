import pandas as pd
import requests
import time

# Carrega seu CSV validado
df = pd.read_csv("./data/remotive_validado.csv")

# Função para analisar descrição com LLaMA
def detectar_erros(texto):
    prompt = f"""
    Você é um validador de qualidade textual para descrições de vagas. Analise o seguinte texto e aponte **no máximo 3 erros** de linguagem, formatação, coerência ou estrutura. 
    Responda apenas com os erros encontrados, se houver. 
    Se estiver tudo certo, diga 'Sem erros detectados', do contrário, termine sua análise com a frase "essa foi a analise".
    Responda com **textos em portugues**.

    Texto:
    \"\"\"{texto}\"\"\"
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma3",
            "prompt": prompt,
            "stream": False
        }
    )
    # print("Resposta da API:", response.json())  # debug
    return response.json().get("response", "").strip()

# print(detectar_erros(df["description"].iloc[0]))
# Aplica ao primeiro exemplo do dataset (ou pode iterar)

inicio = time.time()

df["erros_textuais"] = df["description"].apply(detectar_erros)

# Salva resultado
df.to_csv("./data/remotive_erros_detectados.csv", index=False)

print("Análise concluída! Resultados salvos em 'remotive_erros_detectados.csv'")
fim = time.time()
tempo_exec = fim - inicio
print(f"\nExecução levou {tempo_exec:.2f}s")