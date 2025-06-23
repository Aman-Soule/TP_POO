import logging

# Configuration du fichier de log
logging.basicConfig(
    filename='ventes.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class StockInsuffisantException(Exception):
    """Exception levée quand le stock est insuffisant."""
    pass


class Produit():
    nom = ""
    prix = 0
    quantite_stock = 0
    
    def __init__(self, nom , prix ,quantite_stock):
        self.nom = nom
        self.prix = prix
        self.quantite_stock = quantite_stock
    
    def afficher_infos(self):
        print(f"INFORMATION SUR LE PRODUIT : {self.nom}")
        print(f"Nom : {self.nom}\nPrix : {self.prix} FCFA\nQuantite en stock : {self.quantite_stock}")
        
    def vendre(self):
        print("Vente du produit")
        stock = int(input("Saisir la quantite de produit a vendre : "))
        
        if stock > self.quantite_stock:
            print("La quantite saisie est superieure au stock disponible")
        else:
            self.quantite_stock = self.quantite_stock - stock
            
class Commande:
    def __init__(self, produit, quantite):
        self.produit = produit
        self.quantite = quantite
         
    def infos_commande(self):
        print("\nInfos sur la commande")
        print(f"Produit : {self.produit.nom}\nQuantité : {self.quantite}")
    
    def passer_commande(self):
        print("\nPasser une commande")
        try:
            qte = int(input("Saisir la quantité que vous voulez commander : "))
            if qte > self.produit.quantite_stock:
                raise StockInsuffisantException("La quantité saisie est supérieure au stock disponible.")
            self.quantite_stock -= qte
            logging.info(f"Commande | Produit: {self.produit.nom} | Quantité commandée: {qte} | Stock restant: {self.produit.quantite_stock}")
            print("Commande passée avec succès !")
        except StockInsuffisantException as e:
            logging.warning(f"Échec de commande | {self.produit.nom} | Stock demandé: {qte} | Stock disponible: {self.produit.quantite_stock}")
            print(e)
            

p1 = Produit("Chocolat", 300, 2)
p2 = Produit("Lait", 1000, 234)
p1.afficher_infos()
#p2.vendre()
p2.afficher_infos()
p2.vendre()
p2.afficher_infos()

c1 = Commande(p1,23)
c1.infos_commande()
c1.passer_commande()