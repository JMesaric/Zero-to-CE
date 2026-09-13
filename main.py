import json

try:
    with open('zalihe.json') as f:
        zalihe = json.load(f)
except FileNotFoundError:
    print("Ta datoteka ne postoji")
except json.JSONDecodeError:
    print("JSON datoteka nije ispravno napisana")

def trebam_nar(proizvod):
    return (proizvod['minimum'] > proizvod['kolicina'])

def kol_nar(proizvod):
    return (proizvod['maksimum'] - proizvod['kolicina'])


def izvjestaj(zalihe):
    report = {}
    for i in zalihe:
        if trebam_nar(i):
            report[i['naziv']] = kol_nar(i)
    return report

izvjestaj(zalihe)

novi_proizvodi = {"naziv":"Coca Cola 2L", "kolicina":100, "minimum": 35, "maksimum": 100}
zalihe.append(novi_proizvodi)
narudzba = izvjestaj(zalihe)

with open("narudzba.json","w") as json_file:
    data1 = json.dump(narudzba, json_file)


