# Job Market Analysis — Análise de Requisitos de Vagas

## 🖥️ Descrição do Projeto
- Este projeto tem como objetivo analisar **vagas de emprego na área de dados** e extrair insights sobre os **requisitos de skills** mais demandados pelo mercado.
- O objetivo é transformar dados não estruturados em **insights visuais e dashboards interativos**, documentando todo o pipeline de forma profissional.

---

## 🎯 Objetivos
- Coletar informações de vagas: empresa, cargo, localização, data, skills obrigatórias e diferenciais.  
- Padronizar e organizar os dados para análise.  
- Identificar skills mais demandadas, combinações e tendências.  
- Criar dashboards interativos para exploração visual.  
- Documentar todo o processo, mostrando pipeline completo de dados.
---

## 🔹 Coleta de Dados
> **Desafio:** LinkedIn possui API fechada, impossibilitando a coleta automatizada de vagas diretamente via Python.

> **Solução:** Para contornar, usei IA via prompts, extraindo dados estruturados de cada vaga: empresa, cargo, localização, data e skills (obrigatórias/diferenciais).

Essa abordagem garantiu **eficiência e confiabilidade** para o pipeline subsequente.

---

## 🛠️ Tecnologias e Ferramentas

| Etapa | Ferramenta | Função |
|-------|------------|------|
| Coleta & extração | IA via prompts | Extrai dados estruturados da vaga |
| Visualização inicial | Excel | Conferência e revisão rápida |
| Limpeza e padronização | Python | Padroniza dados, corrige inconsistências, remove duplicatas e gera CSV pronto para SQL |
| Modelagem e análise | SQL | Criação de tabelas, views e queries analíticas |
| Dashboards | Power BI | Visualização interativa, insights e storytelling |
| Documentação | GitHub | Registro completo do projeto, metodologia e exemplos de dashboards |

> 💡 Observação: Python permite **automatizar toda a cadeia de transformação**, tornando o fluxo de dados mais eficiente e escalável do que usar Excel para limpeza manual.

---

## 📊 Pipeline do Projeto 

1. **🤖 COLETA COM IA**
   - Extrai dados estruturados de vagas
   - Captura: empresa, cargo, local, data, skills

2. **🐍 PROCESSAMENTO (Python)**
   - Limpeza e padronização de dados
   - Remoção de duplicatas e inconsistências
   - Geração de CSV pronto para SQL

3. **🗄️ ANÁLISE (SQL)**
   - Criação de tabelas e views analíticas
   - Queries para identificar padrões e tendências

4. **📊 VISUALIZAÇÃO (Power BI)**
   - Dashboards interativos
   - Filtros por skill, empresa, localização

5. **📚 DOCUMENTAÇÃO (GitHub)**
   - README completo
   - Explicação da metodologia
   - Resultados e insights

---

## 🔹Observações do Pipeline

IA: captura dados estruturados diretamente da vaga.

Excel: apenas revisão e visualização inicial; Python é mais eficiente para limpeza.

Python: padroniza skills, cargos e empresas, corrige inconsistências, remove duplicatas e gera CSV pronto para SQL.

SQL: cria tabelas, views e queries para análise.

Power BI: dashboards interativos para exploração de insights.

Documentação: GitHub com histórico, metodologia e dashboards.

---

job-market-analysis/
│
├── 📄 README.md                 # Documentação principal
├── 📚 docs/                     # Documentação detalhada
│   ├── 01_contexto.md          # Contexto e objetivos
│   ├── 02_metodologia.md       # Métodos de coleta e análise
│   └── 03_resultados.md        # Insights e descobertas
│
├── 📊 data/                    # Dados
│   ├── raw/                    # Brutos (não versionado)
│   ├── processed/              # Processados
│   └── database/               # Banco SQLite (.db)
│
├── 🐍 src/                     # Código Python
│   ├── collect/                # Coleta de dados
│   ├── process/                # ETL e limpeza
│   └── analyze/                # Análises
│
├── 🗄️ sql/                     # Scripts SQL
│   ├── ddl/                    # Definição de tabelas
│   ├── queries/                # Consultas analíticas
│   └── views/                  # Views para Power BI
│
├── 📓 notebooks/               # Análises exploratórias
├── 📈 dashboards/              # Arquivos Power BI
└── 🤖 prompts/                 # Prompts de IA utilizados


job-market-analysis/
│
├── README.md
├── docs/ # Documentação detalhada
│ ├── 01_contexto.md
│ ├── 02_metodologia.md
│ ├── 03_resultados.md
│ └── 04_tratamento_e_transformacoes.md
│
├── data/
│ ├── raw/ # Dados brutos
│ ├── processed/ # CSV pronto para SQL
│ └── samples/ # Exemplos de dados
│
├── src/ # Código Python
│ ├── collect/
│ ├── process/
│ └── analyze/
│
├── sql/
│ ├── ddl/
│ ├── transformations/
│ └── views/
│
├── notebooks/ # Análises exploratórias
├── dashboards/ # Arquivos Power BI
└── prompts/ # Prompts de IA
---

## ✅ Status Atual
- [x] Estrutura de pastas criada  
- [x] Coleta de dados inicial (10 vagas)  
- [x] Modelagem do banco de dados  
- [x] Primeiras análises  
- [x] Dashboard inicial  

---

## 🚀 Próximos Passos
- Automatizar coleta e extração via IA com novos prompts  
- Criar rotinas Python para atualização automática dos dados  
- Desenvolver dashboards avançados no Power BI  
- Documentar métricas e análises para portfólio  
- Avaliar integração de novas fontes de vagas

---

## 🔹 Observações Finais
- Pipeline eficiente, contornando limitações do LinkedIn  
- Uso integrado de IA, Python, SQL e Power BI (Excel como revisão rápida)  
- Documentação clara, garantindo transparência e profissionalismo para portfólio
