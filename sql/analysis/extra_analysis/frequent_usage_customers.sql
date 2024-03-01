SELECT
    id_customer,
    COUNT(*) AS listings_count
FROM listings
GROUP BY id_customer
HAVING COUNT(*) > 1
ORDER BY listings_count DESC
LIMIT 20;