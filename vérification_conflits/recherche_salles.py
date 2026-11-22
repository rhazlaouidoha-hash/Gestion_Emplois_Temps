def se_chevauchent(debut1, fin1, debut2, fin2):
    return debut1 < fin2 and debut2 < fin1


def rechercher_salles_libres(   jour,
    heure_debut,
    heure_fin,
    liste_salles,
    liste_seances):
    salles_occupe=[]
    for seance in liste_seances:
       if seance.jour==jour and se_chevauchent(seance.heure_debut,seance.heure_fin ,heure_debut, heure_fin ):
          salles_occupe.append[seance.salle]
    salle_libres=[]
    for salle in liste_salles :
        if salle not in salles_occupe :
           salle_libres.append(salle)

    return salle_libres


def filtrer_salles_par_capacite(salle_libres, nombre_etudiants):
    for salle_libre in salle_libres.copy() :
      if salle_libre.capacite <= nombre_etudiants:
         salle_libres.remove(salle_libre)
    return salle_libres

def filtrer_salles_par_equipements(salle_libres, equipements_requis):
    for salle_libre in salle_libres.copy() :
        for equipement_requis in equipements_requis:
           if equipement_requis not in salle_libre.equipement :
              salle_libres.remove(salle_libre)
              
    return salle_libres  


         