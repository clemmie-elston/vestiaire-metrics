SELECT
    l.id AS listing_id,
    l.id_customer,
    max(c.datetime_session) AS last_action_time,
    c.event_action AS last_action,
    c.event_label AS action_detail
FROM
    listings l
LEFT JOIN clicks c ON l.id = id_product
WHERE
    l.date_completed IS NULL
GROUP BY
    l.id, l.id_customer, c.event_action, c.event_label
ORDER BY
    l.id, last_action_time DESC;


