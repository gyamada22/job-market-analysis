select
    estado,
    count(*) as qtde_vagas,
    current_timestamp() as dbt_load_timestamp
from {{ source('bronze_sources', 'VAGAS') }}
group by estado
order by qtde_vagas desc
