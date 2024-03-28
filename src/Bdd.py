# -*- coding: utf-8 -*-
"""
Code source du projet Cherchez l'intrus

@author : fredt,akram,abdou

classe BaseDeDonnees 
"""

import sqlite3
from Question import Question
from Categorie import Categorie

class BaseDeDonnees:
    def __init__(self, nom_db):
        # Initialisation de la connexion à la base de données
        self.connexion = sqlite3.connect(nom_db)
        # Initialisation du curseur pour exécuter des requêtes SQL
        self.curseur = self.connexion.cursor()


    def create_tables(self):
        """ Créer les tables dans la base de données """
        if self.connexion is not None:
            try:
                # Création de la table des joueurs
                self.connexion.execute('''CREATE TABLE IF NOT EXISTS players (
                                    id INTEGER PRIMARY KEY,
                                    username TEXT UNIQUE
                                )''')

                # Création de la table des catégories
                self.connexion.execute('''CREATE TABLE IF NOT EXISTS categories (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT
                                )''')

                # Création de la table des questions
                self.connexion.execute('''CREATE TABLE IF NOT EXISTS questions (
                                    id INTEGER PRIMARY KEY,
                                    category_id INTEGER,
                                    text TEXT,
                                    option1 TEXT,
                                    option2 TEXT,
                                    option3 TEXT,
                                    correct_option INTEGER,
                                    explication TEXT,
                                    FOREIGN KEY (category_id) REFERENCES categories (id)
                                )''')

                # Création de la table des scores
                self.connexion.execute('''CREATE TABLE IF NOT EXISTS scores (
                                    id INTEGER PRIMARY KEY,
                                    player_id INTEGER,
                                    category_id INTEGER,
                                    score INTEGER,
                                    FOREIGN KEY (category_id) REFERENCES categories(id),
                                    FOREIGN KEY (player_id) REFERENCES players(id)
                                )''')

            except sqlite3.Error as e:
                print(e)

    def close_connection(self):
        """ Fermer la connexion à la base de données """
        if self.connexion is not None:
            self.connexion.close()

    def insert_questions_from_sql_file(self, sql_file):
        """ Insérer des questions à partir d'un fichier SQL """
        try:
            with open(sql_file, 'r',encoding='utf-8') as f:
                sql_commands = f.read().split(';')  # Séparer les commandes SQL

                for command in sql_commands:
                    command = command.strip()
                    if command:
                        self.connexion.execute(command)  # Exécuter la commande SQL
                        self.connexion.commit()

            print("Insertion des questions terminée avec succès.")
        except sqlite3.Error as e:
            print("Erreur lors de l'insertion des questions :", e)



#******************************************************************************************
    def obtenir_categories(self):
        # Exécute une requête SQL pour récupérer les catégories depuis la base de données
        self.curseur.execute("SELECT id, name FROM categories")
        # Crée une liste d'instances de la classe Categorie à partir des résultats de la requête SQL
        return [Categorie(id=cat[0], nom=cat[1]) for cat in self.curseur.fetchall()]

    def obtenir_questions_par_categorie(self, id_categorie):
        # Exécute une requête SQL pour récupérer les questions pour une catégorie spécifique
        self.curseur.execute("SELECT id, category_id, text, option1, option2, option3, correct_option, explication FROM questions WHERE category_id=?", (id_categorie,))
        # Crée une liste d'instances de la classe Question à partir des résultats de la requête SQL
        return [Question(question[0], question[1], question[2], question[3:6], question[6], question[7]) for question in self.curseur.fetchall()]

    def inserer_score(self, nom_joueur, id_categorie, score):
        # Exécute une requête SQL pour insérer un nouveau score dans la table des scores
        self.curseur.execute("INSERT INTO scores (player_name, category_id, score) VALUES (?, ?, ?)", (nom_joueur, id_categorie, score))
        # Valide la transaction en commitant les changements dans la base de données
        self.connexion.commit()

    def obtenir_meilleur_score(self, nom_joueur, id_categorie):
        # Exécute une requête SQL pour récupérer le meilleur score d'un joueur pour une catégorie spécifique
        self.curseur.execute("SELECT MAX(score) FROM scores WHERE player_name=? AND category_id=?", (nom_joueur, id_categorie))
        # Récupère le résultat de la requête SQL et retourne le score ou 0 s'il n'y a aucun score
        resultat = self.curseur.fetchone()
        return resultat[0] if resultat else 0

    def fermer(self):
        # Ferme la connexion à la base de données
        self.connexion.close()
