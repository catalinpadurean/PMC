"""Exercitiul 1:
Scrieti un program care sa satisfaca urmatoarele cerinte:
- folositi un tip de date (clasa) care sa poate stoca urmatoarele campuri:
        1. Nume (public)
        2. Prenume (public)
        3. Varsta  (mangled)
        4. Profesie (mangled)
        5. Vechime (public)
        6. Salariu (public)
- implementarea functiei __init__ ramane la alegerea voastra (sugestia mea e sa aveti macar 1-2 campuri obligatorii, si 1-2 optionale)
- creati proprietati (set, get, delete) pentru campurile mangled
- creati o functie care sa calculeze salariul bazat pe vechime (alegeti voi valoarea salariului) in functie de intervalurile
        A. 0-10 ani
        B. 11-20 ani
        C. 21-30 ani
        D. 31-40 ani
        E. Peste 40 ani

- creati o functie care sa afiseze toate campurile clasei

- instantiati clasa declarata de catre voi pentru urmatoarele 3 exemple:
    I) Persoana1:   Nume:Munteanu
                    Prenume: Vlad
                    Varsta: 35
                    Profesie: Doctor
                    Vechime: 24
                    Salariu: 100

    II) Persoana2:  Nume:Adam
                    Prenume:Andreea
                    Varsta: 20
                    Profesie: Avocat
                    Vechime: 39
                    Salariu: 10000

    III) Persoana3: Nume:Popescu
                    Prenume: Cristian
                    Varsta: 60
                    Profesie: Jurnalist
                    Vechime: 1
                    Salariu: 6788


- instantiati clasa declarata de catre voi pentru inca 3 exemple pe care sa le alegeti voi

- modificati campul vechime al obiectelor instantiate si afisati salariul inainte si  dupa modificare pentru a testa functia de calcul al salariului

- FOLOSITI PRINTARE FORMATATA PENTRU A URMARI MAI USOR CODUL!!!!!

                    """


class Persoana:
    """ 1. Nume (public)
        2. Prenume (public)
        3. Varsta  (mangled)
        4. Profesie (mangled)
        5. Vechime (public)
        6. Salariu (public)"""

    nume = ""
    prenume = ""
    __varsta = 0
    __profesie = ""
    vechime  = 1
    salariu = 20

    def __init__(self, numePers, varstaPers, profesiePers, vechimePers = 20):
        # - implementarea functiei __init__ ramane la alegerea voastra (sugestia mea e sa aveti macar 1-2 campuri obligatorii, si 1-2 optionale)
        self.nume = numePers
        self.__varsta =  varstaPers
        self.__profesie = profesiePers
        self.vechime = vechimePers

    #creati proprietati (set, get, delete) pentru campurile mangled

    """Proprietati pentru varsta"""

    @property #getter
    def varsta(self):
        return self.__varsta

    @varsta.setter #setter
    def varsta(self, varstaParametru):
        if varstaParametru < 18 and varstaParametru > 65:
            print("Persoana nu are varsta potrivita pentru acest program")
        else:
            self.__varsta = varstaParametru

    @varsta.deleter #setter
    def varsta(self):
        del self.__varsta

    """Proprietati pentru profesie"""

    @property #getter
    def profesie(self):
        return self.__profesie

    @profesie.setter
    def profesie(self, profesieParametru):
        self.__profesie = profesieParametru

    @profesie.deleter
    def profesie(self):
        del self.__profesie

    # Functie pentru calcul salariu
    def calcul_salariu(self):
        """
        - creati o functie care sa calculeze salariul bazat pe vechime (alegeti voi valoarea salariului) in functie de intervalurile
        A. 0-10 ani
        B. 11-20 ani
        C. 21-30 ani
        D. 31-40 ani
        E. Peste 40 ani
        """
        if self.vechime > 0 and self.vechime <= 10:      #A
            self.salariu = 900
        elif self.vechime > 10 and self.vechime <= 20:   #B
            self.salariu = 200
        elif self.vechime > 20 and self.vechime <= 30:   #C
            self.salariu = 983
        elif self.vechime > 30 and self.vechime <= 40:   #D
            self.salariu = 983
        else:
            self.salariu = 123

    def detalii_persoana(self):
        """ creati o functie care sa afiseze toate campurile clasei"""
        print(f"Detalii persoana: \n Nume: {self.nume}\n Prenume: {self.prenume}\n Varsta: {self.__varsta}\n Profesie: {self.__profesie}\n Vechime: {self.vechime}\n Salariu: {self.salariu}\n ")

""" instantiati clasa declarata de catre voi pentru urmatoarele 3 exemple:
    I) Persoana1:   Nume:Munteanu   
                    Prenume: Vlad
                    Varsta: 35
                    Profesie: Doctor
                    Vechime: 24
                    Salariu: 100

    II) Persoana2:  Nume:Adam
                    Prenume:Andreea
                    Varsta: 20
                    Profesie: Avocat
                    Vechime: 39
                    Salariu: 10000
    
    III) Persoana3: Nume:Popescu
                    Prenume: Cristian
                    Varsta: 60
                    Profesie: Jurnalist
                    Vechime: 1
                    Salariu: 6788"""

print("=" * 100)
print("PERSOANA 1")
print("prima incercare")
pers1 = Persoana("Munteanu", 35, "Doctor", 24)
pers1.detalii_persoana()  # In acest caz se observa ca nu toate campurile au valoarea ceruta la punctul I
                          #Pentru a completa campurile pers1 astfel incat sa indeplinim cerinta, vom accesa campurile direct (acest lucru poate fi rezolvat mai elegant din functia __init__)
print("A doua incercare")
pers1.prenume = "Vlad"
pers1.salariu = 100
pers1.detalii_persoana() #La al doilea apel al functiei detalii_persoana, se observa ca avem exact campurile cerute mai sus
print("=" * 100)
print("PERSOANA 2")
pers2 = Persoana("Adam", 20, "Avocat", 39)
pers2.prenume = "Andreea"
pers2.salariu = 10000
pers2.detalii_persoana()
print("=" * 100)
print("PERSOANA 3")
pers3 = Persoana("Popescu", 60, "Jurnalist", 1)
pers3.prenume = "Cristian"
pers3.salariu = 6788
pers3.detalii_persoana()
print("=" * 100)
print("Modificare varsta si profesie PERSOANA 1")
pers1.varsta = 50
pers1.profesie = "Comentator"
print("Detalii PERSOANA 1 modificate")
pers1.detalii_persoana()
print("=" * 100)
print("Modificare vechime PERSOANA 1, urmarim ca schimbare si salariul")
pers1.vechime = 40
print("Am modificat doar vechimea, dar nu am apelat functia de calcul a salariului, astfel, salariul nu a fost actualizat!!!!!!!!!!")
pers1.detalii_persoana()
pers1.calcul_salariu() #Daca nu apelam functia calcul salariu, salariul nu se va modifica in functie de varsta
print("Functia de calcul a salariului a fost apelata!!!!!!")
pers1.detalii_persoana()
print("=" * 100)

print("In rezolvarea acestui exemplu nu am mai adaugat 3 persoane la alegere proprie,\n"
      "consider ca acest subpunct este usor de rezolvat dupa implementarea clasei si a metodelor sale specifice")