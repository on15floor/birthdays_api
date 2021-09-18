CREATE TABLE birthdays(
    [id] [INTEGER] PRIMARY KEY AUTOINCREMENT NOT NULL,
    [created_date] DATE DEFAULT (DATETIME('now')),
    [user_id] [INT] NOT NULL,
    [name] [NVARCHAR](300) NOT NULL,
    [gender] [NVARCHAR](1) NOT NULL,
    [birthday] DATE NOT NULL,
    [comment] [NVARCHAR](300) NOT NULL
);

INSERT INTO birthdays
    ( user_id, name, gender, birthday, comment )
VALUES
    (2, 'Олейников Валентин Глебович', 'M', '1990-10-21', 'Яндекс'),
    (2, 'Потапенко Алексей Валерьевич', 'M', '1994-08-01', 'Почта России'),
    (3, 'Федорова Алина Игоревна', 'F', '1993-12-13', 'Школа'),
    (3, 'Денисенко Василий Петрович', 'M', '1990-09-12', 'Школа'),
    (3, 'Климова Мария Ивановна', 'F', '1989-10-03', 'Школа'),
    (4, 'Крестьянинова Ирина Владимировна', 'F', '1995-11-30', 'Институт'),
    (4, 'Галас Андрей Андреевич', 'M', '1992-10-08', 'Работа');