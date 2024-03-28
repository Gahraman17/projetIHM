# -*- coding: utf-8 -*-
"""
Code source du projet Cherchez l'intrus

@author : fredt,akram,abdou

Interface utilisateur du jeu Cherchez l'intrus
"""

import tkinter as tk
from tkinter import messagebox


class Ihm:
    def __init__(self,controleur):#controleur
        # Initialisation de l'interface utilisateur avec le jeu passé en paramètre
        #self.jeu = jeu
        self.fenetre = tk.Tk()  # Création d'une fenêtre Tkinter
        self.fenetre.title("Chassez l'Intrus")  # Définition du titre de la fenêtre
        self.controleur = controleur


        # Récupération des dimensions de l'écran
        largeur_ecran = self.fenetre.winfo_screenwidth()
        hauteur_ecran = self.fenetre.winfo_screenheight()

        # Calcul des dimensions de la fenêtre
        largeur_fenetre = int(largeur_ecran * 0.5)
        hauteur_fenetre = int(hauteur_ecran * 0.5)

        # Calcul de la position de la fenêtre sur l'écran
        position_x = (largeur_ecran - largeur_fenetre) // 2
        position_y = (hauteur_ecran - hauteur_fenetre) // 2
        
        self.score = 0  # Initialisation du score du joueur

        # Configuration de la géométrie de la fenêtre
        self.fenetre.geometry(f"{largeur_fenetre}x{hauteur_fenetre}+{position_x}+{position_y}")

        # Création d'un cadre principal pour placer les éléments de l'interface
        self.cadre_principal = tk.Frame(self.fenetre)
        self.cadre_principal.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        # Label pour afficher le message de sélection de catégorie
        self.label_categorie = tk.Label(self.cadre_principal, text="Choisissez une catégorie:")
        self.label_categorie.pack()

        # Variable pour stocker la catégorie sélectionnée
        self.var_categorie = tk.StringVar()    #permet aussi de mettre à jour dynamiquement le contenu de la variable
        # Récupération des catégories disponibles depuis le jeu et initialisation de la variable
        self.categories = self.controleur.obtenir_categories()
        print("Categories:", self.categories)
        self.var_categorie.set(self.categories[0].nom if self.categories else "")

        # Création du menu déroulant des catégories
        self.menu_categorie = tk.OptionMenu(self.cadre_principal, self.var_categorie, *[cat.nom for cat in self.categories])
        self.menu_categorie.pack()

        # Bouton pour démarrer le jeu
        self.bouton_demarrer = tk.Button(self.cadre_principal, text="Commencer", command=self.demarrer_jeu)
        self.bouton_demarrer.pack()
        
        self.questions_actuelles = []  # Liste des questions actuelles
        self.index_question_actuelle = 0  # Indice de la question actuelle dans la liste

        self.fenetre.mainloop()  # Lancement de la boucle principale de l'interface

    def demarrer_jeu(self):
        # Méthode pour démarrer le jeu
        nom_categorie_selectionnee = self.var_categorie.get()  # Récupération du nom de la catégorie sélectionnée
        categorie_selectionnee = next((cat for cat in self.categories if cat.nom == nom_categorie_selectionnee), None)
        
        if categorie_selectionnee:
            # Récupération des questions pour la catégorie sélectionnée
            self.questions_actuelles = self.controleur.obtenir_questions(categorie_selectionnee.id)
            self.index_question_actuelle = 0  # Commencer par la première question
            if self.questions_actuelles:
                # Affichage de la première question
                self.afficher_question(self.questions_actuelles[self.index_question_actuelle])
            else:
                # Affichage d'un message d'erreur si aucune question n'est trouvée pour la catégorie sélectionnée
                print("Aucune question trouvée pour l'ID de catégorie:", categorie_selectionnee.id)
                messagebox.showerror("Erreur", "Aucune question disponible pour cette catégorie.")
        else:
            # Affichage d'un message d'erreur si la catégorie sélectionnée n'est pas valide
            messagebox.showerror("Erreur", "Catégorie sélectionnée non valide.")
            
    def afficher_question(self, question):
        # Méthode pour afficher une question
        # Nettoyage du cadre principal en détruisant tous les widgets enfants
        for widget in self.cadre_principal.winfo_children():
            widget.destroy()

        # Affichage de la question
        label_question = tk.Label(self.cadre_principal, text=question.texte)
        label_question.pack()

        # Affichage des options de réponse sous forme de boutons
        for index, option in enumerate(question.options):
            bouton_option = tk.Button(self.cadre_principal, text=option, command=lambda idx=index: self.verifier_reponse(question, idx))
            bouton_option.pack()

    def verifier_reponse(self, question, index_choisi):
        # Méthode pour vérifier la réponse choisie par le joueur
        if question.is_correct(index_choisi):
            # Affichage d'un message de confirmation en cas de bonne réponse
            messagebox.showinfo("Bravo", "Bonne réponse!\n" + question.explication)
            self.score += 1  # Incrémentation du score en cas de bonne réponse
        else:
            # Affichage d'un message d'erreur en cas de mauvaise réponse
            messagebox.showerror("Désolé", "Mauvaise réponse!\n" + question.explication)
        
        # Passage à la question suivante si possible
        self.index_question_actuelle += 1
        if self.index_question_actuelle < len(self.questions_actuelles):
            # Affichage de la question suivante
            self.afficher_question(self.questions_actuelles[self.index_question_actuelle])
        else:
            # Affichage de l'écran de fin de jeu si toutes les questions ont été répondues
            self.afficher_fin_jeu()

    def afficher_fin_jeu(self):
        # Méthode pour afficher l'écran de fin de jeu
        # Nettoyage du cadre principal en détruisant tous les widgets enfants
        for widget in self.cadre_principal.winfo_children():
            widget.destroy()

        # Affichage d'un message de fin de jeu
        messagebox.showinfo("Fin", "Vous avez terminé le quiz!")
        # Affichage du score obtenu
        messagebox.showinfo("Score", f"Votre score est de {self.score} / 10.")
        # Bouton pour recommencer le jeu
        bouton_recommencer = tk.Button(self.cadre_principal, text="Recommencer", command=self.recommencer_jeu)
        bouton_recommencer.pack()

        # Bouton pour quitter le jeu
        bouton_quitter = tk.Button(self.cadre_principal, text="Quitter", command=self.quitter_jeu)
        bouton_quitter.pack()

   
