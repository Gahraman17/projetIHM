# -*- coding: utf-8 -*-
"""
Code source du projet Cherchez l'intrus

@author : fredt

Classe Jeux
"""
# TODO : réfléchir à la pertinence de cette classe


class Jeux:
    def __init__(self, db):
        # Initialisation de la classe Jeux avec une instance de la base de données
        self.db = db

    def obtenir_categories(self):
        # Méthode pour obtenir toutes les catégories disponibles depuis la base de données
        return self.db.obtenir_categories()

    def obtenir_questions(self, id_categorie):
        # Méthode pour obtenir toutes les questions d'une catégorie spécifique depuis la base de données
        return self.db.obtenir_questions_par_categorie(id_categorie)
