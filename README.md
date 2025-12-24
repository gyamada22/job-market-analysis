# Job Market Analysis 

## 🖥️ Descrição do Projeto
- Este projeto tem como objetivo analisar **vagas reais de emprego na área de dados**, coletadas a partir de plataformas de recrutamento (ex: LinkedIn), para extrair insights sobre **skills demandadas, tendências do mercado e gaps de competências**.

- A análise é inicialmente focada no **mercado brasileiro**, com posterior **comparação com dados internacionais**, visando identificar padrões globais e possíveis tendências que podem chegar ao Brasil no futuro.

- O projeto transforma dados não estruturados em **insights analíticos e dashboards interativos**, documentando todo o pipeline de dados de forma clara e profissional.

---

## 🔹 Coleta de Dados
> **Desafio:** LinkedIn possui API fechada, impossibilitando a coleta automatizada de vagas diretamente via Python.

> **Solução:** Para contornar, coletei os dados manualmente, visitando cada vaga e usando prompts de IA para extrair informações estruturadas (empresa, cargo, localização, data e skills).

Essa abordagem garantiu **eficiência e confiabilidade** para o pipeline subsequente.

---

## 🛠️ Tecnologias e Ferramentas

O fluxo do projeto segue:

**Coleta** ![IA](https://img.shields.io/badge/IA-AI-blue) ⟶ **Visualização** ![Excel](https://img.shields.io/badge/Excel-217346?style=flat&logo=microsoft-excel&logoColor=white) ⟶ **Limpeza** ![Python](https://img.shields.io/badge/Python-3670A0?style=flat&logo=python&logoColor=white) ⟶ **Análise** ![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat&logo=mysql&logoColor=white) ⟶ **Apresentação** ![Power BI](https://img.shields.io/badge/Dashboard-F2C811?style=flat&logo=power-bi&logoColor=black) ⟶ **Documentação** ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)

| Etapa | Ferramenta | Função |
|-------|------------|------|
| Coleta & extração | IA via prompts | Extrai dados estruturados da vaga |
| Visualização inicial | Excel | Conferência e revisão rápida. Arquivo: [Raw Data](https://github.com/gyamada22/Job-Market-Analysis/blob/main/data/raw/Vagas_Coletadas_Raw.xlsx?raw=true) |
| Limpeza e padronização | Python | Padroniza dados, corrige inconsistências e gera Excel/SQL. Arquivo: [Cleaned Data](https://github.com/gyamada22/Job-Market-Analysis/blob/main/data/cleaned/Vagas_Coletadas_Cleaned.xlsx?raw=true), Script: [ETL.py](https://github.com/gyamada22/Job-Market-Analysis/blob/main/data/ETL.py) |
| Modelagem e análise | SQL | Criação de tabelas, views e queries analíticas. |
| Dashboards | Power BI | Visualização interativa, insights e storytelling |
| Documentação | GitHub | Registro completo do projeto, metodologia e exemplos de dashboards |

> 💡 Observação: Python permite **automatizar toda a cadeia de transformação**, tornando o fluxo de dados mais eficiente e escalável do que usar Excel para limpeza manual.

---

## 🎯 Objetivos
- Coletar dados de vagas reais: empresa, cargo, localização, data, nível de senioridade e requisitos técnicos.  
- Padronizar e estruturar dados textuais não estruturados (descrições de vagas).  
- Identificar **skills mais demandadas** por área e nível (estágio, júnior, pleno, sênior).  
- Analisar **diferenças e gaps de competências** entre níveis de senioridade.  
- Comparar o mercado brasileiro com dados internacionais para identificar **tendências emergentes**.  
- Criar dashboards interativos que apoiem **decisões de carreira e estudo**.  
- Documentar todo o pipeline: **coleta → limpeza → análise → visualização**.

---

## ✅ Status Atual
- [x] Estrutura de pastas criada  
- [x] Coleta de dados inicial 
- [ ] Modelagem do banco de dados  
- [ ] Primeiras análises  
- [ ] Dashboard inicial  

---

## 🔹 Observações Finais
- Pipeline eficiente, contornando limitações do LinkedIn  
- Uso integrado de IA, Python, SQL, Power BI e Excel
- Documentação clara, garantindo transparência e profissionalismo para portfólio
