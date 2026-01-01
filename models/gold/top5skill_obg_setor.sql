with top5setores as (
    select setor
    from {{ source('bronze_sources', 'VAGAS') }}
    group by setor
    order by count(*) desc
    limit 5
)
select *
from (
    select 
        v.setor,
        s.skill,
        count(*) as qtde,
        row_number() over(partition by v.setor order by count(*) desc) as rn
    from {{ source('bronze_sources', 'SKILLS') }} s
    join {{ source('bronze_sources', 'VAGAS') }} v on s.vaga_id = v.id
    where s.requisito = 'Obrigatório'
      and s.skill <> 'Outra Skill'
      and v.setor in (select setor from top5setores)
    group by v.setor, s.skill
) t
where rn <= 5
order by setor, qtde desc
