#Linkuri utile:
# 0 https://www.geeksforgeeks.org/destructors-in-python/ [Optional. Curiozitati]
# ╚ Despre destructor, opusul unui constructor. In python nu sunt la fel de folositi cum sunt in alte limbaje de programare dar o lectura mica nu strica.

# 1. https://realpython.com/python3-object-oriented-programming/ [Necesar. Aprofundare]
# ╚ Despre mostenirea claselor.

# 2 https://www.datacamp.com/community/tutorials/role-underscore-python [Optional. Curiozitati]
# ╚ Despre diferitele feluri in care se poate folosi caracterul: _(underscore)

# 3 https://www.geeksforgeeks.org/access-modifiers-in-python-public-private-and-protected/ [Necesar. Aprofundare]
# ╚ Despre public, private si protected (mangled).


class Animal:
    name = ""  # class variable
    age = 10    # class variable
    sex = "nedefinit" #class variable (class field)

    def __init__(self, nameAnim ="Jenna", ageAnim=2):  # special method used for instantiation - that is object creation
        self.name = nameAnim  # setting name when creating the object
        self.age = ageAnim    # setting age when creating the object

    def print_details(self):  # class method printing state of the instance
        print(f"Name: {self.name}, age: {self.age}, sex: {self.sex}")


my_dog = Animal() #Functia __init__ se apleaza la instantierea unui obiect
# print(type(my_dog))
# my_dog.print_details()  # call function on particular object (my_dog)
# print(my_dog.name)  # access particular object's field variable (my_dog)
# my_dog.age = 3  # change particular object's field value (my_dog)
# # print(my_dog.age)
# my_dog.name = "Alex"
# my_dog.print_details()  # call function on particular object (my_dog)
# my_cat = Animal()
# my_cat.print_details()
# my_mouse = Animal("Mouse_Name", 34.5) #Animal.__init__("Mouse_Name", 34)___
# my_mouse.print_details()
# my_mouse.age = 67
# my_mouse.print_details()
# my_mouse.sex = "F"
# my_mouse.print_details()
# my_cat.print_details()
#
# my_second_cat = Animal("Dina", 1)
# my_second_cat.print_details()
# if my_second_cat.age < 3:
#     my_second_cat.sex = "F"
# else:
#     my_second_cat.sex = "M"
# my_second_cat.print_details()
#
# my_third_cat = Animal("Lexi", "Zece")
# my_third_cat.print_details()



# my_puppy = Animal()  # create my_puppy instance of Animal
# my_older_dog = Animal()  # create my_older_dog instance of Animal
# my_puppy.print_details()
# my_puppy.age = 1
# my_puppy.name = "Rex Junior"
# my_puppy.print_details()
# my_older_dog.age = 10
# my_older_dog.name = "Rex Senior"
# my_older_dog.print_details()
# # prints out 'My puppy: Rex Junior, 1 and my older dog: Rex Senior, 10'
# print(f"My puppy: {my_puppy.name}, {my_puppy.age} and my older dog: {my_older_dog.name}, {my_older_dog.age}")

# print("="*100)
# print("Extra examples")
# print("="*100)
#
# print("Ex1")
# print("-"*100)


#Folosind OOP creati o clasa pentru a inregistra detalii despre un cantec si actualizati numarul de premii acordate acestuia

class Song:
    """Class used for creating an object Song and adding information about it"""

    #Definirea campurilor clasei
    song_name = ""
    number_of_lyrics = 0
    genre = ""
    author_name = ""
    release_year = 0
    number_of_awards = 2  # This field (variable) will not be initialised in __init__

    # __init__ function is called automatically every time an object is instantiated from a class.
    #  It is also known as a constructor

    def __init__(self, song_nm="Unkown song", no_lyrics=99, gen="Indie", athr_name="Unkown Artits", rls_year=2000): # Setting default values for parameteres sent to __init__ function
        # Initializing class variables with parameters received from __init__ function when creating an object
        #author_name, number_of_lyrics, genre, release_year, song_name sunt campurile clasei si vor fi accesate prin self
        #athr_name, no_lyrics, gen, rls_year, song_nm sunt parametrii functiei de initializare ce vor fi stocati(salvati) in campurile clasei
        #athr_name, no_lyrics, gen, rls_year, song_nm sunt parametri si ei vor putea fi utilizati doar in interiorul functiei care ii defineste

        #Daca un camp nu este suprascris in functia de __init__ atunci valoarea sa ramane valoarea primita la definirea campului
        self.author_name = athr_name
        self.number_of_lyrics = no_lyrics
        self.genre = gen
        self.release_year = rls_year
        self.song_name = song_nm

    def song_details(self):
        #author_name, number_of_lyrics, genre, release_year, song_name sunt campurile clasei si vor fi accesate prin self.
        #Ele pot fi accesate de catre orice functie din interiorul clasei
        print(f"{self.song_name} was created in {self.release_year}, by {self.author_name}. The song belongs to {self.genre} genre and has {self.number_of_lyrics} lyrics . It was one of the best songs in the artist's repertoire")

    def update_awards_number(self, no_awds):
        self.number_of_awards = no_awds
        self.number_of_lyrics = no_awds * 10

# print(f"Song class information: {Song.__doc__}")
# print("First song information:")
# first_song = Song(song_nm="The balad of Mona Lisa", no_lyrics=48, gen="Rock", athr_name="Panic! at the Disco", rls_year=2011)
# first_song.song_details()

# print(f"{first_song.song_name} received {first_song.number_of_awards} awards", "\n")
# first_song.update_awards_number(100)
# print(f"{first_song.song_name} received {first_song.number_of_awards} awards", "\n")
# first_song.number_of_awards = 50
# print(f"{first_song.song_name} received {first_song.number_of_awards} awards", "\n")
# first_song.number_of_lyrics = 2
# first_song.song_details()
# first_song.update_awards_number(100)
# print(first_song.number_of_lyrics)

# print("Second song information:")
# second_song = Song(song_nm="Nebun de alb", gen="Folk", athr_name="Emeric Imre")
# second_song.song_details()
# second_song.number_of_awards = 200
# print(f"{second_song.song_name} received {second_song.number_of_awards} awards")
# second_song.update_awards_number(40000)
# print(f"{second_song.song_name} received {second_song.number_of_awards} awards")
# print("Numar versuri: ",second_song.number_of_lyrics)
print("-"*100)

print("Ex2")
print("-"*100)

#Scrieti o clasa pentru a clasifica magazine si a oferi informatii despre program, produse etc


class Shop:
    #Declararea campurilor clasei
    opening_hours = 0
    closing_hours = 0
    shop_size = "Local store" # Other options are: SuperMarket, HyperMarket, ThriftShop
    sell_alcohol = True
    common_products = []

    #def __init__(self, open_hours = input("Introduceti ora la care se deschide magazinul:"), close_hours = input("Introduceti ora la care se inchide magazinul:"), sll_alcohol="False", comm_prod=["Vegetables","Fruits"]):
    def __init__(self, open_hours, close_hours, sll_alcohol="False", comm_prod=["Vegetables","Fruits"]):
        # open_hours = input("Introduceti ora la care se deschide magazinul:")
        # close_hours = input("Introduceti ora la care se inchide magazinul:")
        self.opening_hours = open_hours
        self.closing_hours = close_hours
        self.common_products = comm_prod


    def detalii_magazin(self):
        print(f"Shop schedule: {self.opening_hours} - {self.closing_hours}")
        print(f"Sells alcohol: {self.sell_alcohol}")
        print(f"Most common products: {self.common_products}")
        print(f"Most buyers suggest you should buy {self.common_products[0]}, because they are always fresh")



#my_shop = Shop() #-  se poate sterge daca doriti. Daca rulati codul cu ea, reproduceti eroarea parametrilor obligatorii

# ora_deschidere = input("Introduceti ora la care se deschide magazinul:")
# ora_inchidere = input("Introduceti ora la care se inchide magazinul:")
# # my_shop = Shop(ora_deschidere, ora_inchidere)
# # my_shop.detalii_magazin()
# lista_produse = []
# user_input_counter = 0
# while user_input_counter < 4:
#     produs = input("Introduceti unul dintre cele mai intalnite si disponibile produse din magazinul dvs:")
#     user_input_counter += 1
#     lista_produse.append(produs)

# my_shop = Shop(ora_deschidere, ora_inchidere)
# my_shop = Shop(ora_deschidere, ora_inchidere, comm_prod=lista_produse)
# my_shop.sell_alcohol = False
#De ce am specificat comm_prod = lista_produse dar ora deschidere si ora_inchidere au fostr trimise ca parametrii?
# my_shop.detalii_magazin()
# #
# print("-"*100)


