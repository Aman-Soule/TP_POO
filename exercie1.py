class Membre:
    nom = "Aman"
    prenom= "Soule"
    age = 18
    etat = 1
    
    def __init__(self, nom ,prenom, age, etat):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.etat = etat
    def afficher_infos(self):
        if self.etat == 1:
            etat = "Actif"
        else:
            etat = "Inactif"
        print(f"Nom : {self.nom}   Prenom : {self.prenom}  Age : {self.age}   Statut = {etat} ")
    def changer_statut(self):
        if self.etat == 1:
            self.etat = 0
        else:
            self.etat = 1
        print("Statut mdifié")
    def valider_age(self):
        if self.age < 0:
            print("AgeInvalideException")
        else:
            print("Age valide !")        
            
        
m1 = Membre("Bruno", "Fernandes", 28, 0)
m2 = Membre("Alice", "Noé", -12, 1)
# print(m1.nom, m1.prenom, m1.age)
m1.afficher_infos()
print(m1)
m1.changer_statut()
m1.afficher_infos()

m2.valider_age()
        