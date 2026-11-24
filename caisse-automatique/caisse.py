from datetime import datetime

class Article:
    # Mon Constructeur par défaut de la classe Article
    def __init__(self):
        self.__Designation = ""
        self.__Code_barre = 0
        self.__prix = 0.0
        self.__Horaire_scan = "00-00-00"

        # getters
    def get__des(self):
        return self.__Designation

    def get__cb(self):
        return self.__Code_barre

    def get__p(self):
        return self.__prix

    def get__h(self):
        return self.__Horaire_scan

    # Setters
    def set__des(self, des):
        self.__Designation = des

    def set__cb(self, cb):
        self.__Code_barre = cb

    def set__p(self, p):
        self.__prix = p

    def set__h(self, h):
        self.__Horaire_scan = h


class Panier:
    # Mon Constructeur par défaut de la classe Panier
    def __init__(self):
        self.__Date = datetime.now().strftime("%d-%m-%Y")
        self.__article = []

        # Getters
    def get_date(self):
        return self.__Date

    def get_articles(self):
        return self.__article

        # Setters
    def set_date(self, date):
        self.__Date = date

    def set_articles(self, articles):
        self.__article = articles


    def est_vide(self):
        return len(self.__article) == 0

    def ajouter_article(self, article):
        self.__article.append(article)


    def prix_total(self):
        return sum(article.get__p() for article in self.__article)

    def ticket(self):

        print("\n ===== TICKET DE CAISSE ===== \n")

        print(datetime.now())
        heure = str(datetime.now())[11:19]
        print("Heure :", heure)
        date = str(datetime.now())[:10]
        print("Date :", date)
        print("===========================================")


        print("ARTICLES  ", " - "    "    PRIX")
        total = 0
        for article in self.__article:
            print("-------------------------------------------")
            print(article.get__des(), "-", article.get__p(), "DH")
            print("===========================================\n")
            total += article.get__p()
        print("Nombre d'articles :", len(self.__article))
        print("-------------------------------------------")
        print("Montant total :", total, "DH")
        print("-------------------------------------------")

    def duree_courses(self):
        if len(self.__article) < 2:
            return "00:00:00"

        h1 = datetime.strptime(self.__article[0].get__h(), "%H-%M-%S")# Je récupère l'heure du 1er article sous forme de chaine de caractère
        h2 = datetime.strptime(self.__article[-1].get__h(), "%H-%M-%S")#Je recupère l'heure du dernier article
        return h2 - h1

    def menu(self):
        while True:
            print("\n=== MENU PANIER D'ACHAT ===")
            print("1. Ajouter un article")
            print("2. Afficher le ticket")
            print("3. Quitter")


            choix = input("Choisissez une option à éxécuter: ")

            if choix == "1":
                des = input("Désignation : ")
                cb = int(input("Code barre : "))
                prix = float(input("Prix (DH) : "))
                heure = datetime.now().strftime("%H-%M-%S")
                article = Article()
                article.set__des(des)
                article.set__cb(cb)
                article.set__p(prix)
                article.set__h(heure)
                self.ajouter_article(article)
                print("Article ajouté !")
                print("Nombre d'articles :", len(self.__article))
                print("Prix total :", self.prix_total(), "DH")

            elif choix == "2":
                if self.est_vide():
                    print("Le panier est vide !")
                else:
                    self.ticket()
                    print("Durée des courses :", self.duree_courses())
                    print("===========================================")
            elif choix == "3":
                print("===========================================")
                print("AU REVOIR  !")
                print("===========================================")
                return
            else:
                print("Option invalide. Réessayez.")

#Je lance
p = Panier()
p.menu()