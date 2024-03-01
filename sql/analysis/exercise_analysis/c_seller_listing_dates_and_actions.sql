SELECT 
    id_customer,
    MIN(date_created) AS first_listing_date,
    MAX(date_created) AS last_listing_date,
    MAX(date_sold) AS last_sale_date,
    MAX(CASE WHEN date_sold IS NOT NULL THEN 'Sale' ELSE 'List' END) AS last_action
FROM listings
GROUP BY id_customer;
