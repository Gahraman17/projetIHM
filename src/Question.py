# Définit la classe Question qui représente une question dans le jeu.
class Question:
    def __init__(self, question_id, category_id, text, options, correct_option):
        # Initialise les attributs de la question.
        self.question_id = question_id  # L'identifiant unique de la question.
        self.category_id = category_id  # L'identifiant de la catégorie à laquelle appartient la question.
        self.text = text  # Le texte de la question.
        self.options = options  # Les options possibles pour répondre à la question.
        self.correct_option = correct_option  # L'indice de l'option correcte parmi les options.

    def is_correct(self, selected_option):
        # Vérifie si l'option sélectionnée par le joueur est correcte pour cette question.
        return selected_option == self.correct_option
