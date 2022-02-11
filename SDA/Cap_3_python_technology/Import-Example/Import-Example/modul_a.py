test = "Nice sentence."

def find_index(collection, element):
    for index, value in enumerate(collection):
        if value == element:
            return index
    return -1


def calculeaza_aria_triunghiului(inaltime, latura):
    return inaltime * latura/2
