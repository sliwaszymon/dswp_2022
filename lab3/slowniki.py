#Zad1
miesiace_pl = {
    1: "styczeń",
    2: "luty",
    3: "marzec",
    4: "kwiecień",
    5: "maj",
    6: "czerwiec",
    7: "lipiec",
    8: "sierpień",
    9: "wrzesień",
    10: "piździernik",
    11: "listopad",
    12: "grudzień"
}

#Zad2
miesiace_en = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

miesiace = {
    "pl": miesiace_pl,
    "en": miesiace_en
}

print(miesiace['pl'][4])

#Zad3
ciag = "Marianna"
slownik = dict.fromkeys(tuple(ciag), 1)
# for key in slownik.keys(): slownik[key] = ciag.count(key)
print(slownik)