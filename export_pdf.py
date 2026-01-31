from database import get_connection
from fpdf import FPDF
from tkinter import messagebox

def exporter_pdf():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM clients")
    clients_data = cursor.fetchall()
    db.close()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)
    for client in clients_data:
        pdf.cell(0, 8, f"{client}", ln=True)
    pdf.output("clients.pdf")
    messagebox.showinfo("Export", "Export PDF terminé")
