SELECT c.category, COUNT(*) AS total_listings
FROM listings l
JOIN category c ON l.id_category = c.id_category
GROUP BY c.category
ORDER BY total_listings DESC
LIMIT 10;