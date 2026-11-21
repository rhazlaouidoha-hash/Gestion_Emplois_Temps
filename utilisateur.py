import bcrypt


class Utilisateur:

    def __init__(self, id, nom, prenom, identifiant, mot_de_passe_hache, role):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.identifiant = identifiant
        self.mot_de_passe = mot_de_passe_hache
        self.role = role

    @staticmethod
    def hasher(mot_de_passe):
        return bcrypt.hashpw(mot_de_passe.encode('utf-8'), bcrypt.gensalt())

    def afficher_infos(self):
        print("Nom :", self.nom)
        print("Prénom :", self.prenom)
        print("Identifiant :", self.identifiant)
        print("Rôle :", self.role)

    def modifier_infos(self, nouveau_nom, nouveau_prenom):
        self.nom = nouveau_nom
        self.prenom = nouveau_prenom

    def definir_mot_de_passe(self, mot_de_passe):
        self.mot_de_passe = Utilisateur.hasher(mot_de_passe)

    def verifier_identifiants(self, identifiant, mot_de_passe):
        if self.identifiant != identifiant:
            return False
        return bcrypt.checkpw(mot_de_passe.encode('utf-8'), self.mot_de_passe)

    def changer_mot_de_passe(self, nouveau_mot_de_passe):
        self.definir_mot_de_passe(nouveau_mot_de_passe)