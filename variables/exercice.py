# --- 1 ---
# Définition de variable
a = 1
# Affichage de variable
print(a)

# --- 2 ---
# Définition de variables
age = 35
first_name = "Kevin"
sentence = f'Je suis {first_name} et j\'ai {age} ans.'
# Affichage de variable
print(sentence)

# --- 3 ---
# Affichage de variables
print(age, first_name)

# --- 4 ---
# Multiplication du nombre contenu dans la variable age par 4
print(age * 4)

# --- 5 ---
# Incrémentation 1
add_1 = age + 1
print("age = ", age, ", et résultat = ", add_1, end=".")

# Incrémentation 2
add_2 = age
add_2 += 1
print("age = ", age, ", et résultat = ", add_2, end=".")

# --- 6 ---
# Décrémentation 1
minus_1 = age - 1
print("age = ", age, ", et résultat = ", minus_1, end=".")

# Décrémentation 2
minus_2 = age
minus_2 -= 1
print("age = ", age, ", et résultat = ", minus_2, end=".")

# --- 7 ---
# Multiplication 1
mult_1 = age * 2
print("age = ", age, ", et résultat = ", mult_1, end=".")

# Multiplication 2
mult_2 = age
mult_2 *= 2
print("age = ", age, ", et résultat = ", mult_2, end=".")

# --- 8 ---
# Division 1
div_1 = age / 2
print("age = ", age, ", et résultat = ", div_1, end=".")

# Division 2
div_2 = age
div_2 /= 2
print("age = ", age, ", et résultat = ", div_2, end=".")

# --- 9 ---
a = 1
b = 2
a, b = b, a

# --- 10 ---
# Méthode 1
a = 1
b = 1
c = 1

# Méthode 2
a = 1
b = a
c = a

# Méthode 3
a = b = c = 1

# --- 11 ---
a = 10
print(a)
print(a/2)
print(a//2)
print(a%2)
print(a**3)

# --- 12 ---


def nb_article():
    """This function return the user's input for the article's number.

    :return: number of articles.
    :rtype: str
    """
    nb_article = input("Nombre d'articles?")
    return nb_article


def HT_price():
    """This function return the user's input for the HT price.

    :return: HT price.
    :rtype: str
    """
    HT_price = input("Prix HT?")
    return HT_price


def inputs(HT_price, nb_article):
    """This function calculate the ATI_price.

    This function has no args. Therefore, it will take 2 numerical inputs with
    the input() function.

    :arg nb_article: Number of articles from the user's input.
    :type: str
    :arg HT_price: HT price of the article from the user's input.
    :type: str
    :return: All taxes include price.
    :rtype: float
    """
    # Definition of constants
    ERROR = "Erreur de saisie, merci de recommencer."
    TAXES = 0.2

    try:  # Check the value of HT_price
        HT_price = HT_price()
        HT_price = float(HT_price)
    except Exception as e:
        print(ERROR)
        HT_price()
    else:

        try:  # Check the value of nb_article
            nb_article = nb_article()
            nb_article = float(nb_article)
        except Exception as e:
            print(ERROR)
            nb_article()

        else:   # Calculate the All taxes include price
            ATI_price = ((HT_price * TAXES) + HT_price) * nb_article
            # Return the result
            return ATI_price


ATI_price = inputs(HT_price(), nb_article())
print(ATI_price)

# --- 13 ---
# Définition et affichage de la liste
my_list = [4, 5]
print(my_list)

# --- 14 ---
# Définition de la liste
my_list_2 = [4, 5, "Ma chaine de caractère", "Ma seconde chaine de caractère"]
print(my_list_2)
print(my_list_2[0])
print(my_list_2[2])

# --- 15 ---
# Définition des listes x et y
x = [1, 2]
y = [2, 3]

# Concaténation de x et y dans z
z = x + y
print(z)

# --- 16 ---
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(x[5])
print(x[3:5])
print(x[2:8:2])
print(len(x))
print(min(x))
print(max(x))
print(sum(x))
del x[3:5]
print(x)

# --- 17 ---
x = ["ok", 4, 2, 78, "bonjour"]
print(x[3])
x[1] = "toto"
print(x)

# --- 18 ---
# Méthode 1
x = [0, 1, 2, 3, 4, 5]
print(x)

# Méthode 2
x = [i for i in range(6)]
print(x)

# --- 19 ---
x = {"key": "valeur", "key2": "valeur2"}
print(x)
print(x['key'])
x['titi'] = 'toto'
x['titi'] = 'tata'
print(x)
# Les dictionnaires
# 19 - Créer un dictionnaire "x" avec les clés / valeurs suivantes :
# supprimer la valeur "key" et afficher la valeure correspondante qui à été supprimée
# afficher "x" créez un dictionnaire "y", lui affecter le dictionnaire "x" et afficher "y"
#
# Listes, dictionnaires et tuples
# 20 - Créez une liste "x" de 4 tuples de forme (x, y)
#
# afficher x
# ajouter la string "a" à la fin de la liste, afficher x
# ajouter la string "b" à la fin de la liste d'une manière différente, afficher x
# créer une liste "y" avec les valeurs "1", "2", "3". Ajouter tous les éléments de la liste y à la liste x. Afficher x
# Ajouter "2" à l'index n°4 de la liste x, sans supprimer l'index existant, ni le remplacer. Afficher x
# Supprimer la première valeur uniquement de x qui correspond à "2". afficher x
# Afficher y
# créez une liste "z" et lui affecter les meme valeurs qu'à y, afficher z
# supprimer tous les éléments dans y, afficher y
# supprimer tous les éléments dans z, d'une manière différente, puis afficher z