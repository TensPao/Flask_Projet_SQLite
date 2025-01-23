-- Table pour gérer les utilisateurs
CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone_number TEXT,
    registration_date DATE DEFAULT (DATE('now'))
);

-- Table pour gérer les livres
CREATE TABLE Books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    genre TEXT,
    publication_year INTEGER,
    stock INTEGER NOT NULL DEFAULT 0
);

-- Table pour enregistrer les emprunts de livres
CREATE TABLE BookLoans (
    loan_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    loan_date DATE DEFAULT (DATE('now')),
    return_date DATE,
    is_returned BOOLEAN DEFAULT 0,
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

#Infos utiles
-- Requête pour ajouter un livre
-- INSERT INTO Books (title, author, genre, publication_year, stock) VALUES ('Titre', 'Auteur', 'Genre', 2023, 10);

-- Requête pour supprimer un livre
-- DELETE FROM Books WHERE book_id = ?;

-- Requête pour rechercher des livres disponibles
-- SELECT * FROM Books WHERE stock > 0;

-- Requête pour emprunter un livre
-- INSERT INTO BookLoans (book_id, user_id) VALUES (?, ?);
-- UPDATE Books SET stock = stock - 1 WHERE book_id = ?;

-- Requête pour retourner un livre
-- UPDATE BookLoans SET is_returned = 1, return_date = DATE('now') WHERE loan_id = ?;
-- UPDATE Books SET stock = stock + 1 WHERE book_id = ?;

