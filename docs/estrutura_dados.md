# Estrutura de Dados para Extração de Vagas do LinkedIn

Este documento descreve a **estrutura de abas do Excel** e o **prompt usado para extrair dados de vagas** do LinkedIn, gerando arquivos prontos para análise no Excel, Python ou SQL.

---

##  Estrutura das abas do Excel

### Aba `vagas`
ID, Empresa, Setor, Cargo, Modelo_Trabalho, Area_Atuacao, Data, Senioridade, Localizacao, Tipo_Contratacao, Ferramentas_Específicas, Remoto, Categoria, Fonte_Vaga

### Aba `skills`
Colunas:  Vaga_ID, Skill, Tipo, Nivel_Conhecimento, Obrigatório/Diferencial, Categoria

## Embora exista uma estrutura completa prevista, apenas um subconjunto das abas e colunas é utilizado nesta fase, conforme descrito abaixo.

### Aba `vagas`
ID, Empresa, Setor, Cargo, Modelo_Trabalho, Localização, Senioridade

### Aba `skills`
Vaga_ID, Skill, Obrigatório/Diferencial

---

##  Critério de pesquisa no LinkedIn

As vagas foram coletadas manualmente a partir do LinkedIn utilizando a seguinte **query de busca**:

("analista de dados" OR "cientista de dados" OR "analista bi") AND (sql OR python OR excel OR "power bi")


---

##  Prompt para extrair dados do LinkedIn

```
# PROMPT FINAL AJUSTADO — EXTRAÇÃO DE VAGAS (TSV PURO)

Você vai receber a descrição completa de uma vaga de emprego.

Seu objetivo é extrair os dados para **DUAS abas de Excel**, no formato **TSV (Tab-Separated Values)**:

- Aba 1: `vagas` (13 colunas)  
- Aba 2: `skills` (6 colunas)  

⚠️ **REGRAS CRÍTICAS — NÃO IGNORAR**

## 1️⃣ Estrutura e validação obrigatória
- Aba **`vagas` DEVE TER EXATAMENTE 13 COLUNAS**  
- Aba **`skills` DEVE TER EXATAMENTE 6 COLUNAS**  
- **NUNCA** pode haver deslocamento de dados entre colunas  
- **Toda coluna inexistente deve ser representada por um TAB vazio**  
- Validar mentalmente a quantidade de colunas antes do envio  

## 2️⃣ Regras TSV obrigatórias
- Separador: **TAB**  
- **Nunca usar vírgula como separador**  
- Campos podem conter vírgulas, ponto e vírgula e textos longos **sem aspas**  
- Coluna vazia = TAB  

## 3️⃣ Regras absolutas de output
- **O OUTPUT DEVE CONTER APENAS OS DADOS TSV**, sem qualquer código, comentário, explicação ou linha extra  
- OUTPUT SEMPRE EM CODIGO POWERSHELL
- Cada aba deve ser apresentada separadamente, primeiro `vagas` depois `skills`  
- Nunca misturar os dois conjuntos de dados  
- Nenhum cabeçalho ou linha de separação deve ser incluído  

## 4️⃣ Estrutura das abas

### Aba `vagas` (14 colunas)
1. ID  
2. Empresa  
3. Cargo  
4. Modelo_Trab  
5. Area_Atuacao  
6. Data  
7. Nível  
8. Localizacao  
9. Tipo_Contratacao  
10. Ferramentas_Específicas  
11. Remoto  
12. Categoria  
13. Fonte_Vaga  

### Aba `skills` (6 colunas)
1. Vaga_ID  
2. Skill  
3. Tipo  
4. Nivel_Conhecimento  
5. Obrigatoria  
6. Categoria  

## 5️⃣ Regras de extração
- Data padrão se ausente: **18/01/2024**  
- Nível SOMENTE se explícito: **Júnior | Pleno | Sênior**  
- Skills obrigatórias: termos como *requisito, necessário, obrigatório*  
- Skills diferenciais: termos como *desejável, diferencial, plus*  

EXEMPLO DE OUTPUT
--POP UP 1 DE POWESHELL(NAO ESCREVER ISSO NO OUTPUT, OUTPUT APENAS DADOS)
38	UltraCon Consultoria	Analista de Dados	Presencial	Dados	21/12/2025	Júnior	Campinas, São Paulo, Brasil	Tempo integral	Python; Excel; Power Query; Power Automate; Automação de Processos; Dashboards; Análise de Dados	Sim	Dados	LinkedIn

--POP UP 2 DE POWESHELL(NAO ESCREVER ISSO NO OUTPUT, OUTPUT APENAS DADOS)
23	Python	Técnica		Sim	Dados
23	Excel	Técnica		Sim	Dados
23	Power Query	Técnica		Não	Dados
23	Power Automate	Técnica		Não	Dados
23	Automação de Processos	Técnica		Não	Dados
23	Dashboards	Técnica		Não	Dados
23	Análise de Dados	Técnica		Não	Dados






```
