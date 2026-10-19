{{
  config({    
    "materialized": "ephemeral",
    "database": "workspace",
    "schema": "default"
  })
}}

WITH single_value_query AS (

  {#Returns a fixed value for testing or validation purposes.#}
  SELECT 1 AS a

)

SELECT *

FROM single_value_query
