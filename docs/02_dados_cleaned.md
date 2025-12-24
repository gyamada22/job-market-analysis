# 📂 Dados Limpos – Vagas_Coletadas_Cleaned.xlsx

Este arquivo contém os dados das vagas após **limpeza, padronização e redução**, gerados a partir do raw (`Vagas_Coletadas_Raw.xlsx`) utilizando o script Python [`ETL.py`](../data/ETL.py).  
Ele serve como **versão final pronta para análise, modelagem SQL e dashboards Power BI**.

---

## 📄 Abas do Excel

### 1️⃣ Aba `Vagas`

| Coluna       | Descrição                       | Tipo de dado | Observações |
|-------------|---------------------------------|-------------|------------|
| ID          | Identificador único da vaga      | Numérico    | Chave primária para relacionar com skills |
| Empresa     | Nome da empresa que publicou a vaga | Texto   | Valores padronizados onde necessário |
| Setor       | Setor de atuação da empresa      | Texto       | Alguns registros podem estar vazios |
| Modalidade  | Regime de trabalho               | Texto       | Ex.: Presencial, Remoto, Híbrido |
| Senioridade | Nível da vaga                    | Texto       | Ex.: Estágio, Júnior, Pleno, Sênior |
| Cargo       | Cargo padronizado                | Texto       | Ex.: Analista de Dados, Cientista de Dados |
| Estado      | Estado da vaga                   | Texto       | Extraído e padronizado a partir da coluna `Localização` |

### 2️⃣ Aba `Skills`

| Coluna    | Descrição                     | Tipo de dado | Observações |
|-----------|-------------------------------|-------------|------------|
| ID_Vaga   | ID da vaga correspondente      | Numérico    | Chave estrangeira para a aba `Vagas` |
| Skill     | Nome da skill agrupada e padronizada | Texto | Exemplos: Python, SQL, Excel Avançado, Power BI, Tableau; outras → "Outra Skill" |
| Requisito | Obrigatório ou Diferencial     | Texto       | Padronizado a partir da coluna original `Obrigatório/Diferencial` |

---

## 🧹 Pipeline de Limpeza e Transformação (ETL)

O arquivo [`ETL.py`](../data/ETL.py) realiza todas as etapas de limpeza e transformação:

### 1️⃣ Padronização de Cargo
- Converte cargos para minúsculas e aplica regras:
  - "alis" → "Analista de Dados"
  - "enti" → "Cientista de Dados"

### 2️⃣ Extração e Padronização de Estado
- Mapeia `Localização` para estado correto, reconhecendo abreviações e cidades:
  - "SP", "Barueri" → "São Paulo"
  - "RJ", "Rio de Jan" → "Rio de Janeiro"
  - "remoto" ou "remote" → "Remoto"

### 3️⃣ Tratamento de Skills
- Padroniza requisitos:
  - "sim", "básico", "obrigatório" → "Obrigatório"
  - "não", "diferencial" → "Diferencial"
- Agrupa skills padronizadas; skills não mapeadas recebem "Outra Skill"

### 4️⃣ Redução e Reorganização de Colunas
- Aba `Vagas`: 7 colunas essenciais  
- Aba `Skills`: 3 colunas essenciais

### 5️⃣ Exportação e Carga em SQL
- Exporta para Excel (`Vagas_Coletadas_Cleaned.xlsx`)  
- Carrega automaticamente no SQL Server (`Vagas` e `Skills`) via pyodbc  
- Permite consultas analíticas e integração com dashboards Power BI

---

💡 **Resumo:**  
O script transforma os dados brutos em uma **versão limpa, padronizada e reduzida**, mantendo **rastreabilidade com os dados originais** e pronta para análises, modelagem e visualizações.
