versuri = "roses-are-red*dogs-see-them-as-grey*python-can-be-easy*if-you-PrActicE-every-Day."
# Pornind de la textul dat, stocat in variabila "versuri", rezolvati urmatoarele cerinte:

print("="*120)
print("Solutie Ex.1", "\n")
# 1. Impartiti textul initial dupa caracterul "*" si salvati noul text intr-o variabila noua
# (Ex: versuri_split. Puteti alege orice nume vreti, eu am sa ma refer la ea in continuare cu "versuri_split)
#
# Afisati pe ecran:
#     - textul initial
#     - textul fara "*"
#     - tipul celor doua variabile
versuri_split = versuri.split("*")
print(f"Textul initial: {versuri}")
print(f"Textul modificat (fara *): {versuri_split}")
print(f"Tipul variabile versuri : {type(versuri)}")
print(f"Tipul variabile versuri_split : {type(versuri_split)}")

print("="*120)
print("Solutie Ex.2", "\n")

# 2. Folosind noua variabila create de voi( folosind indexarea!!) afisati pe ecran urmatoarele:
#     - primul vers al textului si doar primul cuvant este scris cu litera mare => Roses-are-red
#     - al doilea vers al textului si toate literele sunt majuscule
#     - al treilea vers al textului si fiecare cuvant incepe cu litera mare => Python-Can-Be-Easy
#     - al patrulea vers al textului unde toate literele sunt litere mici
#    Adaugati un nou vers in "versuri_split" (al 5-lea vers) care sa aiba acelasi format (cu - intre cuvinte)
#    Ex: "my-own-verse"
#   Afisati pe ecran(folosind indexarea pe versuri_split) versul adaugat de voi dar din care sa scoatei caracterul "-"
#   Pe ecran ar trebui sa apara "my own verse"

print(f"Primul vers al textului cu primul cuvant scris cu litera mare: {versuri_split[0].capitalize()}")
print(f"Al doilea vers al textului si toate literele sunt majuscule: {versuri_split[1].upper()}")
print(f"Al treilea vers al textului si fiecare cuvant incepe cu litera mare: {versuri_split[2].title()}")
print(f"Al patrulea vers al textului si toate literele sunt litere mici: {versuri_split[3].lower()}")
new_verse = "Don't-trust-my-word-and-do-as-you-may"
versuri_split.append(new_verse)
print(f"Versul adaugat este: {versuri_split[len(versuri_split)-1].replace('-', ' ')}")

print("="*120)
print("Solutie Ex.3", "\n")

# 3. Creati o lista goala versuri_inversate= [].
# Adaugati pe rand, inversul versurile salvate in variabila variable_split.
# Afisati pe rand fiecare vers din noua variabila (folosind index) dar de data aceasta printati folosind formated-string
# Ex: "Primul vers inversat este: der-era-sesor

versuri_inversate = []
list_index = 0
versuri_inversate.append(versuri_split[list_index][::-1])
print(f" Primul vers inversat este: {versuri_inversate[list_index]} ")
list_index += 1
versuri_inversate.append(versuri_split[list_index][::-1])
print(f" Al doilea vers inversat este: {versuri_inversate[list_index]} ")
list_index += 1
versuri_inversate.append(versuri_split[list_index][::-1])
print(f" Al treilea vers inversat este: {versuri_inversate[list_index]} ")
list_index += 1
versuri_inversate.append(versuri_split[list_index][::-1])
print(f" Al patrulea vers inversat este: {versuri_inversate[list_index]} ")
list_index += 1
versuri_inversate.append(versuri_split[list_index][::-1])
print(f" Al cincilea vers inversat este: {versuri_inversate[list_index]} ")

print("="*120)
print("Solutie Ex.4", "\n")

# 4. Creati doua dictionare goale: "versuri_impare" si "versuri_pare"
#    Adaugati in versuri_impare:
#    3 perechi formate din:   - cheile: v1, v3, v5
#                             - valorile: versul1, versul3, versul5
#    Adaugati in versuri_impare:
#    2 perechi formate din:   - cheile: v2, v4
#                             - valorile: versul2, versul4
#   Afisati pe ecran cele doua dictionare
#   Actualizati primul dictionar cu valorile din al doilea dictionar
#   Eliminati perechea v3:vers3 din dictionarul actualizat

versuri_impare = {}
versuri_pare = {}

versuri_impare["v1"] = versuri_split[0]
versuri_impare["v3"] = versuri_split[2]
versuri_impare["v5"] = versuri_split[4]
print(f"Dictionarul versuri_impare este: {versuri_impare}")
versuri_pare["v2"] = versuri_split[1]
versuri_pare["v4"] = versuri_split[3]
print(f"Dictionarul versuri_pare este: {versuri_pare}")
versuri_impare.update(versuri_pare)
print(f"Dictionarul versuri_impare actualizat cu valorile din versuri_pare:\n{versuri_impare}")
versuri_impare.pop("v3")
print(f"Dictionarul versuri_impare actualizat dupa eliminarea perechii cu cheia v3:\n{versuri_impare}")

print("="*120)

