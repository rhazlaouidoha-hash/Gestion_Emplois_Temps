class Disponibilite:

    def __init__(self, id, enseignant, jour, heure_debut, heure_fin, disponible):

        self.id = id
        self.enseignant = enseignant
        self.jour = jour
        self.heure_debut = heure_debut
        self.heure_fin = heure_fin
        self.disponible = disponible

    def afficher_infos(self):
        print("Enseignant :", self.enseignant)
        print("Jour :", self.jour)
        print("De :", self.heure_debut)
        print("À :", self.heure_fin)
        print("Disponible :", self.disponible)

    def modifier_horaires(self, nouveau_debut, nouvelle_fin):
        self.heure_debut = nouveau_debut
        self.heure_fin = nouvelle_fin

    def est_disponible(self):
        return self.disponible