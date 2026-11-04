CREATE SCHEMA shop;

CREATE TABLE shop.customers (
    id            int PRIMARY KEY,
    name          text NOT NULL,
    city          text NOT NULL,
    registered_at timestamp NOT NULL
);

CREATE TABLE shop.categories (
    id   int PRIMARY KEY,
    name text NOT NULL
);

CREATE TABLE shop.products (
    id          int PRIMARY KEY,
    name        text NOT NULL,
    category_id int NOT NULL REFERENCES shop.categories (id),
    price       numeric NOT NULL
);

CREATE TABLE shop.orders (
    id          int PRIMARY KEY,
    customer_id int REFERENCES shop.customers (id),
    created_at  timestamp NOT NULL,
    status      text NOT NULL CHECK (status IN ('paid', 'shipped', 'delivered', 'pending', 'cancelled'))
);

CREATE TABLE shop.order_items (
    id         int PRIMARY KEY,
    order_id   int NOT NULL REFERENCES shop.orders (id),
    product_id int REFERENCES shop.products (id),
    qty        int NOT NULL,
    price      numeric(10,2) NOT NULL,
    discount   numeric(4,3) NOT NULL
);

CREATE ROLE student LOGIN PASSWORD 'student';
GRANT USAGE ON SCHEMA shop TO student;
GRANT SELECT ON ALL TABLES IN SCHEMA shop TO student;
ALTER ROLE student SET search_path = shop;
ALTER ROLE student SET timezone = 'Europe/Moscow';
ALTER ROLE student SET statement_timeout = '5s';
ALTER ROLE student SET default_transaction_read_only = on;
