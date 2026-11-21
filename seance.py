class Seance:

    def __init__(self, id, matiere, enseignant,  groupe ,filiere,salle=None, jour=None, heure_debut=None, heure_fin=None,):

        self.id = id
        self.matiere = matiere
        self.enseignant = enseignant
        self.salle = salle
        self.groupe = groupe
        self.filiere=filiere
        self.jour = jour
        self.heure_debut = heure_debut
        self.heure_fin = heure_fin
        

    



    def afficher_infos(self):
        print("Matière :", self.matiere)
        print("Enseignant :", self.enseignant)
        print("Salle :", self.salle)
        print("Groupe :", self.groupe)
        print("Jour :", self.jour)
        print("Début :", self.heure_debut)
        print("Fin :", self.heure_fin)

    def modifier_horaire(self, nouveau_debut, nouvelle_fin):
        self.heure_debut = nouveau_debut
        self.heure_fin = nouvelle_fin

    def modifier_salle(self, nouvelle_salle):
        self.salle = nouvelle_salle


    def modifier_jour(self, nouveau_jour):
     self.jour = nouveau_jour