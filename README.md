#  Validador Inteligente de Dados Scrapeados com LLM + Regras QA

Este projeto tem como objetivo construir um validador automatizado de descrições de vagas de emprego coletadas via scraping, utilizando um modelo de linguagem (LLM) local como o LLaMA ou DeepSeek e aplicando também regras tradicionais de qualidade de dados.

---

##  Objetivos

- Extrair dados de sites de vagas de emprego remotas (ex: Remotive).
- Limpar e validar campos como título, descrição, categoria etc.
- Detectar erros textuais e estruturais usando uma LLM.
- Exibir e revisar as validações em uma interface com Streamlit.

---

##  Tecnologias Utilizadas

- Python 3.10+
- Streamlit
- Pandas
- LLaMA / Ollama (ou outro modelo LLM local)
- HTML Parser (BeautifulSoup)
- API Remotive (https://remotive.com/api/remote-jobs)

---

## Estrutura do Projeto

```
.
├── app/
│   └── dash_streamlit.py              # Interface com Streamlit
├── data/
│   └── remotive_jobs_data.csv         # Dados brutos extraídos da API
│   └── remotive_validado.csv          # Dados validados e limpos
│   └── remotive_erros_detectados.csv  # Dados analisados pela LLM
├── src/
│   └── assistente_llm.py              # Função de análise textual com LLM
│   └── jobs_spider.py                 # Função de extração dos dados
│   └── pandas_validation.py           # Função de validacao e pontuação das vagas
├── README.md
└── requirements.txt
```

---

##  Funcionalidades

-  **Extração de Dados**: coleta automática usando API da Remotive.
-  **Limpeza de HTML**: campo de descrição tratado com BeautifulSoup.
-  **Validação com Regras**: checagem de campos obrigatórios, formatos, vazios etc.
-  **Validação com LLM**: inspeção textual da descrição da vaga, identificação de erros de clareza, tom, redundância etc.
-  **Dashboard Streamlit**: visualização e inspeção manual de validações.

---

##  Exemplo de Output da LLM

> "1. **Erro de formatação**: uso excessivo de negrito.  
> 2. **Tom excessivamente formal**: linguagem distante do candidato.  
> 3. **Ausência de chamada para ação**: não convida o usuário a aplicar."

---

##  Licença

Este projeto é para fins educacionais e não possui fins comerciais.

---

##  Autor

Fernando Nast  
[LinkedIn](https://www.linkedin.com/in/fernandonast)