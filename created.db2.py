import sqlite3

# Connexion à la base SQLite
connection = sqlite3.connect('database.db')

# Création du schéma de la base de données pour les livres
connection.executescript('''
CREATE TABLE IF NOT EXISTS livres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titre TEXT NOT NULL,
    auteur TEXT NOT NULL,
    genre TEXT NOT NULL,
    annee_publication INTEGER NOT NULL,
    stock INTEGER NOT NULL DEFAULT 1
);
''')

# Insertion des données dans la table livres
cur = connection.cursor()

cur.execute("INSERT INTO livres (titre, auteur, genre, annee_publication, stock) VALUES (?, ?, ?, ?, ?)", 
            ('Le Petit Prince', 'Antoine de Saint-Exupéry', 'Fiction', 1943, 10))
cur.execute("INSERT INTO livres (titre, auteur, genre, annee_publication, stock) VALUES (?, ?, ?, ?, ?)", 
            ('Les Misérables', 'Victor Hugo', 'Classique', 1862, 5))
cur.execute("INSERT INTO livres (titre, auteur, genre, annee_publication, stock) VALUES (?, ?, ?, ?, ?)", 
            ('L’Étranger', 'Albert Camus', 'Philosophie', 1942, 8))
cur.execute("INSERT INTO livres (titre, auteur, genre, annee_publication, stock) VALUES (?, ?, ?, ?, ?)", 
            ('1984', 'George Orwell', 'Science-fiction', 1949, 12))
cur.execute("INSERT INTO livres (titre, auteur, genre, annee_publication, stock) VALUES (?, ?, ?, ?, ?)", 
            ('Le Rouge et le Noir', 'Stendhal', 'Classique', 1830, 4))
cur.execute("INSERT INTO livres (titre, auteur, genre, annee_publication, stock) VALUES (?, ?, ?, ?, ?)", 
            ('Harry Potter à l’école des sorciers', 'J.K. Rowling', 'Fantasy', 1997, 20))
cur.execute("INSERT INTO livres (titre, auteur, genre, annee_publication, stock) VALUES (?, ?, ?, ?, ?)", 
            ('La Peste', 'Albert Camus', 'Philosophie', 1947, 6))
cur.execute("INSERT INTO livres (titre, auteur, genre, annee_publication, stock) VALUES (?, ?, ?, ?, ?)", 
            ('Don Quichotte', 'Miguel de Cervantes', 'Aventure', 1605, 3))

# Sauvegarde des modifications dans la base de données
connection.commit()

# Fermeture de la connexion
connection.close()
