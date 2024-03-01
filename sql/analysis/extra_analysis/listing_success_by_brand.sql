SELECT
    b.brand,
    COUNT(DISTINCT CASE WHEN l.date_sold IS NOT NULL THEN l.id END) AS sold_listings,
    COUNT(l.id) AS total_listings,
    (COUNT(DISTINCT CASE WHEN l.date_sold IS NOT NULL THEN l.id END)::FLOAT / COUNT(l.id)) * 100 AS success_rate
FROM listings l
JOIN brands b ON l.id_brand = b.id_brand
GROUP BY b.brand
HAVING COUNT(l.id) > 10
ORDER BY success_rate DESC, sold_listings DESC
LIMIT 10;