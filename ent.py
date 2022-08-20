#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Fichier: ent.py
# Auteur: Marc COATANHAY

"""
    Module python pour effectuer des calculs entiers.

"""

# Import des modules
try:
    import mes_modules_path
except:
    pass

# Définitions constantes et variables globales
def pgcd(n1,n2):
    n1 = abs(n1)
    n2 = abs(n2)
    """Calcule le pdcd des entiers n1 et n2"""
    if(n1 < n2):
        return pgcd(n2,n1)
    elif(n2 == 0):
        return n1
    else:
        r = n1 % n2
        if(r == 0):
            return n2
        else:
            return pgcd(n2,r)


# Définitions fonctions et classes

print("* Module : entiers /ok")

