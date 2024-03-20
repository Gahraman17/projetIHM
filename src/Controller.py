from Jeux import Jeux
from Ihm import Ihm

class Controller:
    def __init__(self, db):
        self.game = Jeux(db)
        self.db = db

    def start(self):
        self.ui = Ihm(self.game)

    def quit(self):
        self.db.close()
