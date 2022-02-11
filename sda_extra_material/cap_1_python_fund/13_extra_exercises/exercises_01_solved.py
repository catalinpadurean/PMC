lista_1 = [4, 5, 6.7, 9.232, 457, 1, 20, 43, 3]
lista_2 = [1, 99, 43, 24, 17, 100]

#  Pornind de la listele declaraate mai sus, rezolvati urmatoarele cerinte.
# !!!!!!!!! Folositi printare formatata cu mesaj de fiecare data. !!!!!!!!!

print("="*120)
print("Solutie Ex.1", "\n")
# 1. Afisati lista_1 si lista_2 pe ecran asa cum sunt ele initial.
#    Afisati lista_1 pe ecran sortata crescator si lista_2 sortata descrescator
lista_1.sort()
lista_2.sort(reverse=True)
print(f"lista_1 sortata crescator: {lista_1}")
print(f"lista_2 sortata descrescator: {lista_2}")

print("="*120)
print("Solutie Ex.2", "\n")
# 2. Extindeti lista_1 cu elementele lista_2 dupa care adaugati lista_1 ca elemnent lista_2
#   Afisati pe ecran cele doua liste actualizate

lista_1.extend(lista_2)
lista_2.append(lista_1)
print(f"lista_1 extinsa: {lista_1}")
print(f"lista_2 actualizata: {lista_2}")

print("="*120)
print("Solutie Ex.3", "\n")
# 3. Eliminati din fiecare lista elementul cu indexul egal cu rezultatul impartirii lungimii listei la 2
print(f"Lungime lista_1 = {len(lista_1)}")
print(f"Lungime lista_2 = {len(lista_2)}")
print(f"Index element eliminat din lista_1: {int(len(lista_1) / 2)}. Valoarea elementului: {lista_1[int(len(lista_1) / 2)]}")
print(f"Index element eliminat din lista_2: {int(len(lista_2) / 2)}. Valoarea elementului: {lista_2[int(len(lista_2) / 2)]}\n")
lista_1.pop(int(len(lista_1) / 2))
lista_2.pop(int(len(lista_2) / 2))
print(f"lista_1 actualizata: {lista_1}")
print(f"lista_2 actualizata: {lista_2}")

print("="*120)
print("Solutie Ex.4", "\n")
# 4. Inserati in lista_1 valoarea lungimii lista_2 inmultita cu 1000, pe indexul 44.
#    Inserati in lista_2 valoarea lungimii lista_1 inmultita cu 500, pe indexul 90
#    Afisati cele doua liste actualizate pe ecran.


print(f"Lungime lista_2 = {len(lista_2)}. Elementul adaugat pe pozitia 44 va fi: {len(lista_2)*1000} ")
lista_1.insert(44, len(lista_2)*1000)
print(f"lista_1 actualizata: {lista_1}")

print(f"Lungime lista_1 = {len(lista_1)}. Elementul adaugat pe pozitia 90 va fi: {len(lista_1)*500} ")
lista_2.insert(90, len(lista_1)*500)
print(f"lista_2 actualizata: {lista_2}\n")
print("De indata ce am modificat lista 1 prin operatia de inmultire a lungimii lista_2 si adaugarea valoriila lista_1, \naceasta valoare a fost actualizata direct in lista_2 (valoarea 6000). \nAcest lucru se datoreaza faptului ca am folosit 'lista_1' ca element al listei 'lista_2' \nsi orice operatie asupra listei 'lista_1' se va reflecta in lista 'lista_2' ")
