WITH SubmittedListings AS (
    SELECT
        l.ID AS listing_id,
        COUNT(c.ID_PRODUCT) AS total_clicks
    FROM
        listings l
        JOIN clicks c ON CAST(c.ID_PRODUCT AS BIGINT) = l.ID -- Adjust type casting as necessary
    WHERE
        l.DATE_COMPLETED IS NOT NULL
    GROUP BY
        l.ID
),
ClicksRanked AS (
    SELECT
        listing_id,
        total_clicks,
        ROW_NUMBER() OVER (ORDER BY total_clicks) AS row_number,
        COUNT(*) OVER () AS total_listings
    FROM
        SubmittedListings
),
MedianCalc AS (
    SELECT
        total_clicks
    FROM
        ClicksRanked
    WHERE
        row_number IN (total_listings / 2, (total_listings / 2) + 1, (total_listings + 1) / 2)
)
SELECT
    AVG(total_clicks) AS median_clicks
FROM
    MedianCalc;
