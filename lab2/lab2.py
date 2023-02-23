import requests
from bs4 import BeautifulSoup

URL = 'https://pl.lipsum.com/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

res = soup.find(id='Panes')
ress = res.find("div")
resss = ress.find("p")

zmienna = resss.get_text()

imie, nazwisko = "Szymon", "Śliwa"

litera_1 = nazwisko[3]
liczba_liter1 = zmienna.count(litera_1)

litera_2 = imie[2]
liczba_liter2 = zmienna.count(litera_2)

print(f'W tekście jest {liczba_liter1} liter {litera_1} oraz {liczba_liter2} liter {litera_2}')