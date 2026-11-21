class Reservation:

    def __init__(self, id, enseignant, salle, jour, heure_debut, heure_fin):

        self.id = id
        self.enseignant = enseignant
        self.salle = salle
        self.jour = jour
        self.heure_debut = heure_debut
        self.heure_fin = heure_fin
        self.statut = "En attente"

    def afficher_infos(self):
        print("Enseignant :", self.enseignant)
        print("Salle :", self.salle)
        print("Jour :", self.jour)
        print("Début :", self.heure_debut)
        print("Fin :", self.heure_fin)
        print("Statut :", self.statut)

    def accepter(self):
        self.statut = "Acceptée"

    def refuser(self):
        self.statut = "Refusée"