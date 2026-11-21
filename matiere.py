class Matiere:

    def __init__(self, id, nom, volume_horaire, type_seance,equipements_requis=None):

        self.id = id
        self.nom = nom
        self.volume_horaire = volume_horaire
        self.type_seance = type_seance
        self.equipements_requis = equipements_requis or []

    def afficher_infos(self):
        print("Nom :", self.nom)
        print("Volume horaire :", self.volume_horaire)
        print("Type de séance :", self.type_seance)

    def modifier_volume_horaire(self, nouveau_volume):
        self.volume_horaire = nouveau_volume

    def modifier_type_seance(self, nouveau_type):
        self.type_seance = nouveau_type