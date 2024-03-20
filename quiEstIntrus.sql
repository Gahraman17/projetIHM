-- Active: 1710963252280@@127.0.0.1@3306
-- Création de la table des joueurs
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE
);

-- Création de la table des catégories de jeux
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY,
    name TEXT
);

-- Création de la table des questions
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY, category_id INTEGER, text TEXT, option1 TEXT, option2 TEXT, option3 TEXT, correct_option INTEGER, explication TEXT, FOREIGN KEY (category_id) REFERENCES categories (id)
);

-- Création de la table des scores des joueurs
CREATE TABLE IF NOT EXISTS scores (
    id INTEGER PRIMARY KEY,
    player_id INTEGER,
    category_id INTEGER,
    score INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(id)
    FOREIGN KEY (player_id) REFERENCES players(id)
);
