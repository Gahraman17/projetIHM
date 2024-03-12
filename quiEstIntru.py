# jeux "Chasser l'intrus"

import random

# Liste des questions
questions = [
    {
        'question': "Capital d'Europe",
        'options': ['Paris', 'Berlin', 'Tokyo'],
        'correct_answer': 'Tokyo'
    },
    {
        'question': "Language orienté web",
        'options': ['Haskell', 'PHP', 'JavaScript'],
        'correct_answer': 'Haskell'
    },
    {
        'question': "Produit Apple?",
        'options': ['S9', 'Ipad', 'Iphone'],
        'correct_answer': 'S9'
    },
    {
        'question': "Outil de localisation",
        'options': ["Google maps", "CleverMaps", "Photoshop"],
        'correct_answer': 'Photoshop'
    },
    {
        'question': "Joueur de foot",
        'options': ['Ronaldo', 'Lebron James', 'Messi'],
        'correct_answer': 'Lebron James'
    },
    {
        'question': "Palindrome",
        'options': ['Kayak', 'Ressasser', 'Pierre'],
        'correct_answer': 'Pierre'
    },
    {
        'question': "Animeaux",
        'options': ['chien', 'Chat', 'Arbre'],
        'correct_answer': 'Arbre'
    },
    {
        'question': "Composant d'un ordinateur",
        'options': ['Lunette', 'Processeur', 'Mémoire RAM'],
        'correct_answer': 'Lunette'
    },
    {
        'question': "Acteur",
        'options': ['Di Caprio', 'Brad Pitt' 'MBappé'],
        'correct_answer': 'MBappé'
    },
    {
        'question': "Nombre premier",
        'options': ['7', '11', '22'],
        'correct_answer': '22'
    },
]


# Fonction pour poser une question
def poser_question(question):
    print(question['question'])
    for i, option in enumerate(question['options'], 1):
        print(f"{i}. {option}")
    reponse = input("Votre réponse (entrez le numéro de la réponse) : ")
    return question['options'][int(reponse) - 1]

# Fonction pour jouer le quiz
def jouer_quiz():
    score = 0
    random.shuffle(questions)

    for q in questions:
        reponse_utilisateur = poser_question(q)
        if reponse_utilisateur == q['correct_answer']:
            print("Bonne réponse!\n")
            score += 1
        else:
            print(f"Mauvaise réponse. La réponse correcte était : {q['correct_answer']}\n")

    print(f"Vous avez obtenu {score} sur {len(questions)} questions.")
    
# Appel de la fonction pour jouer le quiz
if __name__ == "__main__":
    jouer_quiz()
