CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    category_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    quantity INT NOT NULL,
    available BOOLEAN DEFAULT TRUE,
    updated_at TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

INSERT INTO categories (name) VALUES
('Electronics'),
('Books'),
('Clothes');

INSERT INTO products (category_id, name, price, quantity, available) VALUES
(1, 'Laptop', 2500, 5, TRUE),
(1, 'Mouse', 50, 20, TRUE),
(2, 'Book 1', 30, 10, TRUE),
(3, 'T-Shirt', 40, 0, FALSE);

CREATE VIEW all_products_view AS
SELECT * FROM products;

CREATE VIEW filtered_products_view AS
SELECT * FROM products
WHERE available = TRUE;

CREATE VIEW products_categories_view AS
SELECT 
    products.product_id,
    products.category_id,
    products.name AS product_name,
    products.price,
    products.quantity,
    products.available,
    products.updated_at,
    categories.name AS category_name
FROM products
JOIN categories ON products.category_id = categories.category_id;

CREATE OR REPLACE VIEW filtered_products_view AS
SELECT * FROM products
WHERE price > 1000;

CREATE OR REPLACE VIEW products_categories_view AS
SELECT 
    products.product_id,
    products.category_id,
    products.name AS product_name,
    products.price,
    products.quantity,
    products.available,
    products.updated_at,
    categories.name AS category_name,
    products.price * products.quantity AS total_price
FROM products
JOIN categories ON products.category_id = categories.category_id;

DROP VIEW all_products_view;
DROP VIEW filtered_products_view;
DROP VIEW products_categories_view;

CREATE OR REPLACE PROCEDURE delete_product_by_id(p_id INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM products
    WHERE product_id = p_id;
END;
$$;

CREATE OR REPLACE PROCEDURE update_product_quantity(p_id INT, new_quantity INT)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE products
    SET 
        quantity = new_quantity,
        available = new_quantity > 0
    WHERE product_id = p_id;
END;
$$;

CREATE OR REPLACE FUNCTION set_product_update_time()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$;

CREATE TRIGGER product_update_trigger
BEFORE UPDATE ON products
FOR EACH ROW
EXECUTE FUNCTION set_product_update_time();