import tkinter as tk
from tkinter import messagebox
from Jeux import Jeux

class Ihm:
    def __init__(self, game):
        self.game = game
        self.window = tk.Tk()
        self.window.title("Chassez l'Intrus")
        
        # Obtenir les dimensions de l'écran
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        
        # Calculer les dimensions de la fenêtre
        window_width = int(screen_width * 0.5)
        window_height = int(screen_height * 0.5)
        
        # Positionner la fenêtre au centre de l'écran
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        
        self.window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        self.category_label = tk.Label(self.main_frame, text="Choisissez une catégorie:")
        self.category_label.pack()

        self.category_var = tk.StringVar()
        self.categories = self.game.get_categories()
        self.category_var.set(self.categories[0].name if self.categories else "")
        self.category_menu = tk.OptionMenu(self.main_frame, self.category_var, *[category.name for category in self.categories])
        self.category_menu.pack()

        self.start_button = tk.Button(self.main_frame, text="Commencer", command=self.start_game)
        self.start_button.pack()

        self.window.mainloop()

    def start_game(self):
        selected_category_name = self.category_var.get()
        selected_category = next((category for category in self.categories if category.name == selected_category_name), None)
        
        if selected_category:
            questions = self.game.get_questions(selected_category.category_id)
            if questions:
                # TODO: Mettre en place la logique pour commencer le jeu avec les questions sélectionnées
                pass
            else:
                messagebox.showerror("Erreur", "Aucune question disponible pour cette catégorie.")
        else:
            messagebox.showerror("Erreur", "Catégorie sélectionnée non valide.")
