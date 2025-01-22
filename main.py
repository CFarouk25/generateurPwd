#!/usr/bin/env python
# -*- coding: utf-8 -*-



import tkinter as tk
from tkinter import messagebox
import random
import string


# Fonction pour générer un mot de passe aléatoire
def generate_password():
    length = int(password_length_entry.get())
    include_upper = upper_case_var.get()
    include_lower = lower_case_var.get()
    include_digits = digits_var.get()
    include_special = special_char_var.get()

    char_set = string.ascii_lowercase  # Toujours inclure les lettres minuscules

    if include_upper:
        char_set += string.ascii_uppercase  # Ajouter les lettres majuscules
    if include_digits:
        char_set += string.digits  # Ajouter les chiffres
    if include_special:
        char_set += string.punctuation  # Ajouter les caractères spéciaux

    # Générer le mot de passe
    if length > 0:
        password = ''.join(random.choice(char_set) for _ in range(length))
        password_output.delete(0, tk.END)  # Effacer l'ancien mot de passe
        password_output.insert(0, password)  # Afficher le nouveau mot de passe
    else:
        messagebox.showerror("Erreur", "La longueur du mot de passe doit être un nombre positif.")


# Créer la fenêtre principale
root = tk.Tk()
root.title("Générateur de Mot de Passe")

# Frame pour l'interface utilisateur
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Longueur du mot de passe
length_label = tk.Label(frame, text="Longueur du mot de passe:")
length_label.grid(row=0, column=0, padx=5, pady=5)

password_length_entry = tk.Entry(frame)
password_length_entry.grid(row=0, column=1, padx=5, pady=5)
password_length_entry.insert(0, "12")  # Valeur par défaut

# Options pour inclure les majuscules, chiffres et caractères spéciaux
upper_case_var = tk.BooleanVar(value=True)
lower_case_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_char_var = tk.BooleanVar(value=True)

upper_case_check = tk.Checkbutton(frame, text="Inclure Majuscules", variable=upper_case_var)
upper_case_check.grid(row=1, column=0, padx=5, pady=5, sticky="w")

lower_case_check = tk.Checkbutton(frame, text="Inclure Minuscules", variable=lower_case_var)
lower_case_check.grid(row=2, column=0, padx=5, pady=5, sticky="w")

digits_check = tk.Checkbutton(frame, text="Inclure Chiffres", variable=digits_var)
digits_check.grid(row=3, column=0, padx=5, pady=5, sticky="w")

special_char_check = tk.Checkbutton(frame, text="Inclure Caractères spéciaux", variable=special_char_var)
special_char_check.grid(row=4, column=0, padx=5, pady=5, sticky="w")

# Bouton pour générer le mot de passe
generate_button = tk.Button(frame, text="Générer", command=generate_password)
generate_button.grid(row=5, column=0, columnspan=2, pady=10)

# Affichage du mot de passe généré
password_label = tk.Label(frame, text="Mot de passe généré:")
password_label.grid(row=6, column=0, padx=5, pady=5)

password_output = tk.Entry(frame, width=30)
password_output.grid(row=6, column=1, padx=5, pady=5)

# Lancer l'application
root.mainloop()
