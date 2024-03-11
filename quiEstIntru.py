# jeux "Chasser l'intrus"

import random

# Liste des questions
questions = [
    {
        'question': "Quelle est la capitale de la France?",
        'options': ['Paris', 'Berlin', 'Londres'],
        'correct_answer': 'Paris'
    },
    {
        'question': "Quel langage de programmation est souvent utilisé pour le développement web?",
        'options': ['Python', 'Java', 'JavaScript'],
        'correct_answer': 'JavaScript'
    },
    {
        'question': "Quel est le système d'exploitation développé par Apple?",
        'options': ['Windows', 'iOS', 'Android'],
        'correct_answer': 'iOS'
    },
    {
        'question': "Quelle est la principale fonction de Git?",
        'options': ["Navigation GPS", "Contrôle de version", "Traitement d'image"],
        'correct_answer': 'Contrôle de version'
    },
    {
        'question': "En informatique, que signifie l'acronyme 'HTML'?",
        'options': ['HyperText Markup Language', 'High Tech Modern Language', 'Home Tool Markup Language'],
        'correct_answer': 'HyperText Markup Language'
    },
    {
        'question': "Quel est le langage de programmation utilisé pour créer des applications Android?",
        'options': ['Swift', 'Java', 'C#'],
        'correct_answer': 'Java'
    },
    {
        'question': "Quelle est la fonction de la boucle 'for' en programmation?",
        'options': ['Itération', 'Condition', 'Déclaration'],
        'correct_answer': 'Itération'
    },
    {
        'question': "Quel est le principal composant d'un ordinateur?",
        'options': ['Carte graphique', 'Processeur', 'Mémoire RAM'],
        'correct_answer': 'Processeur'
    },
    {
        'question': "Quelle est la différence entre RAM et ROM?",
        'options': ['RAM est volatile, ROM est non volatile', 'RAM est non volatile, ROM est volatile', 'Elles sont identiques'],
        'correct_answer': 'RAM est volatile, ROM est non volatile'
    },
    {
        'question': "Quel est le fondateur de Microsoft?",
        'options': ['Steve Jobs', 'Bill Gates', 'Mark Zuckerberg'],
        'correct_answer': 'Bill Gates'
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
