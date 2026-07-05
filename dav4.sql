CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    quantity INT NOT NULL,
    status VARCHAR(30)
);

CREATE OR REPLACE PROCEDURE decrease_product_quantity(p_id INT, p_quantity INT)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE products
    SET quantity = quantity - p_quantity
    WHERE product_id = p_id;
END;
$$;

CREATE OR REPLACE FUNCTION set_product_status()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    IF NEW.quantity <= 0 THEN
        NEW.status = 'out of stock';
    ELSIF NEW.quantity BETWEEN 1 AND 10 THEN
        NEW.status = 'low stock';
    ELSE
        NEW.status = 'in stock';
    END IF;

    RETURN NEW;
END;
$$;

CREATE TRIGGER product_status_trigger
BEFORE INSERT OR UPDATE ON products
FOR EACH ROW
EXECUTE FUNCTION set_product_status();

INSERT INTO products (name, price, quantity) VALUES
('Laptop', 2500.00, 15),
('Mouse', 50.00, 8),
('Keyboard', 120.00, 0),
('Book', 30.00, 25),
('T-Shirt', 40.00, 5);

SELECT * FROM products;

CALL decrease_product_quantity(1, 7);

SELECT * FROM products;