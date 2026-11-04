"""Phase 1: Erprobt die vorgesehenen Elemente der Tkinter-Oberfläche."""

import tkinter as tk
from tkinter import ttk


fenster = tk.Tk()
fenster.title("Oberflächentest")
fenster.geometry("650x300")

titel = tk.Label(
    fenster,
    text="Mein Studien-Dashboard",
    font=("Arial", 18, "bold")
)
titel.pack(pady=15)

fortschritt = ttk.Progressbar(
    fenster,
    maximum=100,
    value=5 / 180 * 100
)
fortschritt.pack(fill="x", padx=20, pady=10)

modul_tabelle = ttk.Treeview(
    fenster,
    columns=("modul", "ects", "status", "note"),
    show="headings",
    height=4
)

modul_tabelle.heading("modul", text="Modul")
modul_tabelle.heading("ects", text="ECTS")
modul_tabelle.heading("status", text="Status")
modul_tabelle.heading("note", text="Note")

modul_tabelle.column("modul", width=250)
modul_tabelle.column("ects", width=70)
modul_tabelle.column("status", width=150)
modul_tabelle.column("note", width=70)

modul_tabelle.insert(
    "",
    "end",
    values=("E-Health", 5, "Bestanden", "1.3")
)
modul_tabelle.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)

fenster.mainloop()