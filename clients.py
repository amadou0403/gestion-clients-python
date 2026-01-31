from database import get_connection

def ajouter_client(nom, prenom, telephone, email, adresse, numero_compte, solde, date_inscription):
    db = get_connection()
    cursor = db.cursor()
    sql = "INSERT INTO clients (nom, prenom, telephone, email, adresse, numero_compte, solde, date_inscription) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (nom, prenom, telephone, email, adresse, numero_compte, solde, date_inscription)
    cursor.execute(sql, val)
    db.commit()
    db.close()

def modifier_client(client_id, nom, prenom, telephone, email, adresse, numero_compte, solde):
    db = get_connection()
    cursor = db.cursor()
    sql = """UPDATE clients SET nom=%s, prenom=%s, telephone=%s, email=%s, adresse=%s, numero_compte=%s, solde=%s
             WHERE id=%s"""
    val = (nom, prenom, telephone, email, adresse, numero_compte, solde, client_id)
    cursor.execute(sql, val)
    db.commit()
    db.close()

def supprimer_client(client_id):
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("DELETE FROM clients WHERE id=%s", (client_id,))
    db.commit()
    db.close()

def rechercher_client(mot_cle):
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM clients WHERE nom LIKE %s OR prenom LIKE %s", (f"%{mot_cle}%", f"%{mot_cle}%"))
    result = cursor.fetchall()
    db.close()
    return result
