"""Exercitiul 1: Cereti utilizatorului sa introduca de la tastatura 7 cuvinte cu lungimea de minim 12 litere si salvati-le intr-o lista input_strings
 - creati o lista input_lengths care sa contina lungimile cuvintelor din input_string
 - afisati pe ecran cel mai lung cuvant din lista input_strings
 - afisati pe ecran cel mai scurt cuvant din lista input strings
 - afisati pe ecran doar elementele listei input_lengths(daca exista) care satisfac urmatoarele cerinte:
        A. Sunt divizibile cu 2
        B. Sunt mai mici decat 100
        C. Patratul lor este mai mic decat 400"""

input_strings = [] #variabila globala(in afara functiei. va fi recunoscuta in tot programul)
input_lengths = [] #variabila globala(in afara functiei. va fi recunoscuta in tot programul)

def input_utilizator():
    """Functie care:
     -nu primeste parametru
     -asteapta pana sunt introduse exact 7 cuvinte corecte (while)
     -verifica daca un cuvant este corect (if)
     -returneaza o lista
    """
    contor_cuvinte = 0 #variabila locala(in interiorul functiei. va fi recunoscuta doar in interiorul functiei)
    user_inp_strings = [] #variabila locala(in interiorul functiei. va fi recunoscuta doar in interiorul functiei)
    while contor_cuvinte < 2:
        user_inp = input(f"Introduceti un cuvant de minim 12 litere. Ati introdus {contor_cuvinte} cuvinte corecte: ")
        if len(user_inp) > 11:
            user_inp_strings.append(user_inp)
            contor_cuvinte += 1
        else:
            continue
    return user_inp_strings
print("="*100)
print("Lista input_strings: \n")
input_strings = input_utilizator() #retinem in input_strings lista returnata de functie
print(input_strings) # verificam lista

def lungime_input_utilizator(lista_input):
    """Functie care:
     -primeste parametru o lista
     -returneaza o alta lista ce contine lungimile elementelor listei primite ca parametru
    """
    user_inp_lengths = []
    for element in lista_input:
        user_inp_lengths.append(len(element))
    return user_inp_lengths
print("="*100)
input_lengths = lungime_input_utilizator(input_strings)
print("Lista input_lengths: \n")
print(input_lengths) # verificam lista

def string_maxim(lista_input):
    """Functie care:
     -primeste parametru o lista
     -returneaza cel mai lung element din lista
    """
    if len(lista_input) > 0:
        element_maxim = lista_input[0] #Presupunem ca elementul maxim este primul element
        print(f"element_lista(adica indexul din lista)= {0}")
        print(f"lista_input[element_lista](adica elementul din lista): {lista_input[0]}")
        for element_lista in range(1, len(lista_input)): #parcurgem lista de la al doilea element pana la capat. element_lista este index in acest caz
            print(f"element_lista(adica indexul din lista)= {element_lista}")
            print(f"lista_input[element_lista](adica elementul din lista): {lista_input[element_lista]}")
            if len(lista_input[element_lista]) > len(element_maxim): #Daca gasim un element din lista mai mare decat actualul maxim,
                element_maxim = lista_input[element_lista] #atunci maximul devine acel element
        return element_maxim #Dupa ce epuizam "for"-ul, returnam elementul maxim
    else:
        print("Lista este goala")


print("=" * 100)
cel_mai_lung_string = string_maxim(input_strings)  # Salvam intr-o variabila cel mai lung string
print("Cel mai lung cuvant: \n")
print(cel_mai_lung_string)  # Afisam pe ecran cel mai lung string


def string_minim(lista_input):
    """Functie care:
     -primeste parametru o lista
     -returneaza cel mai scurt element din lista
    """
    if len(lista_input) > 0:
        element_minimm = lista_input[0] #Presupunem ca elementul minim este primul element
        print(f"element_lista(adica indexul din lista)= {0}")
        print(f"lista_input[element_lista](adica elementul din lista): {lista_input[0]}")
        for element_lista in range(1, len(lista_input)): #parcurgem lista de la al doilea element pana la capat. element_lista este index in acest caz
            print(f"element_lista(adica indexul din lista)= {element_lista}")
            print(f"lista_input[element_lista](adica elementul din lista): {lista_input[element_lista]}")
            if len(lista_input[element_lista]) < len(element_minimm): #Daca gasim un element din lista mai mic decat actualul maxim,
                element_minimm = lista_input[element_lista] #atunci minim devine acel element
        return element_minimm #Dupa ce epuizam "for"-ul, returnam elementul minim
    else:
        print("Lista este goala")
print("="*100)
cel_mai_scurt_string = string_minim(input_strings) #Salvam intr-o variabila cel mai scurt string
print("Cel mai scurt cuvant: \n")
print(cel_mai_scurt_string) #Afisam pe ecran cel mai scurt string


def verifica_lungimi(integer_input):
    """ functie care:
        primeste un parametru, intreg
        - verifica daca este par
        - verifica daca este mai mic decat 100
       - verifica daca patratul este mai mic decat 400"""
    if ((integer_input % 2 == 0) and (integer_input < 100) and (integer_input ** 2 < 400)):
        return integer_input
    else:
        """In mod normal pe aceasta ramura, trebuia sa nu executam nimic dar am pus acest return sau print pentru aurmari mai usor codul
        Daca vreti ca aceasta ramura sa nu execute nimic lasati doar instructiunea"pass"""
        # return(f"Elementul {integer_input} nu satisface toate cele 3 conditii necesare")
        # print (f"Elementul {integer_input} nu satisface toate cele 3 conditii necesare")
        pass

print("="*100)
print("Verificare elemente input_lengths")

for lungime in input_lengths:
    if type(verifica_lungimi(lungime)) != type(None):
        print(verifica_lungimi(lungime))
    else:
        print("Functia returneaza None daca instructiunea pass este decomentata. "
              "Iar noi vrem sa afisam pe ecran doar elemente care satisfac conditiile impuse "
              "Puteti sterge acest print dupa ce ati inteles cum functioneaza acest program.")