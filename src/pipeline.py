import src.jobs_spider                  as jobs_spider
import src.pandas_validation            as pandas_validation
import src.assistente_llm_testeInicial  as assistente_llm_testeInicial

def main():
    df = jobs_spider()
    df = pandas_validation(df)
    df = assistente_llm_testeInicial(df)
    df.to_csv("data/remotive_validado.csv", index=False)

if __name__ == "__main__":
    main()
