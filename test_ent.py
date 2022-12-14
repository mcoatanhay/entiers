#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Fichier: test_entiers.py
# Auteur: Marc COATANHAY

"""
    Test pour le module entiers
"""

# Import des modules
import ent
import unittest

class EntiersTest(unittest.TestCase):
    def test_pgcd(self):
        self.assertEqual(ent.pgcd(1,1), 1)
        self.assertEqual(ent.pgcd(2,4), 2)
        self.assertEqual(ent.pgcd(4,2), 2)
        self.assertEqual(ent.pgcd(2*3*5*7*11*13,2*3*5), 2*3*5)
        self.assertEqual(ent.pgcd(2*3*5*7*11*13,7*11*13), 7*11*13)
        self.assertEqual(ent.pgcd(2*3*5,2*3*5*7*11*13), 2*3*5)
        self.assertEqual(ent.pgcd(7*11*13,2*3*5*7*11*13), 7*11*13)

if (__name__ == "__main__"):
    unittest.main()