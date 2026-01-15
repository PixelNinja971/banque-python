# -------------------------
# Gestion de clients - Banque
# -------------------------

# Client de la banque
clients = ["Georges Dupont", "Luc Martin", "Lucas Anderson", "Alexandre Petit" , "Patricia Koffi", "Jessica Alba"]

# Dictionnaire : nom du client -> solde
comptes = {
    "Georges Dupont": 10000,
    "Luc Martin": 150,
    "Lucas Anderson": 300,
    "Alexandre Petit": 1800.74,
    "Patricia Koffi" : 30000,
    "Jessica Alba" : 7800.91
}

def afficher_menu():
    print("\n===== MENU BANQUE =====")
    print("1 - Afficher les clients")
    print("2 - Afficher le solde d'un client")
    print("3 - Déposer de l'argent")
    print("4 - Retirer argent")
    print("5 - Ajouter un client")
    print("6 - Quitter")


def afficher_clients():
    print("\n===== Client de la banque =====")
    for name in clients :
        print(name)
    print("Nombre total de clients :", len(clients))


def demande_nom_clients():
    nom = input ("Entrez le nom complet du client :")
    return nom

def afficher_solde():

    print("\n===== Solde du compte =====")
    nom = demande_nom_clients()
    if nom in comptes :
        print("le solde de", nom, " est de", comptes[nom], "€")
    else:
        client_introuvable()    
  

def deposit():
    depot = float(input ("Montant de votre depôt :"))
    return depot

def deposer_argent():

    print("\n===== Déposer vous billet =====")
    nom = demande_nom_clients()

    if nom in comptes :
        depot = deposit()
        if depot >= 1 : 
            comptes[nom] = comptes[nom] + depot
            print("Le nouveau solde de", nom, "est de", comptes[nom], "€")
    else:
        client_introuvable()       

        
def withdrawal():
    retrait = int(input ("Montant de votre retrait :"))
    return retrait

def retrait_argent():

    print("\n===== Retrait d'argent =====")
    nom = demande_nom_clients()
    if nom in comptes :
        retrait = withdrawal()
        if retrait >= 1 : 
            comptes[nom] = comptes[nom] - retrait
            print("Le nouveau solde de", nom, "est de", comptes[nom], "€")
    else:
            client_introuvable()           


def nouveau_client():
    nouveau = input ("Nom nouveau client : ")
    return nouveau

def ajout_client():
       nom = nouveau_client()

       if nom in comptes:
            print("Ce client existe déjà.")
            return

       clients.append(nom)
       comptes[nom] = 0 
       print("Client ajouté :", nom)
       

def client_introuvable():
    print("Le client n'hésite pas, ajoute-le.")
    reponse = input("Voulez-vous l'ajouter ? (o/n) : ")
    if reponse.lower() == "o":
        ajout_client()


           
while True:
    afficher_menu()
    choix = input("Choix : ")

    if choix == "1":
        afficher_clients()

    elif choix == "2":
        afficher_solde()

    elif choix == "3":
        deposer_argent()

    elif choix == "4":
        retrait_argent()   

    elif choix == "5":
        ajout_client()

    elif choix == "6":
        print("Au revoir !")
        break    

 