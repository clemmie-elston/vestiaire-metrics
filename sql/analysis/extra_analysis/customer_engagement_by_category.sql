SELECT cat.category, COUNT(clk.id_product) AS total_clicks
FROM clicks clk
JOIN listings lst ON CAST(clk.id_product AS NUMERIC) = lst.id -- Adjust casting as needed
JOIN category cat ON lst.id_category = cat.id_category
GROUP BY cat.category
ORDER BY total_clicks DESC;