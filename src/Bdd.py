import sqlite3
from Question import Question
from Categorie import Categorie

class Bdd:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def get_categories(self):
        self.cursor.execute("SELECT id, name FROM categories")
        return [Categorie(category[0], category[1]) for category in self.cursor.fetchall()]

    def get_questions_by_category(self, category_id):
        self.cursor.execute("SELECT id, text, option1, option2, option3, correct_option FROM questions WHERE category_id=?", (category_id,))
        return [Question(question[0], category_id, question[1], question[2:5], question[5]) for question in self.cursor.fetchall()]

    def insert_score(self, player_name, category_id, score):
        self.cursor.execute("INSERT INTO scores (player_name, category_id, score) VALUES (?, ?, ?)", (player_name, category_id, score))
        self.connection.commit()

    def get_best_score(self, player_name, category_id):
        self.cursor.execute("SELECT MAX(score) FROM scores WHERE player_name=? AND category_id=?", (player_name, category_id))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return 0

    def close(self):
        self.connection.close()
