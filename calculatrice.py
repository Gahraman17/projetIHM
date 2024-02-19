# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 13:37:05 2024

@author: Etudiant
"""

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
    # Calculer la nouvelle taille de police basée sur la taille de la fenêtre pour les boutons
    new_button_font_size = max(8, min(fenetre.winfo_width() // 25, fenetre.winfo_height() // 25))
    new_button_font = ("Arial", new_button_font_size)
    
    # Calculer la nouvelle taille de police pour l'Entry
    new_entry_font_size = max(10, min(fenetre.winfo_width() // 20, fenetre.winfo_height() // 20))
    new_entry_font = ("Arial", new_entry_font_size)
    
    # Mettre à jour la taille de la police pour les boutons
    for button in buttons:
        button.config(font=new_button_font)
    
    # Mettre à jour la taille de la police pour l'Entry
    resultat.config(font=new_entry_font)

fenetre = Tk()
fenetre.title("Calculatrice")

buttons = []

fenetre.columnconfigure(0, weight=1)
fenetre.rowconfigure(0, weight=1)

ecran_resultat = Frame(fenetre, borderwidth=2, relief=GROOVE)
ecran_resultat.pack(side=TOP, fill="both", expand=True, padx=5, pady=5)

resultat = Entry(ecran_resultat)
resultat.pack(fill="both", expand=True, padx=5, pady=5)

clavier = Frame(fenetre, borderwidth=2, relief=GROOVE)
clavier.pack(fill="both", expand=True)

clavier.columnconfigure(tuple(range(4)), weight=1)
clavier.rowconfigure(tuple(range(4)), weight=1)

i = 1
for ligne in range(3):
    for colonne in range(3):
        btn = Button(clavier, text=str(i), borderwidth=1, command=lambda i=i: calculer(i))
        btn.grid(row=ligne, column=colonne, padx=5, pady=5, sticky='nsew')
        buttons.append(btn)
        i += 1

Button(clavier, text='0', command=lambda: calculer(0)).grid(row=3, column=0, padx=5, pady=5, sticky='nsew')
Button(clavier, text='AC', command=lambda: resultat.delete(0, END)).grid(row=3, column=1, padx=5, pady=5, sticky='nsew')
Button(clavier, text='=', command=evaluer).grid(row=3, column=2, padx=5, pady=5, sticky='nsew')

operateurs = ['/', '*', '-', '+']
i = 0
for operateur in operateurs:
    btn_operateur = Button(clavier, text=operateur, command=lambda operateur=operateur: calculer(operateur))
    btn_operateur.grid(row=i, column=3, padx=5, pady=5, sticky='nsew')
    buttons.append(btn_operateur)
    i += 1

# Liaison de l'événement de redimensionnement de la fenêtre pour ajuster la taille de la police
fenetre.bind('<Configure>', adjust_font_size)

fenetre.mainloop()
