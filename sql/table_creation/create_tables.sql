CREATE TABLE brands (
    id_brand SERIAL PRIMARY KEY,
    brand VARCHAR(255) NOT NULL
);

CREATE TABLE category (
    id_category SERIAL PRIMARY KEY,
    category VARCHAR(255) NOT NULL
);

CREATE TABLE clicks (
    datetime_session TIMESTAMP NOT NULL,
    id_user VARCHAR(255) NOT NULL,
    id_product NUMERIC,
    event_category VARCHAR(255) NOT NULL,
    event_action VARCHAR(255) NOT NULL,
    event_label VARCHAR(255) 
);

CREATE TABLE listings (
    id SERIAL PRIMARY KEY,
    id_customer VARCHAR(255) NOT NULL,
    id_brand INT NOT NULL,
    id_category INT NOT NULL,
    date_created TIMESTAMP NOT NULL,
    date_completed TIMESTAMP,  
    date_sold TIMESTAMP, 
    FOREIGN KEY (id_brand) REFERENCES brands(id_brand),
    FOREIGN KEY (id_category) REFERENCES category(id_category)
);
