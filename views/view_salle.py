import customtkinter as ctk
from tkinter import ttk
from services.services_salle import ServiceSalle
from models.salle import Salle


class ViewSalle(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("600x500")

        self.service = ServiceSalle()

        # ========================
        self.cadreInfo = ctk.CTkFrame(self)
        self.cadreInfo.pack(pady=10)

        self.entry_code = ctk.CTkEntry(self.cadreInfo, placeholder_text="Code")
        self.entry_code.grid(row=0, column=0, padx=5, pady=5)

        self.entry_desc = ctk.CTkEntry(self.cadreInfo, placeholder_text="Description")
        self.entry_desc.grid(row=0, column=1, padx=5, pady=5)

        self.entry_cat = ctk.CTkEntry(self.cadreInfo, placeholder_text="Catégorie")
        self.entry_cat.grid(row=1, column=0, padx=5, pady=5)

        self.entry_cap = ctk.CTkEntry(self.cadreInfo, placeholder_text="Capacité")
        self.entry_cap.grid(row=1, column=1, padx=5, pady=5)

        # ================================
        self.cadreBtn = ctk.CTkFrame(self)
        self.cadreBtn.pack(pady=10)

        ctk.CTkButton(self.cadreBtn, text="Ajouter", command=self.ajouter_salle).grid(row=0, column=0, padx=5)
        ctk.CTkButton(self.cadreBtn, text="Modifier", command=self.modifier_salle).grid(row=0, column=1, padx=5)
        ctk.CTkButton(self.cadreBtn, text="Supprimer", command=self.supprimer_salle).grid(row=0, column=2, padx=5)
        ctk.CTkButton(self.cadreBtn, text="Rechercher", command=self.rechercher_salle).grid(row=0, column=3, padx=5)

        # =========================
        self.tree = ttk.Treeview(self, columns=("code", "desc", "cat", "cap"), show="headings")

        self.tree.heading("code", text="Code")
        self.tree.heading("desc", text="Description")
        self.tree.heading("cat", text="Catégorie")
        self.tree.heading("cap", text="Capacité")

        self.tree.pack(expand=True, fill="both", padx=10, pady=10)

        self.lister_salles()

    # ====================================

    def ajouter_salle(self):
        s = Salle(
            self.entry_code.get(),
            self.entry_desc.get(),
            self.entry_cat.get(),
            int(self.entry_cap.get())
        )

        ok, msg = self.service.ajouter_salle(s)
        print(msg)
        self.lister_salles()

    def modifier_salle(self):
        s = Salle(
            self.entry_code.get(),
            self.entry_desc.get(),
            self.entry_cat.get(),
            int(self.entry_cap.get())
        )

        self.service.modifier_salle(s)
        self.lister_salles()

    def supprimer_salle(self):
        code = self.entry_code.get()
        print("Code saisi =", repr(code))

        self.service.supprimer_salle(code)
        self.lister_salles()
#=========================================
    def rechercher_salle(self):
        code = self.entry_code.get()
        s = self.service.rechercher_salle(code)

        if s:
            self.entry_desc.delete(0, "end")
            self.entry_cat.delete(0, "end")
            self.entry_cap.delete(0, "end")

            self.entry_desc.insert(0, s.description)
            self.entry_cat.insert(0, s.categorie)
            self.entry_cap.insert(0, s.capacite)
#================================================
    def lister_salles(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        liste = self.service.recuperer_salles()

        for s in liste:
            self.tree.insert("", "end", values=(s.code, s.description, s.categorie, s.capacite))