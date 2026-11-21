
from utilisateur import Utilisateur


class Administrateur(Utilisateur):

    def __init__(self, id, nom, prenom, identifiant, mot_de_passe_hache):

        super().__init__(
            id, nom, prenom, identifiant,
            mot_de_passe_hache, role="Administrateur"
        )

        self.liste_utilisateurs = []
        self.liste_salles = []
        self.liste_matieres = []
        self.liste_reservations = []
        self.liste_emploi_du_temps = []

    

    def ajouter_utilisateur(self, utilisateur1):
        self.liste_utilisateurs.append(utilisateur1)
        return True

    def afficher_utilisateurs(self):
        for u in self.liste_utilisateurs:
            u.afficher_infos()

    def modifier_utilisateur(self, id, nouveau_nom, nouveau_prenom):
        for u in self.liste_utilisateurs:
            if u.id == id:
                u.modifier_infos(nouveau_nom, nouveau_prenom)
                print("Utilisateur modifié avec succès.")
                return True
        print("Utilisateur introuvable.")
        return False

    def supprimer_utilisateur(self, id):
        for u in self.liste_utilisateurs:
            if u.id == id:
                self.liste_utilisateurs.remove(u)
                print("Utilisateur supprimé avec succès.")
                return True
        print("Utilisateur introuvable.")
        return False

    

    def ajouter_salle(self, salle1):
        self.liste_salles.append(salle1)
        print("Salle ajoutée avec succès.")
        return True

    def afficher_salles(self):
        for s in self.liste_salles:
            s.afficher_infos()

    def supprimer_salle(self, id):
        for s in self.liste_salles:
            if s.id == id:
                self.liste_salles.remove(s)
                print("Salle supprimée avec succès.")
                return True
        print("Salle introuvable.")
        return False

    

    def ajouter_matiere(self, matiere1):
        self.liste_matieres.append(matiere1)
        print("Matière ajoutée avec succès.")
        return True

    def afficher_matieres(self):
        for m in self.liste_matieres:
            m.afficher_infos()

    def supprimer_matiere(self, id):
        for m in self.liste_matieres:
            if m.id == id:
                self.liste_matieres.remove(m)
                print("Matière supprimée avec succès.")
                return True
        print("Matière introuvable.")
        return False

    

    def generer_emploi_du_temps(self, seances1):
        self.liste_emploi_du_temps = seances1
        print("Emploi du temps enregistré.")
        return True

    def afficher_emploi_du_temps(self):
        for s in self.liste_emploi_du_temps:
            s.afficher_infos()

   

    def ajouter_reservation(self, reservation1):
        self.liste_reservations.append(reservation1)
        return True

    def consulter_reservations(self):
        for r in self.liste_reservations:
            r.afficher_infos()

    def accepter_reservation(self, id):
        for r in self.liste_reservations:
            if r.id == id:
                r.accepter()
                print("Réservation acceptée.")
                return True
        print("Réservation introuvable.")
        return False

    def refuser_reservation(self, id):
        for r in self.liste_reservations:
            if r.id == id:
                r.refuser()
                print("Réservation refusée.")
                return True
        print("Réservation introuvable.")
        return False
