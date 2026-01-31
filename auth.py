import tkinter as tk
from tkinter import messagebox
from database import get_connection

def verifier_login(username, password):
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT role FROM utilisateurs WHERE username=%s AND password=%s", (username, password))
    result = cursor.fetchone()
    db.close()
    if result:
        return result[0]  # admin ou user
    else:
        return None

def page_login():
    root = tk.Tk()
    root.title("Login - Gestion Clients")
    root.geometry("400x250")

    tk.Label(root, text="Nom d'utilisateur").pack(pady=5)
    username_entry = tk.Entry(root)
    username_entry.pack(pady=5)

    tk.Label(root, text="Mot de passe").pack(pady=5)
    password_entry = tk.Entry(root, show="*")
    password_entry.pack(pady=5)

    def se_connecter():
        role = verifier_login(username_entry.get(), password_entry.get())
        if role:
            messagebox.showinfo("Succès", f"Connexion réussie ({role})")
            root.destroy()  # ferme la fenêtre login
            import dashboard
            dashboard.ouvrir_dashboard(role)
        else:
            messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect")

    tk.Button(root, text="Se connecter", command=se_connecter).pack(pady=10)
    root.mainloop()
