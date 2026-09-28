{{
  config({    
    "materialized": "ephemeral",
    "database": "pipelinehub",
    "schema": "drew"
  })
}}

WITH single_value_query AS (

  {#Returns a fixed value for use in simple checks or testing.#}
  SELECT 1 AS a

)

SELECT *

FROM single_value_query
