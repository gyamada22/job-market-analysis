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

> **Solução:** Para contornar, coletei os dados manualmente, visitando cada vaga e usando prompts de IA para extrair informações estruturadas (empresa, cargo, localização, data e skills).

Essa abordagem garantiu **eficiência e confiabilidade** para o pipeline subsequente.

---

## 🛠️ Tecnologias e Ferramentas

O fluxo do projeto segue:

**Coleta** ![IA](https://img.shields.io/badge/IA-AI-blue) ⟶ **Visualização** ![Excel](https://img.shields.io/badge/Excel-217346?style=flat&logo=microsoft-excel&logoColor=white) ⟶ **Limpeza** ![Python](https://img.shields.io/badge/Python-3670A0?style=flat&logo=python&logoColor=white) ⟶ **Análise** ![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat&logo=mysql&logoColor=white) ⟶ **Apresentação** ![Power BI](https://img.shields.io/badge/Dashboard-F2C811?style=flat&logo=power-bi&logoColor=black) ⟶ **Documentação** ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)

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

## ✅ Status Atual
- [ ] Estrutura de pastas criada  
- [ ] Coleta de dados inicial (10 vagas)  
- [ ] Modelagem do banco de dados  
- [ ] Primeiras análises  
- [ ] Dashboard inicial  

---

## 🔹 Observações Finais
- Pipeline eficiente, contornando limitações do LinkedIn  
- Uso integrado de IA, Python, SQL, Power BI e Excel
- Documentação clara, garantindo transparência e profissionalismo para portfólio
