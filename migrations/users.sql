CREATE TABLE users(
    [user_id] [INTEGER] PRIMARY KEY AUTOINCREMENT NOT NULL,
    [created_date] DATE DEFAULT (DATETIME('now')),
    [first_name] [NVARCHAR](100) NOT NULL,
    [last_name] [NVARCHAR](100) NOT NULL,
    [email] [NVARCHAR](100) NOT NULL,
    [password] [NVARCHAR](64) NOT NULL,
    [role_id] [INT] NOT NULL
);

INSERT INTO users
    ( first_name, last_name, email, password, role_id )
VALUES
-- AdminPassword123, UserPassword123
    ('Александр', 'Анисимов', 'a.anisimov@lab15.ru', '$2b$10$dF0QAgmohuJ34MzKL9fCieBkepU6a7vnbXQ2brAtPjOg1lEib7gtu', 1),
    ('Алексей', 'Петров', 'a.petrov@lab15.ru', '$2b$10$YwRxo3gUOAoOgOxSTkgtsONW7oIxwtauMcvilM0gPqLT1V06pDYx2', 2),
    ('Сергей', 'Иванов', 's.ivanov@lab15.ru', '$2b$10$YwRxo3gUOAoOgOxSTkgtsONW7oIxwtauMcvilM0gPqLT1V06pDYx2', 2),
    ('Михаил', 'Сидоров', 'm.sidorov@lab15.ru', '$2b$10$YwRxo3gUOAoOgOxSTkgtsONW7oIxwtauMcvilM0gPqLT1V06pDYx2', 2);
