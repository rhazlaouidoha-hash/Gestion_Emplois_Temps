def se_chevauchent(debut1,fin1,debut2,fin2):
    return (debut1 >=debut2 and debut1 <=fin2)or (fin1<=fin2 and fin1>=debut2)
                  
def verifier_conflit_salle(nouvelle_seance, liste_seances):
    for seance in liste_seances:
        if nouvelle_seance.salle==seance.salle:
            if se_chevauchent(nouvelle_seance.heure_debut,nouvelle_seance.heure_fin,seance.heure_debut,seance.heure_fin):
                  return False,"La salle sélectionnée est déjà occupée pendant ce créneau horaire. Veuillez choisir une autre salle ou un autre créneau."
    return False,"Erreur : La salle sélectionnée est introuvable. Veuillez choisir une salle valide."                  
           

def verifier_conflit_enseignant(nouvelle_seance, liste_seances):
    for seance in liste_seances:
        if  nouvelle_seance.enseignant==seance.enseignant:
            if (nouvelle_seance.jour==seance.jour) and  se_chevauchent(nouvelle_seance.heure_debut,nouvelle_seance.heure_fin,seance.heure_debut,seance.heure_fin):
                return False,"L’enseignant sélectionné possède déjà une séance programmée pendant cette période. Veuillez modifier le créneau horaire."
    return False ,"Erreur : L’enseignant sélectionné n’existe pas dans le système. Veuillez vérifier votre choix ou sélectionner un enseignant valide."
                
def verifier_conflit_groupe(nouvelle_seance, liste_seances):
    for seance in liste_seances:
         if  nouvelle_seance.groupe==seance.groupe:
            if(nouvelle_seance.jour==seance.jour)and se_chevauchent(nouvelle_seance.heure_debut,nouvelle_seance.heure_fin,seance.heure_debut,seance.heure_fin):
              return False,"Le groupe concerné possède déjà une séance programmée pendant cette période. Veuillez choisir un autre créneau"
    return False,"Le groupe sélectionné n’existe pas dans le système. Veuillez vérifier le nom du groupe et réessayer."     
# La base de données nous fournit la liste des indisponibilités
# correspondant à un enseignant spécifique.
# Cette liste contient les périodes pendant lesquelles l'enseignant
# a signalé qu'il n'est pas disponible.
def verifier_disponibilite_enseignant(nouvelle_seance,disponibilites):
    for dispo in disponibilites:
       if(nouvelle_seance.jour==dispo.jour and nouvelle_seance.heure_debut==dispo.heure_debut and nouvelle_seance.heure_fin==dispo.heure_fin ):
              return False,"L’enseignant a signalé son indisponibilité pendant cette période. Veuillez sélectionner un créneau compatible avec ses disponibilités."
    return True,"L'enseignant est disponible pour ce créneau horaire."
def verifier_disponibilite_salle(nouvelle_seance,liste_seances):
    for seance in liste_seances:
        if nouvelle_seance.salle== seance.salle and nouvelle_seance.jour == seance.jour and se_chevauchent():
            return False, "La salle sélectionnée n'est pas disponible pour ce créneau horaire. Veuillez choisir une autre salle ou un autre créneau."
    return True ,"La salle sélectionnée est  disponible pour ce créneau horaire."     

def verifier_capacite_salle(nouvelle_seance, liste_salles,nombre_etudiants ):
    for salle in liste_salles:
        if nouvelle_seance.salle==salle.numero:

            if nombre_etudiants > salle.capacite :
                 return False, "La capacité de la salle sélectionnée est insuffisante pour accueillir tous les étudiants du groupe. Veuillez choisir une salle plus grande."

             
def verifier_equipements(nouvelle_seance , liste_salles , equipements_requis):
     for salle in liste_salles:
            if nouvelle_seance.salle==salle.numero:
               for equipement_requis in equipements_requis:
                 for salle.equipement in salle.equipements :
                    if equipement_requis ==salle.equipement :
                         return False, "La capacité de la salle sélectionnée est insuffisante pour accueillir tous les étudiants du groupe. Veuillez choisir une salle plus grande."
    
def detecter_conflits(nouvelle_seance, liste_seances):
    pass
def rechercher_capacite_salle(salle_rech,liste_salles):
     for salle in liste_salles:
         if salle_rech.numero ==salle.numero :
             if salle_rech.capacite== salle.capacite :
                 return 1