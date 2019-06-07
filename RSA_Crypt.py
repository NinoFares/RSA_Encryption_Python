## Programme pour manipuler RSA
# Bouzid Fares Abdelnour 08/11/2018

# WARNING: IMPORTANT !!! : Programme a éxécuter avec python3 et non python

##      Sommaire        ##
#   Fonction PGCD
#   Fonction EGCD (Euclide etendu)
#   Fonction Modulo inverse
#   Fonction teste de primalité
#   Fonction de Factorisation
#   Fonction pour Génerer deux nombre premier distinct
#   Fonction pour calculer le coéficient de cryptage en fonction de phi de n
#   Fonction pour génerer clé privé et public
#   Fonction pour afficher les valeurs
#   Fonction pour le menu
#   Fonction pour chiffrer avec des valeur aléatoire
#   Fonction pour chiffrer avec clé public
#   Fonction pour déchiffrer avec clé privé
#   Fonction pour déchiffrer avec clé public (Factorisation)
#   Fonction pour chiffrer une chaine de caractéres
#   Fonction pour quiiter le Programme
#   MAIN


import random
import sys

#					Fonction pour faire PGCD			#
def pgcd(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a;


#				Fonction du théoréme d'euclide étendu			#
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y);


#					Fonction du modulo inverse			#
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Erreur, pas de modulo inverse.');
    return x%m;


#				Fonction pour le teste de primalité			#
def isPrime(num):
        for x in range(int(num) - 1, 1, -1):
            if int(num) % x == 0:
                return False
        return True;

#               Fonction de factorisation                   #
def factoriser(n):
    b=2
    p=n
    q=1
    while (n/2)>=b:
        while n%b!=0 :
            b=b+1
        if n%b==0:
            p = b
            break
    q=n/p
    return [p,q];

#               Fonction pour génrer deux nombre premier distinct       #
def deuxNombrePrimeDis():
    p = random.randint(3,10000)
    q = random.randint(3,10000)

    #On les regénére tant que ils ne sont pas premier et différent
    while not isPrime(p):
    	p = random.randint(3,10000)
    while not isPrime(q) or p==q:
    	q = random.randint(3,10000)
    return p,q;


#               Fonction pour calculer e                                #
def calculerE(phi):
    e=3
    while e<phi:
    	if pgcd(e,phi)==1:
    		break
    	else:
    		e+=1
    	if e>=phi:
            raise Exception('Erreur, impossible de calculer e.')
            sys.exit(-1);
    return e;



#               Fonction pour afficher toute les valeurs                #
def afficher(p,q,n,e,phi,d):
    print("p = ",p)
    print("q = ",q)
    print("n = ",n)
    print("e = ",e)
    print("phi = ",phi)
    print("d = ",d)
    print("Clé public (",e,",",n,") et Clé privé (",d,",",n,")")

#                           MENU                        #

def menu():
    print()
    print("****         Programme manipulation RSA      ****")
    print("0 - Générer des clés RSA.")
    print("1 - Chiffrer avec clé public.")
    print("2 - Déchiffrer un nombre avec clé privé.")
    print("3 - Déchiffrer un nombre avec clé public (factorisation). ")
    print("4 - Chiffrer une phrase.")
    print("5 - Déchifrer une phrase")
    print("6 - Quitter.")
    return input("Votre choix : ")
    print();

#               Fonction pour générer clé public et clé privé           #
def gen_RSA():
    print("****      Generation cles gen_RSA         ****")
    tab = deuxNombrePrimeDis()
    p = tab[0]
    q = tab[1]
    #						Calcule de N				#
    n = p*q
    #						Calcule de N				#
    n = p*q
    #						Calcule de phi				#
    phi = (p-1)*(q-1)
    e = calculerE(phi)
    #						Calcule de d				#
    d = modinv(e,phi);
    print()
    afficher(p,q,n,e,phi,d);
    print()
    return(e,d,n)


#                         Chiffrement avec clé public           #
def chiffrer_cp():
    print()
    print("Entrer la clé public")
    e = int(input("Entrer la valeur de E : "))
    n = int(input("Entrer la valeur de N : "))
    m = int(input("Entrer la valeur a chiffrer : "))
    msg = pow(int(m),int(e),int(n))
    print("Message chiffrer : ",msg)


#                       Fonction pour Déchiffrer                #
def dechiffrer():
    print()
    print("****         Déchiffrement        ****")
    print()
    print("Entrer clé privé : ")
    d = int(input("Entrer D : "))
    n = int(input("Entrer N : "))
    msge = int(input("Entrer le msg a décrypter : "))
    #						Décryptage				#
    msg = pow(int(msge),int(d),n)
    print()
    print("Le message en clair : ",msg)
    print();



#                       Fonction pour déchiffrer avec factorisation#
def dechiffrer_cp():
    #tab = [9197, 6284, 12836, 8709, 4584, 10239, 11553, 4584, 7008, 12523, 9862, 356, 5356, 1159, 10280, 12523, 7506, 6311]
    #tab2 = [671828605, 407505023, 288441355, 679172842, 180261802]
    print()
    print("****         Déchiffrement avec clé public seulement        ****")
    print("Entrer la clé public : ")
    e=int(input("Entrer E : "))
    n=int(input("Entrer N : "))
    p,q = factoriser(n)
    print("p = ", p)
    print("q = ", q)
    phi = (p-1)*(q-1)
    d=modinv(e,phi)
    print("d = ",d)
    o = 'o'
    #  for msge in tab2:
    #     msg=pow(int(msge),int(d),n)
    #     print("Le message ",msge," en clair : ",msg);
    while o == 'o':
        msge = int(input("Entrer le message a décripter : "))
        msg=pow(int(msge),int(d),n)
        print("Le message en clair : ",msg);
        o = input("Voulez vous continuez ? (o/n) : ")


#                       Chiffrement text                        #
# NOTE: Le chiffrement se fait caractére par caractére avec des bloc de 8 en rajoutant des 0
def chiffrer_char():
    phrase = input("Entrer la phrase que vous voulez chiffrer : ")
    e,d,n=gen_RSA()
    asci = ""
    msge=0
    for c in phrase:
        msge = pow(ord(c),int(e),int(n));
        msge = str(msge)
        while len(msge) != 8:
            msge = '0'+msge
        capt += str(msge)

    if c == '':
        raise Exception("Erreur, chaine vide.")
    print(phrase+" en RSA donne : "+asci)

#                   Dechiffrement chaine                        #
# NOTE: Le déchiffrement se fait en dévisant le nombre par des blocs de 8
def dechiffrer_char():
    phrase = int(input("Entrer le message a déchiffre : "))
    print("**** Entrer la clé privé ****")
    d = int(input("Entrer D : "))
    n = int(input("Entrer N : "))
    msg = ''
    while phrase != 0 :
        msge = phrase % 100000000
        phrase = phrase // 100000000
        msge = pow(int(msge),d,n)
        msg = chr(msge) + msg
    print("Le message en clair : "+msg)


#                       Quitter                                 #
def quitter():
    sys.exit(0);


####### 					DEBUT MAIN			          #######

while 1:

    choix = int(menu())
    option={
        0 : gen_RSA,
        1 : chiffrer_cp,
        2 : dechiffrer,
        3 : dechiffrer_cp,
        4 : chiffrer_char,
        5 : dechiffrer_char,
        6 : quitter,
    }
    option[choix]();
