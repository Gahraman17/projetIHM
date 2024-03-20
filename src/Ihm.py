import tkinter as tk  # Importe le module tkinter sous l'alias 'tk'
from tkinter import messagebox  # Importe la classe 'messagebox' du module tkinter
from Jeux import Jeux  # Importe la classe 'Jeux' depuis le module 'Jeux'

class Ihm:
    def __init__(self, game):
        self.game = game  # Initialise l'instance de la classe 'Jeux' passée en argument
        
        # Crée une nouvelle fenêtre Tkinter
        self.window = tk.Tk()
        self.window.title("Chassez l'Intrus")  # Définit le titre de la fenêtre
        
        # Obtenir les dimensions de l'écran
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        
        # Calculer les dimensions de la fenêtre
        window_width = int(screen_width * 0.5)
        window_height = int(screen_height * 0.5)
        
        # Positionner la fenêtre au centre de l'écran
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        self.window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")  # Définit la géométrie de la fenêtre
        
        # Crée un frame principal à l'intérieur de la fenêtre
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)  # Place le frame dans la fenêtre
        
        # Crée un label pour afficher le texte "Choisissez une catégorie:"
        self.category_label = tk.Label(self.main_frame, text="Choisissez une catégorie:")
        self.category_label.pack()  # Place le label dans le frame principal
        
        # Crée une variable tkinter pour stocker la catégorie sélectionnée
        self.category_var = tk.StringVar()
        self.categories = self.game.get_categories()  # Récupère les catégories à partir de la logique de jeu
        # Définit la première catégorie comme valeur par défaut si des catégories sont disponibles
        self.category_var.set(self.categories[0].name if self.categories else "")
        # Crée un menu déroulant des catégories à choisir
        self.category_menu = tk.OptionMenu(self.main_frame, self.category_var, *[category.name for category in self.categories])
        self.category_menu.pack()  # Place le menu déroulant dans le frame principal
        
        # Crée un bouton "Commencer" qui appelle la méthode start_game lorsqu'il est cliqué
        self.start_button = tk.Button(self.main_frame, text="Commencer", command=self.start_game)
        self.start_button.pack()  # Place le bouton dans le frame principal
        
        self.window.mainloop()  # Lance la boucle principale de la fenêtre Tkinter

    def start_game(self):
        # Récupère le nom de la catégorie sélectionnée
        selected_category_name = self.category_var.get()
        # Recherche la catégorie correspondante dans la liste des catégories
        selected_category = next((category for category in self.categories if category.name == selected_category_name), None)
        
        if selected_category:
            # Si une catégorie valide est sélectionnée, récupère les questions associées à cette catégorie
            questions = self.game.get_questions(selected_category.category_id)
            if questions:
                # TODO: Mettre en place la logique pour commencer le jeu avec les questions sélectionnées
                pass
            else:
                messagebox.showerror("Erreur", "Aucune question disponible pour cette catégorie.")
        else:
            messagebox.showerror("Erreur", "Catégorie sélectionnée non valide.")
