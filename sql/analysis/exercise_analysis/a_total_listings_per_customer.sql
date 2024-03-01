SELECT 
    id_customer,
    COUNT(id) AS total_listings_started,
    COUNT(date_completed) AS listings_completed,
    COUNT(date_sold) AS listings_sold
FROM listings
GROUP BY id_customer
ORDER BY total_listings_started DESC;
