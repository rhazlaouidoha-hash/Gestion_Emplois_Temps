def se_chevauchent(debut1, fin1, debut2, fin2):
    return debut1 < fin2 and debut2 < fin1
     
def verifier_disponibilite_enseignant(nouvelle_seance, disponibilites):

    for dispo in disponibilites:

        if nouvelle_seance.jour == dispo.jour:

            if se_chevauchent(
                nouvelle_seance.heure_debut,
                nouvelle_seance.heure_fin,
                dispo.heure_debut,
                dispo.heure_fin
            ):

                return False, "L’enseignant a signalé son indisponibilité pendant cette période. Veuillez sélectionner un créneau compatible avec ses disponibilités."

    return True, "L'enseignant est disponible pour ce créneau horaire."

def verifier_disponibilite_salle(nouvelle_seance, liste_seances):

    for seance in liste_seances:

        if (nouvelle_seance.salle == seance.salle
            and nouvelle_seance.jour == seance.jour):

            if se_chevauchent(
                nouvelle_seance.heure_debut,
                nouvelle_seance.heure_fin,
                seance.heure_debut,
                seance.heure_fin
            ):

                return False, "La salle sélectionnée n'est pas disponible pour ce créneau horaire. Veuillez choisir une autre salle ou un autre créneau."

    return True, "La salle sélectionnée est disponible pour ce créneau horaire."    

