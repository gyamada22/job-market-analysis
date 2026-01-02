# Análise do Mercado de Dados

##  Descrição do Projeto

- Este projeto tem como objetivo analisar **vagas reais de emprego na área de dados**, coletadas a partir de plataformas de recrutamento (LinkedIn), para extrair insights sobre **skills demandadas, tendências do mercado e gaps de competências**.

- A análise é inicialmente focada no **mercado brasileiro**, com posterior **comparação com dados internacionais**, visando identificar padrões globais e possíveis tendências que podem chegar ao Brasil no futuro.

- O projeto transforma dados não estruturados em **dashboards e insights analíticos**, documentando todo o pipeline de dados de forma clara e profissional.

####  O Projeto em Números

- **302 vagas reais** analisadas individualmente (mercado brasileiro – LinkedIn)
- **2.400+ skills brutas (RAW)** extraídas das descrições das vagas.


Inicialmente, o pipeline utilizava um banco de dados local (SQL Server via SSMS) para armazenamento dos dados tratados após o ETL em Python. 
Com a evolução do projeto, a arquitetura foi modernizada para um **Data Warehouse em nuvem (Snowflake)**, incorporando **dbt para modelagem analítica** e **Docker para padronização e execução do ambiente**, aproximando o fluxo da realidade de pipelines profissionais.

---

##  Coleta de Dados
> **Desafio:** LinkedIn possui API fechada, impossibilitando a coleta automatizada de vagas diretamente via Python.

> **Solução:** Para contornar, coletei os dados manualmente, visitando cada vaga e usando prompts de IA para extrair informações estruturadas (empresa, cargo, localização, data e skills).

Essa abordagem garantiu **eficiência e confiabilidade** para o pipeline subsequente.

---

##  Tecnologias e Ferramentas

**Stack Técnica**

![Python](https://img.shields.io/badge/Python-ETL-3670A0?logo=python&logoColor=white)
![dbt](https://img.shields.io/badge/dbt-Modelagem-FF694B?logo=dbt&logoColor=white)
![Snowflake](https://img.shields.io/badge/Snowflake-Data%20Warehouse-29B5E8?logo=snowflake&logoColor=white)
![Power%20BI](https://img.shields.io/badge/Power%20BI-Dashboards-F2C811?logo=power-bi&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-Ambiente-2496ED?logo=docker&logoColor=white)

O fluxo do projeto segue uma arquitetura analítica moderna:

Coleta (IA) ⟶ Limpeza & ETL (Python) ⟶ Modelagem & Análise (SQL / dbt) ⟶ Visualização (Power BI) ⟶ Documentação (GitHub)

| Etapa | Ferramenta | Função |
|-------|------------|------|
| Coleta & extração | IA via prompts | Extração manual e estruturada de dados das vagas coletadas |
| Visualização inicial | Excel | Conferência e revisão rápida dos dados brutos |
| Limpeza e padronização | Python | Limpeza, padronização e carga direta no Data Warehouse(Snowflake) |
| Modelagem e análise | SQL / dbt | Transformações analíticas e geração de métricas no Data Warehouse |
| Dashboards | Power BI | Visualização interativa e storytelling|
| Documentação | GitHub | Registro do projeto e metodologia |

---

##  Evolução da Arquitetura do Pipeline

### Arquitetura Inicial
- ETL em **Python**
- Persistência dos dados tratados em **SQL Server local (SSMS)**
- Execução dependente do ambiente do desenvolvedor
- Transformações concentradas no script Python

### Arquitetura Atual
- ETL em **Python** com carga direta no **Snowflake**
- **dbt** responsável pela modelagem analítica e camadas Silver/Gold
- **Docker** garantindo ambiente isolado, reproduzível e agnóstico à máquina
- Separação clara entre:
  - Ingestão e limpeza (Python)
  - Transformação analítica (dbt)
  - Consumo (Power BI)

Essa evolução reflete a transição de um pipeline **local e monolítico** para uma **arquitetura moderna, escalável e alinhada às boas práticas de engenharia de dados**.

> 🛠️ Consideração arquitetural  
> Durante o design do pipeline, foi avaliado o uso do **Apache Airflow** para automatizar a coleta e orquestrar o fluxo de dados.  
> No entanto, devido às **restrições de acesso, API fechada e políticas anti-scraping do LinkedIn**, a ingestão de dados é realizada manualmente, tornando inviável a automação dessa etapa neste projeto.  
> Dessa forma, a orquestração foi mantida fora do escopo, sem impacto na modelagem analítica e nos insights gerados.


---
## 📂 Estrutura do Repositório

```text
├── data/
│   ├── raw/
│   │   ├── README.md
│   │   └── Vagas_Coletadas_Raw.xlsx
│   └── processed/
│       ├── README.md
│       └── Vagas_Coletadas_Cleaned.xlsx
│
├── docs/
│   ├── images/
│   └── README.md
│
├── models/
│   ├── sources/
│   └── gold/
│
├── scripts/
│   ├── ETL.py
│   └── README.md
│
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── dbt_project.yml
├── requirements.txt
├── LICENSE
└── README.md


```

---

# 📊 Evolução do Mercado por Senioridade

## 1. Contexto Global: A Explosão de Dados

O volume global de dados cresce em ritmo exponencial. Estudos de mercado indicam que **mais de 90% de todos os dados existentes no mundo foram gerados nos últimos dois anos**, com o total de dados estimado para alcançar **181 zettabytes até 2025**. Esse crescimento é impulsionado principalmente por:

- Cloud Computing  
- Internet of Things (IoT) 
- Streaming de vídeo e áudio  
- Inteligência Artificial e Machine Learning  
- Sistemas transacionais digitais em larga escala  

Esse aumento massivo torna inviável a gestão de dados apenas com soluções locais, manuais ou exclusivamente analíticas. **Dados em escala só podem ser gerenciados, processados e consumidos de forma eficiente em ambientes distribuídos e baseados em nuvem.**

Nesse contexto, a **Cloud deixa de ser uma tecnologia isolada** e passa a ser o **ambiente central** onde dados são gerados, armazenados e consumidos — impactando todos os níveis de senioridade, ainda que de formas diferentes.

Este projeto parte dessa realidade global para analisar **como o mercado brasileiro traduz essa explosão de dados em exigências técnicas concretas**, segmentadas por nível de senioridade.

>Fonte: [Gitnux Big Data & Analytics Market Report](https://www.gitnux.com/big-data-analytics-market-report-2024) 

---

## 2. Evolução por Senioridade

### 🔹 Júnior (101 Vagas)

**Visão Geral**  
O nível Júnior está concentrado no **consumo e visualização de dados**, com foco em ferramentas de BI e análise básica.  
Mesmo nesse estágio, o Cloud já aparece como diferencial, refletindo que **os dados analisados já nascem majoritariamente em ambientes de nuvem**.

**Exigências Técnicas**
- **Obrigatório:** Power BI (81,82%), Excel Avançado (59,60%) e SQL (55,56%)
- **Diferencial:** Python (27,03%), **Cloud** e Tableau (16,22%)

**Leitura Técnica**  
O profissional Júnior ainda não é responsável pela infraestrutura, mas já precisa **consumir dados hospedados em Cloud**.  
Isso explica a presença precoce do Cloud como diferencial, alinhada ao crescimento global do volume de dados.

<p align="center">
  <img src="./docs/images/Junior.png" width="100%">
</p>

---

### 🔹 Pleno (137 Vagas)

**Visão Geral**  
O nível Pleno representa o **ponto de transição estrutural** entre análise e engenharia analítica.  
Com o aumento do volume e da complexidade dos dados, o mercado passa a exigir profissionais capazes de **transformar, integrar e preparar dados em ambientes distribuídos**.

**Exigências Técnicas**
- **Obrigatório:** Power BI (82,84%), SQL (79,10%) e Python (62,69%)
- **Diferenciais estratégicos:** ETL (20,75%), **Cloud (16,98%)** e Tableau (15,09%)

**Leitura Técnica**  
Aqui, Python deixa de ser diferencial e passa a ser **fundamental**.  
O Cloud ganha força como diferencial estratégico, pois o profissional Pleno começa a atuar diretamente na **ponte entre dados brutos armazenados em nuvem e consumo analítico**.

<p align="center">
  <img src="./docs/images/Pleno.png" width="100%">
</p>

---

### 🔹 Sênior (64 Vagas)

**Visão Geral**  
No nível Sênior, o foco migra definitivamente da análise para **arquitetura, escala e governança de dados**.

Nesse estágio, o crescimento global de dados deixa de ser um contexto externo e passa a ser um **problema técnico direto**, exigindo soluções robustas e altamente confiáveis.

**Exigências Técnicas**
- **Obrigatório:** Power BI (89,06%), SQL (84,38%) e Python (71,88%)
- **Diferenciais dominantes:** **Cloud (50,00%)**, Big Data (38,46%) e ETL (23,08%)

**Leitura Técnica**  
A senioridade Sênior está associada à capacidade de **projetar e operar ambientes de dados em larga escala**, incluindo:

- Armazenamento distribuído em Cloud  
- Pipelines resilientes  
- Processamento em larga escala  
- Governança, segurança e confiabilidade dos dados  

Neste nível, **Cloud deixa de ser apenas diferencial técnico e se consolida como infraestrutura base**.

<p align="center">
  <img src="./docs/images/Senior.png" width="100%">
</p>

---

## 3. O Papel Estratégico do Tableau

Embora o **Power BI** concentre o maior volume de exigências ao longo da carreira, o **Tableau** se destaca como um diferencial competitivo relevante.

Seu pico ocorre no nível Pleno, onde:
- É o **3º maior diferencial técnico (15,09%)**
- Alcança **18,66% de necessidade** quando ferramentas básicas (SQL, Excel e Power BI) são desconsideradas

Isso indica que o Tableau atua como um **marcador de especialização**, especialmente em ambientes analíticos mais avançados e fora do ecossistema Microsoft.

---

## 4. Recomendações de Carreira

- **Júnior:**  
  Foco em Power BI, SQL e Excel Avançado.  
  Python, Tableau e **contato inicial com Cloud** funcionam como diferenciais importantes.

- **Pleno:**  
  Consolidação de Bibliotecas Python (Pandas, NumPy), ETL e SQL avançado.  
  **Cloud surge como diferencial estratégico**, refletindo a transição para ambientes de dados orientados à escala.

- **Sênior:**  
  Atuação consolidada em **Cloud como infraestrutura base**, com domínio de Big Data e orquestração de pipelines  
  (ex.: Apache Airflow), assumindo responsabilidade por **arquitetura, confiabilidade e escalabilidade**.

---

## 5. Conclusão

A análise evidencia que o crescimento exponencial do volume global de dados não é apenas um fenômeno tecnológico, mas um **fator estruturante do mercado de trabalho em dados**.

Em mercados mais maduros, especialmente no exterior, a **Cloud já se consolida como infraestrutura base**, refletindo a necessidade de lidar com volumes massivos de dados, pipelines distribuídos e ambientes altamente escaláveis. Esse movimento se manifesta de forma clara nos níveis Pleno e Sênior, onde Cloud deixa de ser diferencial e passa a ser requisito implícito.

No mercado brasileiro, os dados indicam que essa transição **já está em curso**. A presença crescente de Cloud como diferencial desde o nível Júnior sugere que o Brasil segue a mesma trajetória observada internacionalmente, ainda que em um estágio de maturidade anterior.

Dessa forma, a tendência é que o Cloud deixe progressivamente o papel de especialização e se consolide como **fundamento técnico obrigatório** ao longo da carreira em dados no Brasil, acompanhando a expansão contínua do volume, da complexidade e da criticidade dos dados.

