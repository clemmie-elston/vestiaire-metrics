SELECT
    c.category,
    COUNT(DISTINCT CASE WHEN l.date_completed IS NOT NULL THEN l.id END) AS completed_listings,
    COUNT(l.id) AS started_listings,
    (COUNT(DISTINCT CASE WHEN l.date_completed IS NOT NULL THEN l.id END)::FLOAT / COUNT(l.id)) * 100 AS conversion_rate
FROM listings l
JOIN category c ON l.id_category = c.id_category
GROUP BY c.category
ORDER BY conversion_rate DESC;