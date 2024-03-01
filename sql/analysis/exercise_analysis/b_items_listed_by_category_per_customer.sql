SELECT 
    l.id_customer,
    BOOL_OR(c.category = 'Clothing') AS listed_clothing,
    BOOL_OR(c.category = 'Bags') AS listed_bags,
    BOOL_OR(c.category = 'Shoes') AS listed_shoes,
    BOOL_OR(c.category = 'Accessories') AS listed_accessories
FROM listings l
JOIN category c ON l.id_category = c.id_category
GROUP BY l.id_customer;
