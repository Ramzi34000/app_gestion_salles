import mysql.connector
import json
from models.salle import Salle


class DataSalle:

    def get_connection(self):
        f = open("Data/config.json")
        config = json.load(f)

        conn = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        return conn

    def insert_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()

        # Vérifier si la salle existe déjà
        cursor.execute("SELECT * FROM salle WHERE code=%s", (salle.code,))
        result = cursor.fetchone()

        if result:
            print("Erreur : salle déjà existe")
        else:
            cursor.execute(
                "INSERT INTO salle VALUES (%s, %s, %s, %s)",
                (salle.code, salle.description, salle.categorie, salle.capacite)
            )
            conn.commit()
            print("Salle ajoutée")

        conn.close()

    def get_salles(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM salle")
        result = cursor.fetchall()

        salles = []
        for r in result:
            s = Salle(r[0], r[1], r[2], r[3])
            salles.append(s)

        conn.close()
        return salles

    def get_salle(self, code):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM salle WHERE code = %s", (code,))
        r = cursor.fetchone()

        conn.close()

        if r:
            return Salle(r[0], r[1], r[2], r[3])
        else:
            return None

    def delete_salle(self, code):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM salle WHERE code = %s", (code,))
        conn.commit()

        conn.close()

    def update_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE salle SET description=%s, categorie=%s, capacite=%s WHERE code=%s",
            (salle.description, salle.categorie, salle.capacite, salle.code)
        )

        conn.commit()
        conn.close()