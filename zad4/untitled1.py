#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 17:35:53 2023

@author: adrianc
"""

import random

# Generuj 500 liczb całkowitych z zakresu od 1 do 100 (możesz dostosować zakres według potrzeb)
liczby_calkowite = [random.randint(1, 100000) for _ in range(500)]

# Nazwa pliku do zapisu
nazwa_pliku = 'liczby.txt'

# Zapisz wygenerowane liczby do pliku
with open(nazwa_pliku, 'w') as plik:
    for liczba in liczby_calkowite:
        plik.write(str(liczba) + '\n')

print(f'Wygenerowane liczby zostały zapisane do pliku {nazwa_pliku}.')
