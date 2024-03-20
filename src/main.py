# -*- coding: utf-8 -*-
"""
Code source du projet Cherchez l'intrus

@author : fredt

main : point d'entrée du programme
"""

# Importe les classes nécessaires depuis les fichiers correspondants.
from controleur import Controleur
from bdd import BaseDeDonnees

if __name__ == "__main__":
    # Initialise une connexion à la base de données avec le chemin spécifié.
    db = BaseDeDonnees("bddIntrus.db")
    
    # Initialise le contrôleur avec la connexion à la base de données.
    controleur = Controleur(db)
    
    # Démarre le programme en lançant l'interface utilisateur via le contrôleur.
    controleur.demarrer()
