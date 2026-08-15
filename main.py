import json

with open('zalihe.json') as f:
    zalihe = json.load(f)


def trebam_nar(proizvod):
    return (proizvod['minimum'] > proizvod['kolicina'])

def kol_nar(proizvod):
    return (proizvod['maksimum'] - proizvod['kolicina'])


def izvjestaj(zalihe):
    for i in zalihe:
        if trebam_nar(i):
            print(f"Trebam naruciti {i['naziv']}: {kol_nar(i)} komada")

izvjestaj(zalihe)