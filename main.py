import json
from funkcije import trebam_nar, kol_nar, izvjestaj, dodaj_proizvod, azuriraj_kolicinu

try:
    with open('zalihe.json') as f:
        zalihe = json.load(f)
except FileNotFoundError:
    print("Ta datoteka ne postoji")
except json.JSONDecodeError:
    print("JSON datoteka nije ispravno napisana")

print(trebam_nar(zalihe[3]))

print(kol_nar(zalihe[1]))

azuriraj_kolicinu(zalihe, "Fanta 2L", 5)

print(izvjestaj(zalihe))


