WITH ListingTime AS (
    SELECT
        EXTRACT(EPOCH FROM (MAX(datetime_session) - MIN(datetime_session))) / 60 AS time_spent_minutes
    FROM clicks
    GROUP BY id_product
)
SELECT
    AVG(time_spent_minutes) AS avg_time_spent_minutes
FROM ListingTime;
