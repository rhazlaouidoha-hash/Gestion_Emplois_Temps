from utilisateur import Utilisateur
from disponibilite import Disponibilite
from reservation import Reservation




class Enseignant(Utilisateur):

    def __init__(self, id, nom, prenom, identifiant,
                  mot_de_passe_hache, specialite):

        super().__init__(
            id, nom, prenom, identifiant,
            mot_de_passe_hache, role="Enseignant"
        )

        self.specialite = specialite

    def consulter_emploi_du_temps(self, liste_seances):
     resultat = []
     for s in liste_seances:
        if s.enseignant == self.identifiant:
            resultat.append(s)
     return resultat
    

    def signaler_indisponibilite(self, liste_disponibilites, jour, heure_debut, heure_fin):

        d = Disponibilite(
            len(liste_disponibilites) + 1,
            self.identifiant,
            jour,
            heure_debut,
            heure_fin,
            False
        )

        liste_disponibilites.append(d)

        return d


    def rechercher_salles_libres(self, liste_salles, liste_seances, jour, heure_debut, heure_fin):
         salles_libres = []

         for salle in liste_salles:
            libre = True

            for s in liste_seances:
                if s.salle == salle.numero and s.jour == jour:
                    if heure_debut < s.heure_fin and heure_fin > s.heure_debut:
                        libre = False
                        break

            if libre:
                salles_libres.append(salle)

         return salles_libres

    def demander_reservation(self, liste_reservations, salle, jour, heure_debut, heure_fin):

     r = Reservation(
        len(liste_reservations) + 1,
        self.identifiant,
        salle,
        jour,
        heure_debut,
        heure_fin
    )

     liste_reservations.append(r)

     print("Demande de réservation envoyée.")
     return r