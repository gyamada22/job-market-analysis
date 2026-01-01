with totalvagas as (
    select count(*) as total from {{ source('bronze_sources', 'VAGAS') }}
)
select 
    v.estado,
    count(*) as qtd_vagas,
    count(*) * 100.0 / t.total as percentual,
    current_timestamp() as dbt_load_timestamp
from {{ source('bronze_sources', 'VAGAS') }} v
cross join totalvagas t
group by v.estado, t.total
order by qtd_vagas desc
