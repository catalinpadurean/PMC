# Importam modul_a integral:
# import modul_a
# Importam doar acele functii care ne intereseaza din modul_a:
# from modul_a import test, find_index, calculeaza_aria_triunghiului

# calc_aria_tri(10, 2)
#
# print(modul_a.test)
# courses = ["PE", "History", "Math"]
# index = modul_a.find_index(courses, "PE")
# print(index)  # Prints 0
# ---------------------------------------------------------------------------------------------------

# Importam variabila test din modul_a, care este situat in directorul Techonology:
# from Technology.modul_a import test
# print(test)

# ---------------------------------------------------------------------------------------------------
# Importam tot continutul modulului modul_a, care este situat in directorul Techonology:
# from Technology.modul_a import *
# print(test)

# ---------------------------------------------------------------------------------------------------
# Putem folosi aliasuri (folosind keyword-ul "as") pentru a redenumi variabilele/functiile pe care le importam
# from modul_a import test as var_1, find_index as function_1, calculeaza_aria_triunghiului as calc_aria_tri
#
# courses = ["PE", "History", "Math"]
# index = find_index(courses, "PE")
# print(index)  # Prints 0
# ---------------------------------------------------------------------------------------------------


# Orinea in care facem importurile:
#
# Librarii standard:
# import os
# Librarii externe:
# import django
# Module locale (codul scris de noi in proiect)
# from modul_a import *
#
# ---------------------------------------------------------------------------------------------------
# Importam o librarie(biblioteca) standard - in intregime
# import os
#
# Returneaza calea catre directorul curent
# directorul_curent = os.getcwd() # get current working directory
#
# print(f'Ne aflam in directorul: {directorul_curent}')

# ---------------------------------------------------------------------------------------------------
# Importam o librarie(biblioteca) standard - in intregime
# import sys
#
# print(sys.path)
# ---------------------------------------------------------------------------------------------------
# Importam o librarie(biblioteca) standard - in intregime
# import random
#
# print(random.__file__)
# ---------------------------------------------------------------------------------------------------
# Importam toate modulele din directorul Technology (in intregime)
# from Technology import *
# Importam modul_a si modul_b din directorul Technology (in intregime)
# from Technology import modul_a, modul_b