class Jeux:
    def __init__(self, db):
        self.db = db

    def get_categories(self):
        return self.db.get_categories()

    def get_questions(self, category_id):
        return self.db.get_questions_by_category(category_id)
