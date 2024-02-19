from tkinter import *

def calculer(valeur):
    current_text = resultat.get()
    resultat.delete(0, END)
    resultat.insert(0, current_text + str(valeur))

def evaluer():
    try:
        expression = resultat.get()
        resultat.delete(0, END)
        resultat.insert(0, eval(expression))
    except Exception as e:
        resultat.insert(0, "Erreur")

def adjust_font_size(event):
    # Calculer la nouvelle taille de police basée sur la taille de la fenêtre pour les boutons numériques
    new_button_font_size = max(8, min(fenetre.winfo_width() // 25, fenetre.winfo_height() // 25))
    new_button_font = ("Arial", new_button_font_size)
    
    # Calculer la nouvelle taille de police pour les boutons spéciaux (0, AC, =)
    new_special_button_font_size = max(8, min(fenetre.winfo_width() // 40, fenetre.winfo_height() // 40))
    new_special_button_font = ("Arial", new_special_button_font_size)
    
    # Calculer la nouvelle taille de police pour l'Entry
    new_entry_font_size = max(10, min(fenetre.winfo_width() // 20, fenetre.winfo_height() // 20))
    new_entry_font = ("Arial", new_entry_font_size)
    
    # Mettre à jour la taille de la police pour les boutons numériques
    for button in buttons_num:
        button.config(font=new_button_font)
    
    # Mettre à jour la taille de la police pour les boutons spéciaux
    for button in buttons_special:
        button.config(font=new_special_button_font)
    
    # Mettre à jour la taille de la police pour l'Entry
    resultat.config(font=new_entry_font)

fenetre = Tk()
fenetre.title("Calculatrice")

buttons_num = []  # Liste pour les boutons numériques
buttons_special = []  # Liste pour les boutons spéciaux (0, AC, =)

fenetre.columnconfigure(0, weight=1)
fenetre.rowconfigure(0, weight=1)

ecran_resultat = Frame(fenetre, borderwidth=2, relief=GROOVE)
ecran_resultat.pack(side=TOP, fill="both", expand=True, padx=5, pady=5)

resultat = Entry(ecran_resultat)
resultat.pack(fill="both", expand=True, padx=5, pady=5)

clavier = Frame(fenetre, borderwidth=2, relief=GROOVE)
clavier.pack(fill="both", expand=True)

clavier.columnconfigure(tuple(range(4)), weight=1)
clavier.rowconfigure(tuple(range(5)), weight=1)

i = 1
for ligne in range(3):
    for colonne in range(3):
        btn = Button(clavier, text=str(i), borderwidth=1, command=lambda i=i: calculer(i))
        btn.grid(row=ligne, column=colonne, padx=5, pady=5, sticky='nsew')
        buttons_num.append(btn)
        i += 1

Button(clavier, text='0', command=lambda: calculer(0)).grid(row=3, column=0, padx=5, pady=5, sticky='nsew')
Button(clavier, text='AC', command=lambda: resultat.delete(0, END)).grid(row=3, column=1, padx=5, pady=5, sticky='nsew')
Button(clavier, text='=', command=evaluer).grid(row=3, column=2, padx=5, pady=5, sticky='nsew')

operateurs = ['/', '*', '-', '+']
i = 0
for operateur in operateurs:
    btn_operateur = Button(clavier, text=operateur, command=lambda operateur=operateur: calculer(operateur))
    btn_operateur.grid(row=i, column=3, padx=5, pady=5, sticky='nsew')
    buttons_num.append(btn_operateur)
    i += 1

# Ajout des boutons spéciaux à la liste buttons_special
buttons_special.extend([button for button in clavier.winfo_children() if button.cget("text") in ['0', 'AC', '=']])

fenetre.bind('<Configure>', adjust_font_size)

fenetre.mainloop()
