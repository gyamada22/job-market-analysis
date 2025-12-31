-- 1. volume de vagas por senioridade
select 
    senioridade,
    count(*) as vagas_totais
from vagas
group by senioridade;

--------------------------------------------------

-- 2. top 3 skills obrigatória por senioridade
with skill_obg as (
    select
        v.senioridade,
        s.skill,
        count(*) as qtde,
        row_number() over(partition by v.senioridade order by count(*) desc) as rn
    from skills s
    join vagas v on s.vaga_id = v.id
    where s.requisito = 'Obrigatório'
    group by v.senioridade, s.skill
)
select senioridade, skill, qtde
from skill_obg
where rn <= 3
order by senioridade, qtde desc;

--------------------------------------------------

-- 3. top 3 skills diferenciais por senioridade
with skill_dif as (
    select
        v.senioridade,
        s.skill,
        count(*) as qtde,
        row_number() over(partition by v.senioridade order by count(*) desc) as rn
    from skills s
    join vagas v on s.vaga_id = v.id
    where s.requisito = 'Diferencial'
      and s.skill <> 'Outra Skill'
      and s.skill <> 'SQL'
    group by v.senioridade, s.skill
)
select senioridade, skill, qtde
from skill_dif
where rn <= 3
order by senioridade, qtde desc;

--------------------------------------------------

-- distribuição de vagas por estado
select 
    estado,
    count(*) as qtde_vagas
from vagas
group by estado
order by qtde_vagas desc;

--------------------------------------------------

-- percentual do total de vagas por estado
with totalvagas as (
    select count(*) as total from vagas
)
select 
    v.estado,
    count(*) as qtd_vagas,
    cast(count(*) * 100.0 / t.total as decimal(5,2)) as percentual
from vagas v
cross join totalvagas t
group by v.estado, t.total
order by qtd_vagas desc;

--------------------------------------------------

-- distribuição de vagas por modalidade (remoto, híbrido, presencial)
select modalidade, count(*) as qtde_vagas
from vagas
group by modalidade
order by qtde_vagas desc;

--------------------------------------------------

-- top 5 setores por quantidade de vagas
select top 5
    setor,
    count(*) as qtde_vagas
from vagas
group by setor
order by count(*) desc;

--------------------------------------------------

-- top 5 skills obrigatórias por setor (apenas para os top 5 setores)
with top5setores as (
    select top 5 setor
    from vagas
    group by setor
    order by count(*) desc
)
select *
from (
    select 
        v.setor,
        s.skill,
        count(*) as qtde,
        row_number() over(partition by v.setor order by count(*) desc) as rn
    from skills s
    join vagas v on s.vaga_id = v.id
    where s.requisito = 'Obrigatório'
      and s.skill <> 'Outra Skill'
      and v.setor in (select setor from top5setores)
    group by v.setor, s.skill
) t
where rn <= 5
order by setor, qtde desc;

--------------------------------------------------

-- top 5 skills diferenciais por setor (top 5 setores)
with top5setores as (
    select top 5 setor
    from vagas
    group by setor
    order by count(*) desc
)
select *
from (
    select 
        v.setor,
        s.skill,
        count(*) as qtde,
        row_number() over(partition by v.setor order by count(*) desc) as rn
    from skills s
    join vagas v on s.vaga_id = v.id
    where s.requisito = 'Diferencial'
      and s.skill <> 'Outra Skill'
      and v.setor in (select setor from top5setores)
    group by v.setor, s.skill
) t
where rn <= 5
order by setor, qtde desc;

