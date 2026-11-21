class Filiere:

    def __init__(self, id, nom, description):

        self.id = id
        self.nom = nom
        self.description = description
        self.liste_groupes = []

    def afficher_infos(self):
        print("Nom :", self.nom)
        print("Description :", self.description)

    def ajouter_groupe(self, groupe):
        self.liste_groupes.append(groupe)

    def afficher_groupes(self):
        for g in self.liste_groupes:
            print(g.nom)