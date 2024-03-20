class Question:
    def __init__(self, question_id, category_id, text, options, correct_option):
        self.question_id = question_id
        self.category_id = category_id
        self.text = text
        self.options = options
        self.correct_option = correct_option

    def is_correct(self, selected_option):
        return selected_option == self.correct_option
