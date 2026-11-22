def se_chevauchent(debut1, fin1, debut2, fin2):
    return debut1 < fin2 and debut2 < fin1
                  
def verifier_conflit_salle(nouvelle_seance, liste_seances):

    for seance in liste_seances:

        if (nouvelle_seance.salle == seance.salle
            and nouvelle_seance.jour == seance.jour):

            if se_chevauchent(
                nouvelle_seance.heure_debut,
                nouvelle_seance.heure_fin,
                seance.heure_debut,
                seance.heure_fin
            ):

                return False, "La salle sélectionnée est déjà occupée pendant ce créneau horaire. Veuillez choisir une autre salle ou un autre créneau."

    return True, "Aucun conflit détecté : la salle est disponible."

def verifier_conflit_enseignant(nouvelle_seance, liste_seances):

    for seance in liste_seances:

        if (nouvelle_seance.enseignant == seance.enseignant
            and nouvelle_seance.jour == seance.jour):

            if se_chevauchent(
                nouvelle_seance.heure_debut,
                nouvelle_seance.heure_fin,
                seance.heure_debut,
                seance.heure_fin
            ):

                return False, "L’enseignant sélectionné possède déjà une séance programmée pendant cette période. Veuillez modifier le créneau horaire."

    return True, "Aucun conflit détecté : l’enseignant est disponible."

def verifier_conflit_groupe(nouvelle_seance, liste_seances):

    for seance in liste_seances:

        if (nouvelle_seance.groupe == seance.groupe
            and nouvelle_seance.jour == seance.jour):

            if se_chevauchent(
                nouvelle_seance.heure_debut,
                nouvelle_seance.heure_fin,
                seance.heure_debut,
                seance.heure_fin
            ):

                return False, "Le groupe concerné possède déjà une séance programmée pendant cette période. Veuillez choisir un autre créneau."

    return True, "Aucun conflit détecté : le groupe est disponible."

def verifier_capacite_salle(nouvelle_seance, liste_salles, nombre_etudiants):

    for salle in liste_salles:

        if nouvelle_seance.salle == salle.numero:

            if nombre_etudiants > salle.capacite:

                return False, "La capacité de la salle sélectionnée est insuffisante pour accueillir tous les étudiants du groupe. Veuillez choisir une salle plus grande."

            return True, "La capacité de la salle est suffisante."

    return False, "Erreur : La salle sélectionnée est introuvable."
             
def verifier_equipements(nouvelle_seance, liste_salles, equipements_requis):

    for salle in liste_salles:

        if nouvelle_seance.salle == salle.numero:

            for equipement_requis in equipements_requis:

                if equipement_requis not in salle.equipements:

                    return False, "La salle sélectionnée ne dispose pas de tous les équipements requis pour cette séance. Veuillez choisir une salle adaptée."

            return True, "Tous les équipements requis sont disponibles."

    return False, "Erreur : La salle sélectionnée est introuvable."

def detecter_conflits(nouvelle_seance, liste_seances):

    conflits = []

    resultat_salle, message_salle = verifier_conflit_salle(
        nouvelle_seance, liste_seances
    )

    resultat_enseignant, message_enseignant = verifier_conflit_enseignant(
        nouvelle_seance, liste_seances
    )

    resultat_groupe, message_groupe = verifier_conflit_groupe(
        nouvelle_seance, liste_seances
    )

    if not resultat_salle:
        conflits.append(message_salle)

    if not resultat_enseignant:
        conflits.append(message_enseignant)

    if not resultat_groupe:
        conflits.append(message_groupe)

    if conflits:
        return False, conflits

    return True, "Aucun conflit détecté. La séance peut être programmée."


