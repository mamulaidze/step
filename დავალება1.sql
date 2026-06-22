CREATE TABLE cars (
    car_id SERIAL PRIMARY KEY,
    brand VARCHAR(50) NOT NULL,
    release_year INT NOT NULL,
    vin_code VARCHAR(17) UNIQUE,
    added_date DATE DEFAULT CURRENT_DATE,
    engine_volume DECIMAL(3,1) CHECK (engine_volume > 0.5),
    millage_km INT,
    price DECIMAL(10,2),
    description TEXT,
    is_sold BOOLEAN NOT NULL DEFAULT FALSE
);

 -- მანქანების შეყვანა
INSERT INTO cars
(brand, release_year, vin_code, engine_volume, millage_km, price, description, is_sold)
VALUES
('Toyota', 2015, 'JTDBR32E520123456', 1.8, 180000, 8500.00, 'ჰიბრიდული ავტომობილი', FALSE),

('BMW', 2014, 'WBA3A5C50DF123456', 2.0, 160000, 12500.00, 'კარგ მდგომარეობაში', FALSE),

('Mercedes', 2016, 'WDDWF4KB1GR123456', 2.0, 140000, 15800.00, 'კომფორტული სედანი', FALSE),

('Honda', 2013, 'JHMGK5850DS123456', 1.5, 120000, 6200.00, 'ეკონომიური მანქანა', FALSE),

('Ford', 2017, '3FA6P0HD4HR123456', 2.5, 110000, 10500.00, 'ამერიკული წარმოება', FALSE),

('Hyundai', 2018, 'KMHD84LF8JU123456', 1.6, 90000, 9800.00, 'დაბალი გარბენით', FALSE),

('Kia', 2016, '5XXGT4L30GG123456', 2.4, 135000, 9000.00, 'კარგი ვიზუალური მდგომარეობა', TRUE),

('Nissan', 2015, '1N4AZ0CP5FC123456', 0.8, 80000, 7000.00, 'ელექტრო ავტომობილი', FALSE),

('Subaru', 2014, 'JF2SJABC4EH123456', 2.5, 170000, 11200.00, '4x4 გამავლობა', FALSE),

('Lexus', 2012, 'JTJBK1BA9C2123456', 3.5, 190000, 14500.00, 'პრემიუმ კლასის SUV', TRUE);