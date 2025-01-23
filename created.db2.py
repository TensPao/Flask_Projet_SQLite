
import sqlite3

# Connexion à la base SQLite
connection = sqlite3.connect('database2.db')

# Création du schéma de la base de données
connection.executescript('''
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    adresse TEXT NOT NULL
);
''')

# Insertion des données dans la table clients
cur = connection.cursor()

cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)", ('DUPONT', 'Emilie', '123 Rue des Lilas, 75001 Paris'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)", ('LEROUX', 'Lucas', '456 Avenue du Soleil, 31000 Toulouse'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)", ('MARTIN', 'Amandine', '789 Rue des Érables, 69002 Lyon'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)", ('TREMBLAY', 'Antoine', '1010 Boulevard de la Mer, 13008 Marseille'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)", ('LAMBERT', 'Sarah', '222 Avenue de la Liberté, 59000 Lille'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)", ('GAGNON', 'Nicolas', '456 Boulevard des Cerisiers, 69003 Lyon'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)", ('DUBOIS', 'Charlotte', '789 Rue des Roses, 13005 Marseille'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)", ('LEFEVRE', 'Thomas', '333 Rue de la Paix, 75002 Paris'))

# Sauvegarde des modifications dans la base de données
connection.commit()

# Fermeture de la connexion
connection.close()
