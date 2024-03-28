# -*- coding: utf-8 -*-
"""
Code source du projet Cherchez l'intrus

@author : fredt,akram,abdou

Question : classe représentant une question dans le jeu
"""

# Définit la classe Question qui représente une question dans le jeu.
class Question:
    # Initialise une instance de la classe Question avec les attributs spécifiés.
    def __init__(self, question_id, id_categorie, texte, options, option_correcte, explication):
        self.question_id = question_id  # Identifiant unique de la question
        self.id_categorie = id_categorie  # Identifiant de la catégorie à laquelle la question appartient
        self.texte = texte  # Texte de la question
        self.options = options  # Liste des options possibles pour la question
        self.option_correcte = option_correcte  # Index de l'option correcte dans la liste des options
        self.explication = explication  # Explication de la réponse correcte

    # Vérifie si l'index de l'option sélectionnée correspond à l'option correcte.
    def is_correct(self, selected_option_index):
        return selected_option_index == self.option_correcte - 1 # Soustrait 1 pour correspondre à l'index de la liste
