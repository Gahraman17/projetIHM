# -*- coding: utf-8 -*-
"""
Code source du projet Cherchez l'intrus

@author : fredt

main : point d'entrée du programme
"""

# Importe les classes nécessaires depuis les fichiers correspondants.
from controleur import Controleur
from Bdd import BaseDeDonnees

if __name__ == "__main__":
    
    #BUG : chemin relatif ne fonctionne pas
    # Initialise une connexion à la base de données avec le chemin complet
    db = BaseDeDonnees("C:\\Users\\fredt\\OneDrive\\Bureau\\cours\\Licence\\projetQuizz\\projetIHM\\src\\bddIntrus.db")
    
    # Initialise le contrôleur avec la connexion à la base de données.
    controleur = Controleur(db)
    
    # Démarre le programme en lançant l'interface utilisateur via le contrôleur.
    controleur.demarrer()
