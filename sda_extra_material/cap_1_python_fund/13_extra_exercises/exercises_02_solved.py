import math
input_strings = ["Windows Defender might be impacting your build performance.", "Comanda din 16.02.2021 a fost împachetată și expediată din depozitul nostru", "Februarie pare că se mută de la un an la altul de partea mai luminoasă a calendarului.",
                 " Cum am stat cu muzica în 2020? ", "Pentru mai multe detalii și opțiuni suplimentare, accesați următorul link!", "test_2002", "Habar nu am ce stringuri sa mai pun aici", "sper ca sunt suficiente", "asta e ultimul", "punct!."]
output_strings = []

print("="*100)
print("Exercitiul.1")

def modifica_string (param_str):
    # Scrieti codul functiei care verifica lungimea fiecarui string din input_strings si il modifica:
    # -daca lungimea stringului e numar par, face tot stringul cu litere mici
    # -daca lungimea stringului e numar impar, face tot stringul cu litere mari
    if len(param_str) % 2 == 0:
        return param_str.lower()
    else:
        return param_str.upper()


for inp_str in range(0, len(input_strings)):
    out_str = modifica_string(input_strings[inp_str])
    output_strings.append(out_str)

for item in output_strings:
    print(item)

print("=" * 100)
print("Exercitiul.2")

input_list_nr = [243, 4004, 3500, 2002, 450054, 101, 3333, 200, 49894, 20200202, 1234321, 111223, 0, 1, 7]
input_list_str = ["aba", "poodoop", "abcad", "Sosos", "text_0", "lateral", "absent", "stop", "tras", "rest", "castravete", "kokok", "armamra"]
output_list_nr = []
output_list_str = []


def palindrom_str(param_str):
    #Scrieti codul pentru o functie care returneaza:
    # True daca stringul este palindrom
    # False daca stringul nu este palindrom
    if param_str == param_str[::-1]:
        return True
    else:
        return False


def palindrom_nr(param_nr):
    # Scrieti codul pentru o functie care returneaza:
    # True daca numarul intreg este palindrom
    # False daca numarul intreg nu este palindrom
    # Incercati sa faceti verificarea fara a converti numarul intreg in string.
    # Daca numerele formate dintr-o cifra sunt considerate palindrom, ramane la alegerea voastra
    var_temp = param_nr
    palindrom = 0
    while(var_temp != 0): # var_temp = 243 | var_temp =  24 | var_temp = 2
        # print(f"var_temp: {var_temp}")
        palindrom = (palindrom * 10) + (var_temp % 10)  # 0 *10 + 3 | 3*10 +4 | 34 * 10 + 2
        # print(f"palindrom: {palindrom}")
        var_temp = var_temp // 10
        # print(f"var_temp: {var_temp}")
    if palindrom == param_nr:
        return True
    else:
        return False


for item in range(0, len(input_list_nr)):
    if palindrom_nr(input_list_nr[item]):
        output_list_nr.append(input_list_nr[item])
print(output_list_nr)


for item in range(0, len(input_list_str)):
    if palindrom_str(input_list_str[item]):
        output_list_str.append(input_list_str[item])
print(output_list_str)

print("=" * 100)
print("Exercitiul.3")

def citeste_numere_returneaza_radical():
    lista_radicali = []
    contor_numere = 0
    while contor_numere < 10 :
        print(f"Ati introdus {contor_numere} numere, mai aveti de introdus {10-contor_numere}")
        numar_citit = int(input("Introduceti un numar pozitiv mai mic decat 400: "))
        if 0 < numar_citit < 401:
            lista_radicali.append(math.sqrt(numar_citit))
            contor_numere += 1
        else:
            continue
    return lista_radicali



print(citeste_numere_returneaza_radical())
