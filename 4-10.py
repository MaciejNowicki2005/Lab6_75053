#4A
from random import randint

losowa = randint(1,10)
print("Szczęśliwy numerek na sobotę to....",losowa)

#4B
roczniki = [1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007]

print("Szczęśliwy rok z grupy:",randint(min(roczniki),max(roczniki)))


#5
import random
numerki = []
for i in range(49):numerki.append(i+1)

print("Rozpoczynamy losowanie, szczęśliwe liczby to:")
wynikLosowania = random.sample(numerki,k=6)
print(wynikLosowania)
print("W razie przegranej życzę powodzenia następnym razem...")

#6
import time

ileSekund = int(input("Podaj ile sekund chcesz obliczyć"))

for i in range(ileSekund,-1,-1):
    print(i)
    time.sleep(1)

#7
from datetime import date
import locale

locale.setlocale(locale.LC_TIME, "Polish")

dzisiaj = date.today()
laboratoria = date(2026, 11, 23)
kolokwium = date(2026, 12, 21)

odLaboratorium = (dzisiaj - laboratoria).days
doKolokwium = (kolokwium - dzisiaj).days

print("Dzisiejsza data:", dzisiaj.strftime("%d %B %Y"))
print("Od ostatnich laboratoriów minęło:", odLaboratorium, "dni")
print("Do kolokwium zostało:", doKolokwium, "dni")


#8
import keyword

print("Keyword for:",keyword.iskeyword("for"))
print("Keyword print:",keyword.iskeyword("print"))
print("Keyword break:",keyword.iskeyword("break"))
print("Keyword done:",keyword.iskeyword("done"))
print("Keyword bad:",keyword.iskeyword("bad"))

#9
import math
import keyword
print("Funkcje w math:",dir(math))
print("Funkcje w tuble:",dir(tuple))
print("Funkcje w keyword:",dir(keyword))

#10
import random
import math

pocz = int(input("Podaj początek przedziału: "))
kon = int(input("Podaj koniec przedziału: "))

krotka = tuple(random.randint(pocz, kon) for i in range(10))

srednia =  (math.prod(krotka))**(1/len(krotka))

print("Wylosowana krotka:", krotka)
print("Średnia geometryczna:", round(srednia, 2))