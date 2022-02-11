input_strings = ["Windows Defender might be impacting your build performance.",
                 "Comanda din 16.02.2021 a fost împachetată și expediată din depozitul nostru",
                 "Februarie pare că se mută de la un an la altul de partea mai luminoasă a calendarului.",
                 " Cum am stat cu muzica în 2020? ",
                 "Pentru mai multe detalii și opțiuni suplimentare, accesați următorul link!", "test_2002",
                 "Habar nu am ce stringuri sa mai pun aici", "sper ca sunt suficiente", "asta e ultimul", "punct!."]
output_strings = []

print("="*100)
print("""Exercitiul 1:
Scrieti un program care parcurge o lista de stringuri data, si returneaza o noua lista 
cu stringurile modificate conform cerintei aflate in comentariu""")
print("="*100)
def modifica_string(param_str):
# Scrieti codul functiei care verifica lungimea fiecarui string din input_strings si il modifica:
# -daca lungimea stringului e numar par, face tot stringul cu litere mici
# -daca lungimea stringului e numar impar, face tot stringul cu litere mari
    return 0 #Stergeti aceasta linie dupa implementare

# Aplicati functia definita mai sus pentru fiecare element al listei "input_strings" si retineti rezultatul in lista"output_strings"
# Afisati pe ecran lista output_strings, fiecare element pe o linie separata

print("""Exercitiul 2:
Scrieti un program care parcurge doua liste date: o lista cu stringuri si o lista cu numere intregi
si afiseaza pe ecran doua liste doar cu palindromurile aflate in cele doua liste. Cititi comentariile pentru detalii""")
print("="*100)

input_list_nr = [100, 4004, 3500, 2002, 450054, 101, 3333, 200, 49894, 20200202, 1234321, 111223, 0, 1, 7]
input_list_str = ["aba", "poodoop", "abcad", "Sosos", "text_0", "lateral", "absent", "stop", "tras", "rest",
                  "castravete", "kokok", "armamra"]
output_list_nr = []
output_list_str = []


def palindrom_str(param_str):
    #Scrieti codul pentru o functie care returneaza:
    # True daca stringul este palindrom
    # False daca stringul nu este palindrom
    return 0 #Stergeti aceasta linie dupa implementare


def palindrom_nr(param_nr):
    # Scrieti codul pentru o functie care returneaza:
    # True daca numarul intreg este palindrom
    # False daca numarul intreg nu este palindrom
    # Incercati sa faceti verificarea fara a converti numarul intreg in string.
    # Daca numerele formate dintr-o cifra sunt considerate palindrom, ramane la alegerea voastra
    return 0  # Stergeti aceasta linie dupa implementare



print("""Exercitiul 3:""")
print("="*100)
print("""Scrieti o functie care cere utilizatorului sa introduca de la tastatura numere.
        Functia va cere utilizatorului sa introduca cate un numar, pe rand, pana sunt introduse exact 10 numere.
        Daca numarul este mai mic decat 0 si mai mare decat 400, numarul va fi ignorat. 
        Daca numarul se afla in intervalul (0-400] atunci functia ii va calcula radacina patrata si o va salva intr-o lista
        In momentul in care in utilizatorul a introdus 10 numere corespunzatoare criteriilor, functia isi va incheia executia si va returna lista cu radicali.
        Afisati pe ecran lista finala.
        Datele de intrare sunt la alegerea voastra.""")
def citeste_numere_returneaza_radical():
    #Scrieti codul pentru functia care returneaza o lista cu radicali
    #Valoarea va fi adaugata in lista doar daca numarul este strict mai mare decat 0 si mai mic sau egal decat 400
    #Functia va cere utilizatorului sa introduca date pana la epuizarea conditiei: numarul de numere valide introduse = 10
    return 0 #Stergeti aceasta linie dupa implementare

