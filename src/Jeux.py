class Jeux:
    def __init__(self, db):
        # Initialise la classe Jeux avec une connexion à la base de données.
        self.db = db

    def get_categories(self):
        # Récupère les catégories à partir de la base de données.
        return self.db.get_categories()

    def get_questions(self, category_id):
        # Récupère les questions associées à une catégorie spécifiée à partir de la base de données.
        return self.db.get_questions_by_category(category_id)
