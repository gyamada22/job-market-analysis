with skill_dif as (
    select
        v.senioridade,
        s.skill,
        count(*) as qtde,
        row_number() over(partition by v.senioridade order by count(*) desc) as rn
    from {{ source('bronze_sources', 'SKILLS') }} s
    join {{ source('bronze_sources', 'VAGAS') }} v on s.vaga_id = v.id
    where s.requisito = 'Diferencial'
      and s.skill not in ('Outra Skill','SQL')
    group by v.senioridade, s.skill
)
select senioridade, skill, qtde, current_timestamp() as dbt_load_timestamp
from skill_dif
where rn <= 3
order by senioridade, qtde desc
