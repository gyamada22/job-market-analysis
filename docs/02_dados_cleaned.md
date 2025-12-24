# 🧹 Processo de Limpeza e Transformação – Python

O arquivo `Vagas_Coletadas_Cleaned.xlsx` é gerado a partir do raw (`Vagas_Coletadas_Raw.xlsx`) utilizando um **script Python** que realiza as seguintes etapas:

---

## 1️⃣ Padronização de Cargo
- Converte todos os cargos para letras minúsculas e aplica regras de padronização:
  - Termos como "alis" → "Analista de Dados"
  - Termos como "enti" → "Cientista de Dados"
- Resultado armazenado na coluna `Cargo` final.

## 2️⃣ Extração e Padronização de Estado
- Analisa a coluna `Localização` e mapeia para o **estado correto**.
- Reconhece variações, abreviações e cidades, por exemplo:
  - "SP", "Barueri" → "São Paulo"
  - "RJ", "Rio de Jan" → "Rio de Janeiro"
  - "remoto" ou "remote" → "Remoto"
- Resultado armazenado na coluna `Estado`.

## 3️⃣ Tratamento de Skills
- A coluna de requisitos (`Obrigatório/Diferencial`) é padronizada:
  - Valores como "sim", "básico", "obrigatório" → "Obrigatório"
  - Valores como "não", "diferencial" → "Diferencial"
- As skills são agrupadas em categorias padronizadas:
  - Exemplos: "Python", "SQL", "Excel Avançado", "Power BI", "Tableau"
  - Skills não mapeadas recebem "Outra Skill"

## 4️⃣ Redução e Reorganização das Colunas
- Aba `Vagas`: mantidas apenas 7 colunas essenciais:
  - `ID`, `Empresa`, `Setor`, `Modalidade`, `Senioridade`, `Cargo`, `Estado`
- Aba `Skills`: mantidas 3 colunas essenciais:
  - `ID_Vaga`, `Skill`, `Requisito`

## 5️⃣ Exportação e Carga em SQL
- Dados limpos exportados para Excel (`analise_vagas.xlsx`)
- Também enviados para banco SQL (`Vagas` e `Skills`) via pyodbc
- Permite consultas analíticas e integração com dashboards Power BI

---

💡 **Resumo:**  
O script transforma os dados brutos em uma **versão padronizada, limpa e reduzida**, pronta para análises, modelagem e visualizações, mantendo **rastreabilidade com os dados originais**.

