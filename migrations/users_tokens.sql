CREATE TABLE users_tokens(
    [id] [INTEGER] PRIMARY KEY AUTOINCREMENT NOT NULL,
    [user_id] [INTEGER] NOT NULL,
    [created_date] DATE DEFAULT (DATETIME('now')),
    [token] [NVARCHAR](32) NOT NULL,
    [token_expired] DATE NOT NULL
);