import tkinter as tk
from tkinter import messagebox
import mysql.connector
from fpdf import FPDF

# -------------------
# CONFIGURATION MYSQL
# -------------------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gestion_clients"
)

cursor = db.cursor()

# -------------------
# FONCTIONS DE BASE
# -------------------
def ajouter_client(nom, prenom, telephone, email, adresse, numero_compte, solde, date_inscription):
    try:
        sql = "INSERT INTO clients (nom, prenom, telephone, email, adresse, numero_compte, solde, date_inscription) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (nom, prenom, telephone, email, adresse, numero_compte, solde, date_inscription)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Succès", "Client ajouté avec succès")
    except Exception as e:
        messagebox.showerror("Erreur", str(e))

def exporter_pdf():
    cursor.execute("SELECT * FROM clients")
    clients = cursor.fetchall()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)
    for c in clients:
        pdf.cell(0, 8, f"{c}", ln=True)
    pdf.output("clients.pdf")
    messagebox.showinfo("Export", "Export PDF terminé")

# -------------------
# INTERFACE GRAPHIQUE
# -------------------
root = tk.Tk()
root.title("Gestion des Clients - Amadou Dème")
root.geometry("900x600")
root.configure(bg="#f5f5f5")

# Titre
titre = tk.Label(root, text="Système de Gestion des Clients", font=("Arial", 20, "bold"), bg="#f5f5f5")
titre.pack(pady=20)

# Exemple simple : Bouton Ajouter Client
btn_ajouter = tk.Button(root, text="Ajouter Client (Exemple)", width=25, bg="#4CAF50", fg="white",
                        command=lambda: ajouter_client(
                            "DÈME", "Amadou", "785241466", "amadoudeme123@gmail.com", 
                            "Dakar", "24120403", 1000000000, "2020-12-24"))
btn_ajouter.pack(pady=10)

# Bouton Export PDF
btn_export = tk.Button(root, text="Exporter en PDF", width=25, bg="#2196F3", fg="white",
                       command=exporter_pdf)
btn_export.pack(pady=10)

root.mainloop()
