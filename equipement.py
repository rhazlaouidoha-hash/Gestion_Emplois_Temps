class Equipement:

    def __init__(self, id, nom, quantite, description):

        self.id = id
        self.nom = nom
        self.quantite = quantite
        self.description = description

    def afficher_infos(self):
        print("Nom :", self.nom)
        print("Quantité :", self.quantite)
        print("Description :", self.description)

    def modifier_quantite(self, nouvelle_quantite):
        self.quantite = nouvelle_quantite