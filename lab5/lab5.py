import random

#Zad1
A = [1/x for x in range(1,11)]
B = [2**x for x in range(11)] #range <1 10> tak dla czytelności
C = [x for x in B if x%4==0]

#Zad2
macierz = [[random.randint(0, 255) for y in range(4)] for x in range(4)]
print(macierz)
przekatna = [macierz[x][x] for x in range(4)]
print(przekatna)

#Zad3
slownik = {
    "mleko": "litry",
    "cukier": "kilogramy",
    "chleb": "sztuki",
    "woda": "litry",
    "cukierki": "kilogramy",
    "energole": "sztuki"
}

sl = {x:y for x,y in slownik.items() if y=="sztuki"}
print(sl)

#Zad4
def pyta():
    imie = input("Podaj imie: ")
    print(f'Witaj {imie}')

#Zad5
def foo5(val = 4):
    for x in range(val):
        print(str(val)*val)

# foo5(3)

#Zad6
def ciag(* liczby):
    if len(liczby) == 0:
        return 0.0
    else:
        iloczyn = 1.0
    for i in liczby:
        iloczyn *= i
    return iloczyn

# print(ciag(1,2,3,4,5)) #5!=120

#Zad7
def ile_zakupow(**lista_zakupow):
    ilosc = 0
    for produkt in lista_zakupow: ilosc += lista_zakupow[produkt]
    return ilosc

print(ile_zakupow(mleko= 2, cukier= 1, chleb= 1, woda= 2, energole= 10))