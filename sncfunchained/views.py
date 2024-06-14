from django.http import HttpResponse
from django.shortcuts import render
from sncfunchained.models import Sncfunchained
import random

# Create your views here.

def accueil(request) : 
    # allSncfunchained = Sncfunchained.objects.all()
  
    # On récupère les informations de chaque trajet et les stocke dans des variables.
    # Je préfère ne pas encore faire de boucle pour mieux appréhender les commandes Django. 
    # Mon premier élément commence à l'id 4 , les id précédents étaient des tests.
    trajet_1 = Sncfunchained.objects.get(trainID = 4)
    trajet_2 = Sncfunchained.objects.get(trainID = 5)
    trajet_3 = Sncfunchained.objects.get(trainID = 6)
    trajet_4 = Sncfunchained.objects.get(trainID = 7)
    trajet_5 = Sncfunchained.objects.get(trainID = 8)
    trajet_6 = Sncfunchained.objects.get(trainID = 9)
    trajet_7 = Sncfunchained.objects.get(trainID = 10)
    trajet_8 = Sncfunchained.objects.get(trainID = 11)
    trajet_9 = Sncfunchained.objects.get(trainID = 12)
    trajet_10 = Sncfunchained.objects.get(trainID = 13)
    trajet_11 = Sncfunchained.objects.get(trainID = 15)
    trajet_12= Sncfunchained.objects.get(trainID = 16)
    trajet_13 = Sncfunchained.objects.get(trainID = 17)
    trajet_14 = Sncfunchained.objects.get(trainID = 18)
    trajet_15 = Sncfunchained.objects.get(trainID = 19)
    trajet_16 = Sncfunchained.objects.get(trainID = 20)
    trajet_17 = Sncfunchained.objects.get(trainID = 21)
    trajet_18 = Sncfunchained.objects.get(trainID = 22)
    trajet_19 = Sncfunchained.objects.get(trainID = 23)
    trajet_20 = Sncfunchained.objects.get(trainID = 24)
    # trajet_21 = Sncfunchained.objects.get(trainID = 24)


    # On retourne les 20 id (de 4 à 24), les noms de ville, les 4 départs et les 24 arrivées en chaînes de caractères que l'on réutilise dans accueil HTML.
    return render(request, "sncfunchained/accueil.html", {

        # Trajet 1
        "id4" : trajet_1.trainID,
        "Toulouse" : trajet_1.ville,
        "depart1" : trajet_1.heure_depart,
        "arrivee4" : trajet_1.heure_arrivee,

        # Trajet 2
        "id5" : trajet_2.trainID,
        "Tours" : trajet_2.ville,
        "depart1" : trajet_1.heure_depart,
        "arrivee5" : trajet_2.heure_arrivee,
        
        # Trajet 3
        "id6" : trajet_3.trainID,
        "Montpellier" : trajet_3.ville,
        "depart1" : trajet_1.heure_depart,
        "arrivee6" : trajet_2.heure_arrivee,

        # Trajet 4
        "id7" : trajet_4.trainID,
        "Strasbourg" : trajet_4.ville,
        "depart1" : trajet_1.heure_depart,
        "arrivee7" : trajet_4.heure_arrivee,

        # Trajet 5
        "id8" : trajet_5.trainID,
        "LeHavre" : trajet_5.ville,
        "depart1" : trajet_1.heure_depart,
        "arrivee8" : trajet_5.heure_arrivee,

        # Trajet 6
        "id9" : trajet_6.trainID,
        "Reims" : trajet_6.ville,
        "depart2" : trajet_6.heure_depart,
        "arrivee9" : trajet_6.heure_arrivee,

        # Trajet 7
        "id10" : trajet_7.trainID,
        "Rennes" : trajet_7.ville,
        "depart2" : trajet_6.heure_depart,
        "arrivee10" : trajet_7.heure_arrivee,

        # Trajet 8
        "id11" : trajet_8.trainID,
        "Lyon" : trajet_8.ville,
        "depart2" : trajet_6.heure_depart,
        "arrivee11" : trajet_8.heure_arrivee,

        # Trajet 9
        "id12" : trajet_9.trainID,
        "Marseille" : trajet_9.ville,
        "depart2" : trajet_6.heure_depart,
        "arrivee12" : trajet_9.heure_arrivee,

        # Trajet 10
        "id13" : trajet_10.trainID,
        "Amsterdam" : trajet_10.ville,
        "depart2" : trajet_6.heure_depart,
        "arrivee13" : trajet_10.heure_arrivee,

        # Trajet 11
        "id15" : trajet_11.trainID,
        "Berlin" : trajet_11.ville,
        "depart3" : trajet_11.heure_depart,
        "arrivee14" : trajet_11.heure_arrivee,

        # Trajet 12
        "id16" : trajet_12.trainID,
        "Barcelone" : trajet_12.ville,
        "depart3" : trajet_11.heure_depart,
        "arrivee15" : trajet_12.heure_arrivee,

        # Trajet 13
        "id17" : trajet_13.trainID,
        "Milan" : trajet_13.ville,
        "depart3" : trajet_11.heure_depart,
        "arrivee16" : trajet_13.heure_arrivee,

        # Trajet 14
        "id18" : trajet_14.trainID,
        "Zurich" : trajet_14.ville,
        "depart3" : trajet_11.heure_depart,
        "arrivee17" : trajet_14.heure_arrivee,

        # Trajet 15
        "id19" : trajet_15.trainID,
        "Vienne" : trajet_15.ville,
        "depart3" : trajet_11.heure_depart,
        "arrivee18" : trajet_15.heure_arrivee,

        # Trajet 16
        "id20" : trajet_16.trainID,
        "Prague" : trajet_16.ville,
        "depart4" : trajet_16.heure_depart,
        "arrivee19" : trajet_16.heure_arrivee,

        # Trajet 17
        "id21" : trajet_17.trainID,
        "Nice" : trajet_17.ville,
        "depart4" : trajet_16.heure_depart,
        "arrivee20" : trajet_17.heure_arrivee,

        # Trajet 18
        "id22" : trajet_18.trainID,
        "Bordeaux" : trajet_18.ville,
        "depart4" : trajet_16.heure_depart,
        "arrivee21" : trajet_18.heure_arrivee,

        # Trajet 19
        "id23" : trajet_19.trainID,
        "Lille" : trajet_19.ville,
        "depart4" : trajet_16.heure_depart,
        "arrivee22" : trajet_19.heure_arrivee,

        # Trajet 20
        "id24" : trajet_20.trainID,
        "Angers" : trajet_20.ville,
        "depart4" : trajet_16.heure_depart,
    })

    # trajets = []
    # for i in range(15, 24):  # Boucler sur les IDs de 4 à 24 inclus
    #     trajet = Sncfunchained.objects.get(trainID=i)
    #     trajets.append({
    #         "id": trajet.trainID,
    #         "ville": trajet.ville,
    #         "depart": trajet.heure_depart,
    #         "arrivee": trajet.heure_arrivee
    #     })

    # return render(request, "sncfunchained/accueil.html", {
    #     "trajets": trajets
    # })

def show(request, trainID) : 
    # On récupére chaque trajet correspondant à son ID qu'un réutilise dans l'URL.
    monTrajet = Sncfunchained.objects.get(trainID = trainID)

    # On cree des conditions ternaires lorsque les pages n'existent pas ( en dessous de 4, la page 14 et au au-dessus de 24)
    condition1 = int(trainID) - 1 if int(trainID) > 4 else 4
    condition2 = int(trainID) + 1 if int(trainID) < 24 else 24

    # Puisque ici je n'ai pas d'id 14 je dois mettre 2 conditions pour faire un système de saut de page 
    # si l'id est égal à 15, la page précédente doit être celle de l'id 13
    if int(trainID) == 15 :
        condition1 = 13
    # Si l'id est égal à 13, la page suivante doit être celle de l'id 15
    if int(trainID) == 13 :
        condition2 = 15

    # On crée le dictionnaire "itinéaire" pour stocker les informations du trajet à réutiliser dans le rendu HTML.

    itineraire = {
        "numéro" : monTrajet.trainID,
        "ville": monTrajet.ville,
        "depart": monTrajet.heure_depart,
        "arrivee": monTrajet.heure_arrivee,
        "precedent": condition1,
        "suivant": condition2
    }
    
    return render(request, "sncfunchained/show.html", { 
        "itineraire" : itineraire,
    })
        
def random_trajet():
    # On importe random à l'intérieur de la fonctionne pour une portée locale. Sinon ca ne fonctionne pas
    import random
    # Générer un nombre aléatoire entre 4 et 24
    train_id = random.randint(4, 24)
    # Vérifier si le nombre est égal à 14
    if train_id == 14:
    # S'il est égal à 14, on génère à nouveau un nombre jusqu'à ce qu'il ne soit pas égal à 14
        while train_id == 14:
            train_id == random.randint(4, 24)
    return train_id


def random(request) : 
    # On refait la même chose avec la page random.

    # On va utiliser la méthode random pour générer les trajets aléatoirement
    # On importe la bibliothèque
     
    random_trainID = random_trajet()

    monTrajetaleatoire = Sncfunchained.objects.get(trainID = random_trainID)
        
    itineraire = {
        "numéro" : monTrajetaleatoire.trainID,
        "ville": monTrajetaleatoire.ville,
        "depart": monTrajetaleatoire.heure_depart,
        "arrivee": monTrajetaleatoire.heure_arrivee,
    }
    
    return render(request, "sncfunchained/random.html", { 
        "itineraire" : itineraire
    })
           


def login(request) : 
    return render(request, "sncfunchained/login.html", {})