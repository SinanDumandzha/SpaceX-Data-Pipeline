select * 
from dbt_spacex.launches;

select * 
from dbt_spacex.launches
where success = true;

select * 
from dbt_spacex.launches
order by launch_date desc;

select
    rocket,
    count(*) as launch_count
from dbt_spacex.launches
group by rocket;