# Estrutura de Dados para Extração de Vagas do LinkedIn

Este documento descreve a **estrutura de abas do Excel** e o **prompt usado para extrair dados de vagas** do LinkedIn, gerando arquivos prontos para análise no Excel, Python ou SQL.

---

##  Estrutura das abas do Excel

### Aba `vagas`
ID, Empresa, Cargo, Modelo_Trab, Area_Atuacao, Data, Nível, Salario, Link_Vaga, Destaque, Localizacao, Tipo_Contratacao, Num_Candidatos, Idiomas, Beneficios, Departamento, Ferramentas_Específicas, Remoto, Categoria, Fonte_Vaga

### Aba `skills`
Colunas:  Vaga_ID, Skill, Tipo, Nivel_Conhecimento, Obrigatoria, Categoria

---

##  Critério de pesquisa no LinkedIn

As vagas foram coletadas manualmente a partir do LinkedIn utilizando a seguinte **query de busca**:

("analista de dados" OR "cientista de dados" OR "analista bi") AND (sql OR python OR excel OR "power bi")


---

##  Prompt para extrair dados do LinkedIn

```
Você vai receber a descrição completa de uma vaga de emprego.

Seu objetivo é extrair os dados para DUAS abas de Excel:

vagas

skills

⚠️ REGRAS CRÍTICAS (NÃO IGNORAR)

A aba "vagas" DEVE TER EXATAMENTE 20 COLUNAS, NA ORDEM FIXA ABAIXO.

A aba "skills" DEVE TER EXATAMENTE 6 COLUNAS, NA ORDEM FIXA ABAIXO.

Se uma informação não existir, deixe o campo VAZIO, mas mantenha o TAB.

⚠️ FORMATO OBRIGATÓRIO: TSV (TAB-SEPARATED VALUES)

Os campos DEVEM ser separados por TAB (não vírgula).

NÃO usar vírgulas como separador de colunas.

NÃO usar aspas para tratar vírgulas (vírgulas são permitidas dentro do texto).

NÃO criar colunas extras.

NÃO mover informações entre colunas.

NÃO explicar nada no output final.

==================================================
ABA "vagas" (1 linha por vaga)
ORDEM FIXA DAS COLUNAS (20):

ID
Empresa
Cargo
Modelo_Trab
Area_Atuacao
Data
Nível
Salario
Link_Vaga
Destaque
Localizacao
Tipo_Contratacao
Num_Candidatos
Idiomas
Beneficios
Departamento
Ferramentas_Específicas
Remoto
Categoria
Fonte_Vaga

==================================================
ABA "skills" (1 linha por skill)
ORDEM FIXA DAS COLUNAS (6):

Vaga_ID
Skill
Tipo
Nivel_Conhecimento
Obrigatoria
Categoria

==================================================
REGRAS DE EXTRAÇÃO

Data padrão se ausente: 18/01/2024

Nível SOMENTE se explícito: Júnior | Pleno | Sênior

Skills obrigatórias: termos como requisito, necessário, obrigatório

Skills diferenciais: termos como desejável, diferencial, plus

Nivel_Conhecimento somente se explícito

Obrigatoria:

Sim = obrigatória

Não = diferencial

Categoria da vaga: resumo da área principal (ex: Dados)

Fonte_Vaga: origem explícita (ex: LinkedIn)

Usar o MESMO ID da vaga em todas as skills

NÃO repetir cabeçalhos

NÃO agrupar múltiplas vagas

==================================================
FORMATO FINAL DE SAÍDA (POWERSHELL)

BLOCO 1 — ABA VAGAS
• Enviar APENAS 1 linha TSV
• Campos separados por TAB
• Exatamente 20 colunas
• NÃO adicionar comentários
• NÃO adicionar títulos
• NÃO adicionar linhas em branco

BLOCO 2 — ABA SKILLS
• Enviar múltiplas linhas TSV
• 1 skill por linha
• Campos separados por TAB
• Exatamente 6 colunas por linha
• NÃO adicionar comentários
• NÃO adicionar títulos

==================================================

Descrição da vaga:
[COLE AQUI A DESCRIÇÃO COMPLETA]

```
