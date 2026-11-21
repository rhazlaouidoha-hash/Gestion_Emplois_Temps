from utilisateur import Utilisateur


class Etudiant(Utilisateur):

    def __init__(self, id, nom, prenom, identifiant, mot_de_passe_hache, groupe,filiere):

        super().__init__( id, nom, prenom, identifiant, mot_de_passe_hache, role="Etudiant")

        self.groupe = groupe
        self.filiere = filiere

    def consulter_emploi_du_temps(self, liste_seances, choix):
     resultat = []
     for s in liste_seances:
        if choix == "groupe" and s.groupe == self.groupe:
            resultat.append(s)
        elif choix == "filiere" and s.filiere == self.filiere:
            resultat.append(s)
     return resultat

    

    def consulter_modifications(self):
        print("Consultation des modifications de l'emploi du temps")

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