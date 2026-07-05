CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    location VARCHAR(50) NOT NULL
);

CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    salary DECIMAL(10,2) NOT NULL,
    department_id INT NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

INSERT INTO departments (name, location) VALUES
('IT', 'New York'),
('Marketing', 'Los Angeles'),
('Finance', 'Chicago'),
('HR', 'New York');

INSERT INTO employees (name, salary, department_id) VALUES
('Giorgi', 2500, 1),
('Nino', 1800, 2),
('Luka', 3200, 1),
('Mariam', 1500, 3),
('Saba', 2200, 4),
('Ana', 1700, 2),
('Dato', 4000, 1),
('Elene', 2800, 4);

SELECT name, salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);

SELECT 
    name,
    salary,
    (
        SELECT departments.name
        FROM departments
        WHERE departments.department_id = employees.department_id
    ) AS department_name
FROM employees;

SELECT *
FROM employees
WHERE department_id IN (
    SELECT department_id
    FROM departments
    WHERE location = 'New York'
);

SELECT *
FROM departments
WHERE EXISTS (
    SELECT 1
    FROM employees
    WHERE employees.department_id = departments.department_id
);

SELECT *
FROM employees
WHERE salary > ANY (
    SELECT salary
    FROM employees
    WHERE department_id = (
        SELECT department_id
        FROM departments
        WHERE name = 'Marketing'
    )
);

SELECT *
FROM employees
WHERE salary > ALL (
    SELECT salary
    FROM employees
    WHERE department_id = (
        SELECT department_id
        FROM departments
        WHERE name = 'IT'
    )
);

SELECT name, salary
FROM employees
WHERE department_id IN (
    SELECT department_id
    FROM departments
    WHERE location = 'New York'
)

UNION

SELECT name, salary
FROM employees
WHERE department_id IN (
    SELECT department_id
    FROM departments
    WHERE location = 'Los Angeles'
);

SELECT name, salary
FROM employees
WHERE department_id IN (
    SELECT department_id
    FROM departments
    WHERE location = 'New York'
)

UNION ALL

SELECT name, salary
FROM employees
WHERE department_id IN (
    SELECT department_id
    FROM departments
    WHERE location = 'Los Angeles'
);