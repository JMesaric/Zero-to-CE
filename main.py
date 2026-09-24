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

def dodaj_proizvod(zalihe, naziv, kolicina, minimum, maksimum):
    d =  {}
    d["naziv"] = naziv
    d["kolicina"] = kolicina
    d["minimum"] = minimum
    d["maksimum"] = maksimum
    zalihe.append(d)
    with open("zalihe.json", "w") as json_file:
        zz = json.dump(zalihe, json_file, indent=2)

def azuriraj_kolicinu(zalihe, naziv, kolicina):
    for i in zalihe:
        if (i["naziv"] == naziv):
            i["kolicina"] = kolicina
            with open("zalihe.json", "w") as json_file:
                zz = json.dump(zalihe, json_file, indent=2)
                return ("Količina izmjenjena")
    print ("Proizvod ne postoji") 

    

izvjestaj(zalihe)

narudzba = izvjestaj(zalihe)

with open("narudzba.json","w") as json_file:
    data1 = json.dump(narudzba, json_file, indent=2)

azuriraj_kolicinu(zalihe, "Mlijeko 1L", 7)




