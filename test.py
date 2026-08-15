# Zadatak 1
def odd_even(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(odd_even(3))
print(odd_even(4))
print(odd_even(67))


# Zadatak 2
def list_10(l):
    rez = []
    for i in l:
        if i > 10:
            rez.append(i)
    return rez

print(list_10([1,2,6,55,10,12,3,98]))

# Zadatak 3
def name_sur(ime,prezime):
    return f"{ime}" + " " + f"{prezime}"

print(name_sur("Juraj", "Mesarić"))

# Zadatak 4
def lista(l):
    n = 0
    for i in l:
        n += 1
    return n

print(lista([1,2,3]))


# Zadatak 5
def dj(x):
    n = []
    for i in range(1, x + 1):
        if (x % i == 0):
            n.append(i)
    return n

print(dj(12))