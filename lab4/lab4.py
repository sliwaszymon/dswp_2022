import sys

#Zad1
def foo1():
    zdanie = input("Podaj zdanie: ")
    spacje = zdanie.count(" ")
    print(f'W tym zdaniu występuje {spacje} spacji.')
    # return spacje

# foo1()

#Zad2
def foo2():
    print("Podaj pierwszą wartość: ")
    x = int(sys.stdin.readline())
    print("Podaj drugą wartość: ")
    y = int(sys.stdin.readline())
    sys.stdout.write(str(x*y))
    # return x*y

# foo2()

#Zad3
def foo3():
    a = int(input("Podaj a: "))
    b = int(input("Podaj b: "))
    c = int(input("Podaj c: "))

    if (a > 0) and (a <= 10):
        print("a jest w przedziale (0, 10>") 
        # return True
    elif (a > b) or (b > c):
        print("a>b lub b>c")
        # return True
    else:
        print("Warunek zadania nie jest spełniony")
        # return False

# foo3()

#Zad4
# for x in range(5, 51, 5): print(x)
for x in [x for x in range(0,51) if x%5==0 and x!=0]: print(x)

#Zad5
def foo5():
    liczby = input("Podaj liczby po spacj: ")
    liczby = map(lambda x: int(x)**2, liczby.split())
    print(list(liczby))
    # return(list(liczby))

# foo5()

#Zad6
def foo6():
    lista = []
    stop = False
    while not stop:
        _in = input("Podaj liczbę (lub 'stop' jeśli chcesz zakończyć dodawanie liczb do listy): ")
        if _in == 'stop':
            stop = not stop
        else:
            lista.append(int(_in))
    print(lista)
    # return(lista)

# foo6()

#Zad7 - nie wiem po co tu while xD ale niech będzie
def foo7():
    val = input("Podaj liczbę składającą się z wielu cyfr: ")
    lista = list(val)
    wynik = 0
    while len(lista) > 0:
        wynik += int(lista.pop(0))
    print(wynik)
    # return(wynik)

# foo7()

#Zad8
def foo8():
    val = int(input("Podaj wysokość wieży (nie większa niż 10): "))
    if val < 10: 
        for x in range(1,val+1):
            print("A"*x)
    else:
        print("Mordzia zbastuj bajerke, miało być nie większa niż 10")

# foo8()

#Zad9
def foo9():
    for x in range(1, 101):
        for y in range(1, 101):
            multiply = x*y
            print(f'{x} * {y} = {multiply}')

# foo9()

#Zad10
def foo10():
    h = int(input("Podaj wysokość: "))
    if h >= 3 and h <= 9:
        if h%2==0:
            print("Nie chce mi się wyjątków obsługiwać, więc będzie o wiersz większa haha :P")
        for x in range(h//2 + 1):
            print(" " * (h - x), "o" * (2*x + 1))
        for x in range(h//2-1, -1, -1):
            print(" " * (h - x), "o" * (2*x + 1))
    else:
        print("No coś średnio ta liczba pasuje w przedział <3, 9> mordzia.")
foo10()