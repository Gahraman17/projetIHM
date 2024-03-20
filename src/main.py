from Question import Question
from Categorie import Categorie
from Jeux import Jeux
from Bdd import Bdd
from Controller import Controller
from Ihm import Ihm

if __name__ == "__main__":
    db = Bdd('C:/Users/fredt/OneDrive/Bureau/cours/Licence/projetQuizz/projetIHM/bdd/quiEstIntrus.bd')
    controller = Controller(db)
    controller.start()
