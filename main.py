KosztTowaruNr10 = 2.50


print("Wpisz numer towaru: ")
NrTowaru = input()
NrTowaru = int(NrTowaru)
print(type(NrTowaru))

while NrTowaru != 10:
    print("Nie ma takiego numeru. Wybierz jeszcze raz")
    NrTowaru = input()
    NrTowaru = int(NrTowaru)


print("Wybrales nr", NrTowaru, "koszt to", KosztTowaruNr10)
