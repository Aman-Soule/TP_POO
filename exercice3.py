import logging
from datetime import datetime
from functools import wraps

logging.basicConfig(
    filename='projets.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DateLimiteInvalideException(Exception):
    pass

def valider_date_limite(fonction):
    @wraps(fonction)
    def wrapper(*args, **kwargs):
        date_limite = kwargs.get('date_limite')
        if not date_limite:
            date_limite = args[3]

        if isinstance(date_limite, str):
            date_limite = datetime.strptime(date_limite, "%Y-%m-%d")

        if date_limite < datetime.now():
            logging.error("Erreur : date limite dans le passé.")
            raise DateLimiteInvalideException("La date limite ne peut pas être dans le passé.")
        
        return fonction(*args, **kwargs)
    return wrapper

class Projet:
    @valider_date_limite
    def __init__(self, nom, date_debut, date_limite, statut="En cours"):
        self.nom = nom
        self.date_debut = datetime.strptime(date_debut, "%Y-%m-%d")
        self.date_limite = datetime.strptime(date_limite, "%Y-%m-%d")
        self.statut = statut
        logging.info(f"Projet ajouté : {self.nom} | Statut : {self.statut}")

    def afficher_infos(self):
        print("\nINFOS DU PROJET")
        print(f"Nom : {self.nom}")
        print(f"Date de début : {self.date_debut.strftime('%d/%m/%Y')}")
        print(f"Date limite : {self.date_limite.strftime('%d/%m/%Y')}")
        print(f"Statut : {self.statut}")

    def terminer(self):
        self.statut = "Terminé"
        logging.info(f"Statut mis à jour pour {self.nom} : {self.statut}")
        print(f"\nLe projet '{self.nom}' est maintenant terminé.")


projet1 = Projet("Site Web ISI", "2025-06-20", "2025-07-30")
projet1.afficher_infos()
projet1.terminer()
projet1.afficher_infos()

