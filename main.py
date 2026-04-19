from models.salle import Salle

s1 = Salle("A01", "Salle infos", "Laboratoire", 27)
s1.afficher_infos()

from Data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

s = Salle("D02", "Salle simple", "Classe", 10)
dao.insert_salle(s)

liste = dao.get_salles()
for salle in liste:
    salle.afficher_infos()