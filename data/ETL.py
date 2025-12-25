import pandas as pd
import pyodbc

CONFIG = {
    'server': 'localhost\\SQLEXPRESS',
    'database': 'projeto_vagas',
    'table_vagas': 'Vagas',
    'table_skills': 'Skills',
    'excel_origem': r'C:\MeusProjetos\projeto_vagas\Dados\Vagas_Coletadas_Raw.xlsx',
    'excel_processado': r'C:\MeusProjetos\projeto_vagas\Dados\Vagas_Coletadas_Cleaned.xlsx'
}



# vamos padronizar 4 colunas #1 cargo , #2 localizacao , #3 requisito e #4 skill

#1
def padronizar_cargo(cargo):
    if pd.isna(cargo): 
        return cargo
    cargo_str = str(cargo).lower()
    if 'nalis' in cargo_str: 
        return 'Analista de Dados'
    elif 'entis' in cargo_str: 
        return 'Cientista de Dados'
    return cargo

#2
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

#3
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

#4
def padronizar_skill(skill):
    if pd.isna(skill):
        return None

    s = str(skill).strip().lower()

    if 'python' in s:
        return 'Python'

    mapeamento = {
        # Linguagens
        'java': 'Java',
        'sql': 'SQL',
        ' r ': 'R',

        # BI / Visualizaçao
        'power bi': 'Power BI',
        'tableau': 'Tableau',
        'looker': 'Looker',
        'qlik': 'Qlik',

        # Excel
        'excel': 'Excel Avançado',
        'vba': 'Excel Avançado',
        'power query': 'Excel Avançado',
        'power pivot': 'Excel Avançado',

        # Machine Learning / IA
        'machine learning': 'Machine Learning',
        'deep learning': 'Deep Learning',
        'nlp': 'NLP',
        'inteligência artificial': 'IA',
        ' ia ': 'IA',

        # Estatistica
        'estatística': 'Estatística',
        'probabilidade': 'Estatística',

        # Engenharia de Dados
        'etl': 'ETL',
        'elt': 'ETL',
        'airflow': 'ETL',
        'dbt': 'ETL',

        # Cloud
        'aws': 'AWS',
        'azure': 'Azure',
        'gcp': 'GCP',
    }

    for termo, padrao in mapeamento.items():
        if termo in f" {s} ":
            return padrao

    return 'Outras Skills'

vagas = pd.read_excel(CONFIG['excel_origem'], sheet_name='Vagas')
skills = pd.read_excel(CONFIG['excel_origem'], sheet_name='Skills')

# padronizar colunas
vagas['Cargo'] = vagas['Cargo'].apply(padronizar_cargo)
vagas['Localizacao'] = vagas['Localização'].apply(padronizar_estado)  

skills['Requisito'] = skills['Requisito'].apply(padronizar_requisito)
skills['Skill'] = skills['Skill'].apply(padronizar_skill)

# salvar arquivos limpos em Excel
vagas.to_excel(CONFIG['excel_processado'], index=False, sheet_name='Vagas')
skills.to_excel(CONFIG['excel_processado'], index=False, sheet_name='Skills')

def conectar_banco():
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={CONFIG['server']};"
        f"DATABASE={CONFIG['database']};"
        f"Trusted_Connection=yes;"
    )
    return pyodbc.connect(conn_str)

def importar_dados(conn, df_vagas, df_skills):
    cursor = conn.cursor()
    
    # apagar os dados antigos
    cursor.execute(f"DELETE FROM {CONFIG['table_skills']}")
    cursor.execute(f"DELETE FROM {CONFIG['table_vagas']}")
    
    vagas_data = [
        (
            row['ID'], 
            row['Empresa'], 
            row['Setor'], 
            row['Modalidade'], 
            row['Senioridade'], 
            row['Cargo'], 
            row['Localizacao']  
        )
        for _, row in df_vagas.iterrows()
    ]
    
    skills_data = [
        (
            row['Vaga_ID'], 
            row['Skill'], 
            row['Requisito']
        )
        for _, row in df_skills.iterrows()
    ]
    
    # inserçao no sql server
    cursor.executemany(f"""
        INSERT INTO {CONFIG['table_vagas']} 
        (ID, Empresa, Setor, Modalidade, Senioridade, Cargo, Localizacao)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, vagas_data)
    
    cursor.executemany(f"""
        INSERT INTO {CONFIG['table_skills']} 
        (Vaga_ID, Skill, Requisito)
        VALUES (?, ?, ?)
    """, skills_data)
    
    conn.commit()
    cursor.close()

def main():
    conn = conectar_banco()
    importar_dados(conn, vagas, skills)
    conn.close()

if __name__ == "__main__":
    main()
