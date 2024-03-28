# -*- coding: utf-8 -*-
"""
Code source du projet Cherchez l'intrus

@author : fredt,akram,abdou

Contrôleur du jeu Cherchez l'intrus
"""

from Ihm import Ihm

class Controleur:
    def __init__(self, db):
        # Initialisation des attributs de la classe Controleur
        # Instance de la classe Jeux
        self.db = db  # Instance de la base de données
        self.ui = None  # Initialisation de l'interface utilisateur à None

    def demarrer(self):
        # Méthode pour démarrer le jeu
        self.ui = Ihm(Controleur(self.db))  # Instanciation de l'interface utilisateur avec l'instance du jeu
    # Ihm(self.jeu,self) 
    def quitter(self):
        # Méthode pour quitter le jeu
        self.db.fermer()  # Fermeture de la connexion à la base de données
     #recupération du catégorie de jeu
    
    def obtenir_categories(self):
        # Méthode pour obtenir toutes les catégories disponibles depuis la base de données
        return self.db.obtenir_categories() 
        # cette méthode retourne une liste de compréhension contenant les catégories 

    def obtenir_questions(self, id_categorie):
        # Méthode pour obtenir toutes les questions d'une catégorie spécifique depuis la base de données
        return self.db.obtenir_questions_par_categorie(id_categorie)
    
    def verifier_reponse(self, question, index_choisi):
        # Méthode pour vérifier la réponse choisie par le joueur
        if question.is_correct(index_choisi):
            self.ui.afficher_confirmation("Bonne réponse!\n" + question.explication)
            self.score += 1  # Incrémentation du score en cas de bonne réponse
        else:
            self.ui.afficher_erreur("Mauvaise réponse!\n" + question.explication)
        
        # Passage à la question suivante si possible
        self.index_question_actuelle += 1
        if self.index_question_actuelle < len(self.questions_actuelles):
            self.ui.afficher_prochaine_question(self.questions_actuelles[self.index_question_actuelle])
        else:
            self.ui.afficher_fin_jeu()
