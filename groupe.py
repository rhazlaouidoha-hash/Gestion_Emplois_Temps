class Groupe:

    def __init__(self, id, nom, niveau, nombre_etudiants):

        self.id = id
        self.nom = nom
        self.niveau = niveau
        self.nombre_etudiants = nombre_etudiants

    def afficher_infos(self):
        print("Nom :", self.nom)
        print("Niveau :", self.niveau)
        print("Nombre d'étudiants :", self.nombre_etudiants)

    def modifier_nombre_etudiants(self, nouveau_nombre):
        self.nombre_etudiants = nouveau_nombre