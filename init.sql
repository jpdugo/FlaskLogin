CREATE DATABASE IF NOT EXISTS AccessControl;
USE AccessControl;

CREATE TABLE status (
    id TINYINT PRIMARY KEY,
    description VARCHAR(50)
);

CREATE TABLE user (
    dni VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100),
    lastName VARCHAR(100),
    status_id TINYINT,
    FOREIGN KEY (status_id) REFERENCES status(id)
);

INSERT INTO status (id, description) VALUES
(1, 'autorizado'),
(2, 'denegado');

INSERT INTO user (dni, name, lastName, status_id) VALUES
('38888840', 'John', 'Doe', 1),
('38888841', 'Jane', 'Doe', 2),
('38888842', 'Alice', 'Smith', 1),
('38888843', 'Bob', 'Johnson', 1),
('38888844', 'Charlie', 'Brown', 1),
('38888845', 'David', 'Wilson', 1),
('38888846', 'Eve', 'Davis', 1),
('38888847', 'Frank', 'Miller', 1),
('38888848', 'Grace', 'Taylor', 1),
('38888849', 'Hank', 'Anderson', 1),
('38888850', 'Ivy', 'Thomas', 1),
('38888851', 'Jack', 'Moore', 1),
('38888852', 'Kara', 'Martin', 1),
('38888853', 'Leo', 'Jackson', 1),
('38888854', 'Mia', 'White', 1),
('38888855', 'Nina', 'Harris', 1),
('38888856', 'Oscar', 'Clark', 2),
('38888857', 'Paul', 'Lewis', 1),
('38888858', 'Quinn', 'Robinson', 1),
('38888859', 'Ruth', 'Walker', 1);

