SELECT b.brand, COUNT(*) AS total_listings
FROM listings l
JOIN brands b ON l.id_brand = b.id_brand
GROUP BY b.brand
ORDER BY total_listings DESC
LIMIT 10;