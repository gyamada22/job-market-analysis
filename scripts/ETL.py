import pandas as pd
import snowflake.connector
from dotenv import load_dotenv
import os

load_dotenv()

CONFIG = {
    "user": os.getenv("SNOWFLAKE_USER"),
    "password": os.getenv("SNOWFLAKE_PASSWORD"),
    "account": os.getenv("SNOWFLAKE_ACCOUNT"),
    "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
    "database": os.getenv("SNOWFLAKE_DATABASE"),
    "schema": os.getenv("SNOWFLAKE_SCHEMA"),

    "table_vagas": "VAGAS",
    "table_skills": "SKILLS",

    "excel_origem": r"C:\Users\guilh\Área de Trabalho\github\Analise-Mercado-de-Dados\data\raw\Vagas_Coletadas_Raw.xlsx",
    "excel_processado": r"C:\Users\guilh\Área de Trabalho\github\Analise-Mercado-de-Dados\data\processed\Vagas_Coletadas_Cleaned.xlsx",
}


# 1
def padronizar_cargo(cargo):
    if pd.isna(cargo):
        return cargo
    cargo_str = str(cargo).lower()
    if 'nalis' in cargo_str:
        return 'Analista de Dados'
    elif 'entis' in cargo_str:
        return 'Cientista de Dados'
    return cargo

# 2
def padronizar_estado(local):
    if pd.isna(local):
        return local
    local_str = str(local).lower()
    palavras = local_str.replace('-', ' ').replace('/', ' ').split()
    estados = {
        'acre': 'Acre', 'ac': 'Acre',
        'alagoas': 'Alagoas', 'al': 'Alagoas',
        'amapá': 'Amapá', 'ap': 'Amapá',
        'amazonas': 'Amazonas', 'am': 'Amazonas',
        'bahia': 'Bahia', 'ba': 'Bahia',
        'ceará': 'Ceará', 'ce': 'Ceará',
        'distrito federal': 'Distrito Federal', 'df': 'Distrito Federal',
        'espírito santo': 'Espírito Santo', 'es': 'Espírito Santo',
        'goiás': 'Goiás', 'go': 'Goiás',
        'maranhão': 'Maranhão', 'ma': 'Maranhão',
        'mato grosso': 'Mato Grosso', 'mt': 'Mato Grosso',
        'mato grosso do sul': 'Mato Grosso do Sul', 'ms': 'Mato Grosso do Sul',
        'minas gerais': 'Minas Gerais', 'mg': 'Minas Gerais',
        'pará': 'Pará', 'pa': 'Pará',
        'paraíba': 'Paraíba', 'pb': 'Paraíba',
        'paraná': 'Paraná', 'pr': 'Paraná',
        'pernambuco': 'Pernambuco', 'pe': 'Pernambuco',
        'piauí': 'Piauí', 'pi': 'Piauí',
        'rio de janeiro': 'Rio de Janeiro', 'rj': 'Rio de Janeiro',
        'rio grande do norte': 'Rio Grande do Norte', 'rn': 'Rio Grande do Norte',
        'rio grande do sul': 'Rio Grande do Sul', 'rs': 'Rio Grande do Sul',
        'rondônia': 'Rondônia', 'ro': 'Rondônia',
        'roraima': 'Roraima', 'rr': 'Roraima',
        'santa catarina': 'Santa Catarina', 'sc': 'Santa Catarina',
        'são paulo': 'São Paulo', 'sp': 'São Paulo',
        'sergipe': 'Sergipe', 'se': 'Sergipe',
        'tocantins': 'Tocantins', 'to': 'Tocantins'
    }
    if 'remoto' in local_str or 'remote' in local_str:
        return 'Remoto'
    for palavra in palavras:
        if palavra in estados:
            return estados[palavra]
    for chave, estado in estados.items():
        if len(chave) > 2 and chave in local_str:
            return estado
    return 'Não identificado'

# 3
def padronizar_requisito(valor):
    if pd.isna(valor):
        return "Não informado"
    valor_str = str(valor).strip().lower()
    obrigatorio = {'sim', 'obrigatório', 'obrigatorio'}
    diferencial = {'não', 'nao', 'diferencial'}
    if valor_str in obrigatorio:
        return "Obrigatório"
    elif valor_str in diferencial:
        return "Diferencial"
    else:
        return "Não informado"

# 4
def padronizar_skill(skill):
    if pd.isna(skill):
        return None

    s = str(skill).strip().lower()

    if 'python' in s:
        return 'Python'

    mapeamento = {

        'java': 'Java',
        'sql': 'SQL',
        ' r ': 'R',

        'power bi': 'Power BI',
        'powerbi': 'Power BI',
        'bi': 'Power BI',
        'business intelligence': 'Power BI',
        'tableau': 'Tableau',
        'looker': 'Looker',
        'qlik': 'Qlik',
        'ibm cognos': 'Power BI',
        'dashboards': 'Power BI',
        'data viz': 'Power BI',
        'data visualization': 'Power BI',
        'visualização': 'Power BI',
        'visualização de dados': 'Power BI',
        'storytelling': 'Power BI',
        'storytelling com dados': 'Power BI',
        'dax': 'Power BI',
        'dax studio': 'Power BI',
        'kpis': 'Power BI',

        'excel': 'Excel Avançado',
        'vba': 'Excel Avançado',
        'power query': 'Excel Avançado',
        'power pivot': 'Excel Avançado',
        'powerapps': 'Excel Avançado',
        'power apps': 'Excel Avançado',
        'power automate': 'Excel Avançado',
        'power platform': 'Excel Avançado',
        'google sheets': 'Excel Avançado',


        'aws': 'Cloud',
        'azure': 'Cloud',
        'gcp': 'Cloud',
        'google cloud': 'Cloud',
        'google cloud platform': 'Cloud',
        'cloud': 'Cloud',
        'cloud computing': 'Cloud',
        'serverless': 'Cloud',

        'big data': 'Big Data',
        'bigdata': 'Big Data',
        'spark': 'Big Data',
        'hadoop': 'Big Data',
        'databricks': 'Big Data',

        'data warehouse': 'Data Warehouse',
        'data lake': 'Data Lake',
        'snowflake': 'Data Warehouse',
        'teradata': 'Data Warehouse',

        'etl': 'ETL',
        'elt': 'ETL',
        'airflow': 'ETL',
        'dbt': 'ETL',
        'nifi': 'ETL',
        'ssis': 'ETL',
        'kedro': 'ETL',
        'flink': 'ETL',
        'n8n': 'ETL',
        'data pipelines': 'ETL',

        'docker': 'DevOps',
        'kubernetes': 'DevOps',
        'terraform': 'DevOps',
        'devops': 'DevOps',

        'machine learning': 'Machine Learning',
        'deep learning': 'Deep Learning',
        'mlops': 'Mlops',
        'estatística': 'Estatística',
        'probabilidade': 'Estatística',
        'nlp': 'NLP',
        'inteligência artificial': 'IA',
        ' ia ': 'IA',
        'llm': 'IA',
        'llms': 'IA',
        'langchain': 'IA',
        'rag': 'IA',
        'crewai': 'IA',
        'modelagem preditiva': 'Machine Learning',
        'redes neurais': 'Machine Learning',

        'pandas': 'Bibliotecas Python',
        'numpy': 'Bibliotecas Python',
        'pyspark': 'Bibliotecas Python',
        'matplotlib': 'Bibliotecas Python',
        'seaborn': 'Bibliotecas Python',
        'plotly': 'Bibliotecas Python',
        'scikit-learn': 'Bibliotecas Python',
        'scikit learn': 'Bibliotecas Python',
        'scikit': 'Bibliotecas Python',

        'mongodb': 'NoSQL',
        'postgres': 'SQL',
        'oracle': 'Oracle',
        'duckdb': 'DuckDB',
        'sap': 'SAP',
        'sas': 'SAS',
        'knime': 'Knime',
        'metabase': 'Metabase',
        'pentaho': 'Pentaho',
        'alteryx': 'Alteryx',
        'git': 'Git',
        'jupyter': 'Jupyter',
        'google colab': 'Google Colab',
        'api': 'API',
        'apis': 'API',
        'rest': 'API',
        'json': 'API',
        'inglês': 'Inglês',
        'inglês avançado': 'Inglês'
    }

    for termo, padrao in mapeamento.items():
        if termo in f" {s} ":
            return padrao

    return 'Outra Skill'




vagas = pd.read_excel(CONFIG["excel_origem"], sheet_name="Vagas")
skills = pd.read_excel(CONFIG["excel_origem"], sheet_name="Skills")

vagas["Estado"] = vagas["Localização"].apply(padronizar_estado)
vagas["Cargo"] = vagas["Cargo"].apply(padronizar_cargo)

skills["Requisito"] = skills["Requisito"].apply(padronizar_requisito)
skills["Skill"] = skills["Skill"].apply(padronizar_skill)

skills = skills.drop_duplicates(subset=["Vaga_ID", "Skill"], keep="first")

with pd.ExcelWriter(CONFIG["excel_processado"], engine="openpyxl") as writer:
    vagas.to_excel(writer, index=False, sheet_name="Vagas")
    skills.to_excel(writer, index=False, sheet_name="Skills")


def conectar_snowflake():
    return snowflake.connector.connect(
        user=CONFIG["user"],
        password=CONFIG["password"],
        account=CONFIG["account"],
        warehouse=CONFIG["warehouse"],
        database=CONFIG["database"],
        schema=CONFIG["schema"],
    )


def importar_dados(conn, df_vagas, df_skills):
    cursor = conn.cursor()

    cursor.execute(f"TRUNCATE TABLE {CONFIG['table_skills']}")
    cursor.execute(f"TRUNCATE TABLE {CONFIG['table_vagas']}")

    cursor.executemany(
        f"""
        INSERT INTO {CONFIG['table_vagas']}
        (ID, EMPRESA, SETOR, MODALIDADE, SENIORIDADE, CARGO, ESTADO)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        df_vagas[
            ["ID", "Empresa", "Setor", "Modalidade", "Senioridade", "Cargo", "Estado"]
        ].values.tolist(),
    )

    cursor.executemany(
        f"""
        INSERT INTO {CONFIG['table_skills']}
        (VAGA_ID, SKILL, REQUISITO)
        VALUES (%s, %s, %s)
        """,
        df_skills[["Vaga_ID", "Skill", "Requisito"]].values.tolist(),
    )

    conn.commit()
    cursor.close()


def main():
    conn = conectar_snowflake()
    importar_dados(conn, vagas, skills)
    conn.close()


if __name__ == "__main__":
=======
import pandas as pd
import snowflake.connector
from dotenv import load_dotenv
import os

load_dotenv()

CONFIG = {
    "user": os.getenv("SNOWFLAKE_USER"),
    "password": os.getenv("SNOWFLAKE_PASSWORD"),
    "account": os.getenv("SNOWFLAKE_ACCOUNT"),
    "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
    "database": os.getenv("SNOWFLAKE_DATABASE"),
    "schema": os.getenv("SNOWFLAKE_SCHEMA"),

    "table_vagas": "VAGAS",
    "table_skills": "SKILLS",

    "excel_origem": r"C:\Users\guilh\Área de Trabalho\github\Analise-Mercado-de-Dados\data\raw\Vagas_Coletadas_Raw.xlsx",
    "excel_processado": r"C:\Users\guilh\Área de Trabalho\github\Analise-Mercado-de-Dados\data\processed\Vagas_Coletadas_Cleaned.xlsx",
}


# 1
def padronizar_cargo(cargo):
    if pd.isna(cargo):
        return cargo
    cargo_str = str(cargo).lower()
    if 'nalis' in cargo_str:
        return 'Analista de Dados'
    elif 'entis' in cargo_str:
        return 'Cientista de Dados'
    return cargo

# 2
def padronizar_estado(local):
    if pd.isna(local):
        return local
    local_str = str(local).lower()
    palavras = local_str.replace('-', ' ').replace('/', ' ').split()
    estados = {
        'acre': 'Acre', 'ac': 'Acre',
        'alagoas': 'Alagoas', 'al': 'Alagoas',
        'amapá': 'Amapá', 'ap': 'Amapá',
        'amazonas': 'Amazonas', 'am': 'Amazonas',
        'bahia': 'Bahia', 'ba': 'Bahia',
        'ceará': 'Ceará', 'ce': 'Ceará',
        'distrito federal': 'Distrito Federal', 'df': 'Distrito Federal',
        'espírito santo': 'Espírito Santo', 'es': 'Espírito Santo',
        'goiás': 'Goiás', 'go': 'Goiás',
        'maranhão': 'Maranhão', 'ma': 'Maranhão',
        'mato grosso': 'Mato Grosso', 'mt': 'Mato Grosso',
        'mato grosso do sul': 'Mato Grosso do Sul', 'ms': 'Mato Grosso do Sul',
        'minas gerais': 'Minas Gerais', 'mg': 'Minas Gerais',
        'pará': 'Pará', 'pa': 'Pará',
        'paraíba': 'Paraíba', 'pb': 'Paraíba',
        'paraná': 'Paraná', 'pr': 'Paraná',
        'pernambuco': 'Pernambuco', 'pe': 'Pernambuco',
        'piauí': 'Piauí', 'pi': 'Piauí',
        'rio de janeiro': 'Rio de Janeiro', 'rj': 'Rio de Janeiro',
        'rio grande do norte': 'Rio Grande do Norte', 'rn': 'Rio Grande do Norte',
        'rio grande do sul': 'Rio Grande do Sul', 'rs': 'Rio Grande do Sul',
        'rondônia': 'Rondônia', 'ro': 'Rondônia',
        'roraima': 'Roraima', 'rr': 'Roraima',
        'santa catarina': 'Santa Catarina', 'sc': 'Santa Catarina',
        'são paulo': 'São Paulo', 'sp': 'São Paulo',
        'sergipe': 'Sergipe', 'se': 'Sergipe',
        'tocantins': 'Tocantins', 'to': 'Tocantins'
    }
    if 'remoto' in local_str or 'remote' in local_str:
        return 'Remoto'
    for palavra in palavras:
        if palavra in estados:
            return estados[palavra]
    for chave, estado in estados.items():
        if len(chave) > 2 and chave in local_str:
            return estado
    return 'Não identificado'

# 3
def padronizar_requisito(valor):
    if pd.isna(valor):
        return "Não informado"
    valor_str = str(valor).strip().lower()
    obrigatorio = {'sim', 'obrigatório', 'obrigatorio'}
    diferencial = {'não', 'nao', 'diferencial'}
    if valor_str in obrigatorio:
        return "Obrigatório"
    elif valor_str in diferencial:
        return "Diferencial"
    else:
        return "Não informado"

# 4
def padronizar_skill(skill):
    if pd.isna(skill):
        return None

    s = str(skill).strip().lower()

    if 'python' in s:
        return 'Python'

    mapeamento = {

        'java': 'Java',
        'sql': 'SQL',
        ' r ': 'R',

        'power bi': 'Power BI',
        'powerbi': 'Power BI',
        'bi': 'Power BI',
        'business intelligence': 'Power BI',
        'tableau': 'Tableau',
        'looker': 'Looker',
        'qlik': 'Qlik',
        'ibm cognos': 'Power BI',
        'dashboards': 'Power BI',
        'data viz': 'Power BI',
        'data visualization': 'Power BI',
        'visualização': 'Power BI',
        'visualização de dados': 'Power BI',
        'storytelling': 'Power BI',
        'storytelling com dados': 'Power BI',
        'dax': 'Power BI',
        'dax studio': 'Power BI',
        'kpis': 'Power BI',

        'excel': 'Excel Avançado',
        'vba': 'Excel Avançado',
        'power query': 'Excel Avançado',
        'power pivot': 'Excel Avançado',
        'powerapps': 'Excel Avançado',
        'power apps': 'Excel Avançado',
        'power automate': 'Excel Avançado',
        'power platform': 'Excel Avançado',
        'google sheets': 'Excel Avançado',


        'aws': 'Cloud',
        'azure': 'Cloud',
        'gcp': 'Cloud',
        'google cloud': 'Cloud',
        'google cloud platform': 'Cloud',
        'cloud': 'Cloud',
        'cloud computing': 'Cloud',
        'serverless': 'Cloud',

        'big data': 'Big Data',
        'bigdata': 'Big Data',
        'spark': 'Big Data',
        'hadoop': 'Big Data',
        'databricks': 'Big Data',

        'data warehouse': 'Data Warehouse',
        'data lake': 'Data Lake',
        'snowflake': 'Data Warehouse',
        'teradata': 'Data Warehouse',

        'etl': 'ETL',
        'elt': 'ETL',
        'airflow': 'ETL',
        'dbt': 'ETL',
        'nifi': 'ETL',
        'ssis': 'ETL',
        'kedro': 'ETL',
        'flink': 'ETL',
        'n8n': 'ETL',
        'data pipelines': 'ETL',

        'docker': 'DevOps',
        'kubernetes': 'DevOps',
        'terraform': 'DevOps',
        'devops': 'DevOps',

        'machine learning': 'Machine Learning',
        'deep learning': 'Deep Learning',
        'mlops': 'Mlops',
        'estatística': 'Estatística',
        'probabilidade': 'Estatística',
        'nlp': 'NLP',
        'inteligência artificial': 'IA',
        ' ia ': 'IA',
        'llm': 'IA',
        'llms': 'IA',
        'langchain': 'IA',
        'rag': 'IA',
        'crewai': 'IA',
        'modelagem preditiva': 'Machine Learning',
        'redes neurais': 'Machine Learning',

        'pandas': 'Bibliotecas Python',
        'numpy': 'Bibliotecas Python',
        'pyspark': 'Bibliotecas Python',
        'matplotlib': 'Bibliotecas Python',
        'seaborn': 'Bibliotecas Python',
        'plotly': 'Bibliotecas Python',
        'scikit-learn': 'Bibliotecas Python',
        'scikit learn': 'Bibliotecas Python',
        'scikit': 'Bibliotecas Python',

        'mongodb': 'NoSQL',
        'postgres': 'SQL',
        'oracle': 'Oracle',
        'duckdb': 'DuckDB',
        'sap': 'SAP',
        'sas': 'SAS',
        'knime': 'Knime',
        'metabase': 'Metabase',
        'pentaho': 'Pentaho',
        'alteryx': 'Alteryx',
        'git': 'Git',
        'jupyter': 'Jupyter',
        'google colab': 'Google Colab',
        'api': 'API',
        'apis': 'API',
        'rest': 'API',
        'json': 'API',
        'inglês': 'Inglês',
        'inglês avançado': 'Inglês'
    }

    for termo, padrao in mapeamento.items():
        if termo in f" {s} ":
            return padrao

    return 'Outra Skill'




vagas = pd.read_excel(CONFIG["excel_origem"], sheet_name="Vagas")
skills = pd.read_excel(CONFIG["excel_origem"], sheet_name="Skills")

vagas["Estado"] = vagas["Localização"].apply(padronizar_estado)
vagas["Cargo"] = vagas["Cargo"].apply(padronizar_cargo)

skills["Requisito"] = skills["Requisito"].apply(padronizar_requisito)
skills["Skill"] = skills["Skill"].apply(padronizar_skill)

skills = skills.drop_duplicates(subset=["Vaga_ID", "Skill"], keep="first")

with pd.ExcelWriter(CONFIG["excel_processado"], engine="openpyxl") as writer:
    vagas.to_excel(writer, index=False, sheet_name="Vagas")
    skills.to_excel(writer, index=False, sheet_name="Skills")


def conectar_snowflake():
    return snowflake.connector.connect(
        user=CONFIG["user"],
        password=CONFIG["password"],
        account=CONFIG["account"],
        warehouse=CONFIG["warehouse"],
        database=CONFIG["database"],
        schema=CONFIG["schema"],
    )


def importar_dados(conn, df_vagas, df_skills):
    cursor = conn.cursor()

    cursor.execute(f"TRUNCATE TABLE {CONFIG['table_skills']}")
    cursor.execute(f"TRUNCATE TABLE {CONFIG['table_vagas']}")

    cursor.executemany(
        f"""
        INSERT INTO {CONFIG['table_vagas']}
        (ID, EMPRESA, SETOR, MODALIDADE, SENIORIDADE, CARGO, ESTADO)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        df_vagas[
            ["ID", "Empresa", "Setor", "Modalidade", "Senioridade", "Cargo", "Estado"]
        ].values.tolist(),
    )

    cursor.executemany(
        f"""
        INSERT INTO {CONFIG['table_skills']}
        (VAGA_ID, SKILL, REQUISITO)
        VALUES (%s, %s, %s)
        """,
        df_skills[["Vaga_ID", "Skill", "Requisito"]].values.tolist(),
    )

    conn.commit()
    cursor.close()


def main():
    conn = conectar_snowflake()
    importar_dados(conn, vagas, skills)
    conn.close()


if __name__ == "__main__":
    main()