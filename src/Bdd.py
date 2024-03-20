import sqlite3  # Importation du module sqlite3
from Question import Question  # Importation de la classe Question depuis le module Question
from Categorie import Categorie  # Importation de la classe Categorie depuis le module Categorie

class Bdd:
    def __init__(self, db_name):
        # Initialisation de la classe Bdd avec le nom de la base de données
        self.connection = sqlite3.connect(db_name)  # Connexion à la base de données spécifiée
        self.cursor = self.connection.cursor()  # Création d'un objet curseur pour exécuter des requêtes SQL

    def get_categories(self):
        # Méthode pour récupérer toutes les catégories depuis la base de données
        self.cursor.execute("SELECT id, name FROM categories")  # Exécution de la requête SQL pour récupérer les catégories
        # Création d'une liste de catégories à partir des résultats de la requête
        return [Categorie(category[0], category[1]) for category in self.cursor.fetchall()]

    def get_questions_by_category(self, category_id):
        # Méthode pour récupérer toutes les questions associées à une catégorie donnée
        # La méthode prend en paramètre l'identifiant de la catégorie
        self.cursor.execute("SELECT id, text, option1, option2, option3, correct_option FROM questions WHERE category_id=?", (category_id,))
        # Exécution de la requête SQL pour récupérer les questions de la catégorie spécifiée
        # Création d'une liste d'objets Question à partir des résultats de la requête
        return [Question(question[0], category_id, question[1], question[2:5], question[5]) for question in self.cursor.fetchall()]

    def insert_score(self, player_name, category_id, score):
        # Méthode pour insérer un score dans la base de données
        # La méthode prend en paramètre le nom du joueur, l'identifiant de la catégorie et le score
        self.cursor.execute("INSERT INTO scores (player_name, category_id, score) VALUES (?, ?, ?)", (player_name, category_id, score))
        # Exécution de la requête SQL pour insérer le score dans la table scores
        self.connection.commit()  # Validation de la transaction

    def get_best_score(self, player_name, category_id):
        # Méthode pour récupérer le meilleur score d'un joueur dans une catégorie donnée
        # La méthode prend en paramètre le nom du joueur et l'identifiant de la catégorie
        self.cursor.execute("SELECT MAX(score) FROM scores WHERE player_name=? AND category_id=?", (player_name, category_id))
        # Exécution de la requête SQL pour récupérer le meilleur score du joueur dans la catégorie spécifiée
        result = self.cursor.fetchone()  # Récupération du résultat de la requête
        if result:
            return result[0]  # Retourne le meilleur score s'il existe
        else:
            return 0  # Retourne 0 si aucun score n'est trouvé

    def close(self):
        # Méthode pour fermer la connexion à la base de données
        self.connection.close()  # Fermeture de la connexion
