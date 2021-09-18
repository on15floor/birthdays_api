CREATE TABLE users_roles(
    [id] [INTEGER] PRIMARY KEY AUTOINCREMENT NOT NULL,
    [role_name] [NVARCHAR](16) NOT NULL
);

INSERT INTO users_roles
    ( role_name )
VALUES
    ('admin'),
    ('user');
