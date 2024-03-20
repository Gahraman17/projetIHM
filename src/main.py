# Importe les classes nécessaires depuis les fichiers correspondants.
from Question import Question
from Categorie import Categorie
from Jeux import Jeux
from Bdd import Bdd
from Controller import Controller
from Ihm import Ihm

if __name__ == "__main__":
    # Initialise une connexion à la base de données avec le chemin spécifié.
    db = Bdd('C:/Users/fredt/OneDrive/Bureau/cours/Licence/projetQuizz/projetIHM/bdd/quiEstIntrus.bd')
    
    # Initialise le contrôleur avec la connexion à la base de données.
    controller = Controller(db)
    
    # Démarre le programme en lançant l'interface utilisateur via le contrôleur.
    controller.start()
