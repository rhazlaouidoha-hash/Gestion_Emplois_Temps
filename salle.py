class Salle:

    def __init__(self, id, numero, capacite, type_salle):

        self.id = id
        self.numero = numero
        self.capacite = capacite
        self.type_salle = type_salle
        self.equipements = []

    def afficher_infos(self):
        print("Numéro :", self.numero)
        print("Capacité :", self.capacite)
        print("Type :", self.type_salle)
        print("Équipements :", self.equipements)

    def modifier_capacite(self, nouvelle_capacite):
        self.capacite = nouvelle_capacite

    def ajouter_equipement(self, equipement):
        self.equipements.append(equipement)

    def est_adaptee(self, nombre_etudiants, equipements_requis=()):
     if self.capacite < nombre_etudiants:
        return False
     
     noms = [e.nom for e in self.equipements]
     
     for nom in equipements_requis:
        if nom not in noms:
            return False
     return True