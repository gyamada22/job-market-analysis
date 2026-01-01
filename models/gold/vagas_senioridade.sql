with source_data as (
    select *
    from {{ source('bronze_sources', 'VAGAS') }}
)

select
    senioridade,
    count(*) as vagas_totais,
    current_timestamp() as dbt_load_timestamp
from source_data
group by senioridade
