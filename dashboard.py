import tkinter as tk
from tkinter import messagebox
import clients
import export_pdf

def ouvrir_dashboard(role):
    root = tk.Tk()
    root.title("Dashboard - Gestion Clients")
    root.geometry("900x600")

    tk.Label(root, text=f"Bienvenue ({role})", font=("Arial", 16)).pack(pady=10)

    # Boutons
    tk.Button(root, text="Ajouter Client", bg="#4CAF50", fg="white", width=20,
              command=lambda: messagebox.showinfo("Ajouter", "Fonction Ajouter Client")).pack(pady=5)

    tk.Button(root, text="Modifier Client", bg="#FFC107", fg="white", width=20,
              command=lambda: messagebox.showinfo("Modifier", "Fonction Modifier Client")).pack(pady=5)

    if role == "admin":
        tk.Button(root, text="Supprimer Client", bg="#F44336", fg="white", width=20,
                  command=lambda: messagebox.showinfo("Supprimer", "Fonction Supprimer Client")).pack(pady=5)

    tk.Button(root, text="Rechercher Client", bg="#2196F3", fg="white", width=20,
              command=lambda: messagebox.showinfo("Rechercher", "Fonction Rechercher Client")).pack(pady=5)

    tk.Button(root, text="Exporter PDF", bg="#9C27B0", fg="white", width=20,
              command=export_pdf.exporter_pdf).pack(pady=5)

    root.mainloop()
