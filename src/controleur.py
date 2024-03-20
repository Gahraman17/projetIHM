# -*- coding: utf-8 -*-
"""
Code source du projet Cherchez l'intrus

@author : fredt

Contrôleur du jeu Cherchez l'intrus
"""

from Jeux import Jeux
from Ihm import Ihm

class Controleur:
    def __init__(self, db):
        # Initialisation des attributs de la classe Controleur
        self.jeu = Jeux(db)  # Instance de la classe Jeux
        self.db = db  # Instance de la base de données
        self.ui = None  # Initialisation de l'interface utilisateur à None

    def demarrer(self):
        # Méthode pour démarrer le jeu
        self.ui = Ihm(self.jeu)  # Instanciation de l'interface utilisateur avec l'instance du jeu

    def quitter(self):
        # Méthode pour quitter le jeu
        self.db.fermer()  # Fermeture de la connexion à la base de données
