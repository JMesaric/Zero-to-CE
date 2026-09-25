import json

#Prima proizvod i vraća True ili False ukoliko treba ili ne treba naručiti
def trebam_nar(proizvod):
    return (proizvod['minimum'] > proizvod['kolicina'])

#Vraća trenutnu količinu proizvoda
def kol_nar(proizvod):
    return (proizvod['maksimum'] - proizvod['kolicina'])

#Vraća izvještaj koliko čega ima
def izvjestaj(zalihe):
    report = {}
    for i in zalihe:
        if trebam_nar(i):
            report[i['naziv']] = kol_nar(i)
    return report

#Funkcija pomoću koje možeš dodati proizvod
def dodaj_proizvod(zalihe, naziv, kolicina, minimum, maksimum):
    d =  {}
    for i in zalihe:
        if (i["naziv"] == naziv):
            i["kolicina"] += kolicina
            with open("zalihe.json", "w") as json_file:
                    zz = json.dump(zalihe, json_file, indent=2)
            return "Uspjesno azurirano"
    d["naziv"] = naziv
    d["kolicina"] = kolicina
    d["minimum"] = minimum
    d["maksimum"] = maksimum
    zalihe.append(d)

    with open("zalihe.json", "w") as json_file:
        zz = json.dump(zalihe, json_file, indent=2)
    return "Proizvod je uspješno dodan"

#Funkcija pomoću koje ažuruiramo količinu već postojećeg proizvoda
def azuriraj_kolicinu(zalihe, naziv, kolicina):
    for i in zalihe:
        if (i["naziv"] == naziv):
            i["kolicina"] = kolicina
            with open("zalihe.json", "w") as json_file:
                zz = json.dump(zalihe, json_file, indent=2)
                return ("Količina izmjenjena")
    print ("Proizvod ne postoji") 