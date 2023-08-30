DROP TABLE transactions;
DROP TABLE tags;
DROP TABLE merchants;
DROP TABLE budgets;

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    deactivated BOOLEAN
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    deactivated BOOLEAN
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    merchant_id INT NOT NULL REFERENCES merchants(id),
    tag_id INT NOT NULL REFERENCES tags(id),
    amount REAL,
    timestamp TIMESTAMP
);

CREATE TABLE budgets (
    id SERIAL PRIMARY KEY,
    amount REAL
);