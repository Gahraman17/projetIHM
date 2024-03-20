from Jeux import Jeux  # Importe la classe Jeux depuis le module Jeux
from Ihm import Ihm  # Importe la classe Ihm depuis le module Ihm

class Controller:
    def __init__(self, db):
        # Initialise le contrôleur avec une instance de la classe Jeux et une connexion de base de données
        self.game = Jeux(db)  # Crée une instance de la classe Jeux en lui passant la connexion de base de données
        self.db = db  # Stocke la connexion de base de données pour une utilisation ultérieure

    def start(self):
        # Lance l'interface utilisateur en passant l'instance de la classe Jeux
        self.ui = Ihm(self.game)  # Crée une instance de la classe Ihm en lui passant l'instance de la classe Jeux

    def quit(self):
        # Ferme la connexion de la base de données lorsque l'application est quittée
        self.db.close()  # Appelle la méthode close() de l'objet de connexion de base de données pour fermer la connexion
