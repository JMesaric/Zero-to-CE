# Prvi dio projekta za skladištenje robe po uzoru na trgovinu
Ovaj projekt zamišljen je kao vježba pri izradu projekta. On bi trebao omogućiti snalaženje kroz proizvode neke trgovine koji su u skladištu, trenutno nema interface pa se sve radi u direktno kroz python. Kod uključuje i različite funkcije za koje se vjeruje da mogu pomoći kroz rad s proizvodima u trgovini.

## Funkcije
Postoji pet različitih funkcija: trebam_nar, kol_nar, izvjestaj, dodaj_proizvod, azuriraj_kolicinu. 
### trebam_nar služi da bi provjerili treba li određen proizvod naručiti, ona se pokreće pozivomm, a kao argument prima rječnik s indeksom koji označava proizvod. Vraća samo True ili False ukoliko treba ili ne treba naručiti neki proizvod
### kol_nar vraća broj koji govori o tome koju kolicinu nekog proizvoda treba naručiti i vratit će nam broj, argument je isti kao i kod prethodne funkcije
### izvjestaj je funkcija koja vraća sve proizvode koje treba naručiti, to su proizvodi čija je količina manja od minimuma, tu smo koristili prethodno opisanu funkciju za provjeru kolicine, a zatim potvrdili da treba naručiti pomoću prve opisane funkcije
### dodaj_proizvod je funkcija koja služi kako bi dodali novi proizvod, ukoliko se taj proizvod već nalazi unutar rječnika njegova količina se samo ažurira, jer se smatra da ga ponovno uvodimo što bi značilo da smo ga još dobili
### azuriraj_kolicinu je funkcija koja kao argument prima naziv i novu kolicinu koja se upisuje
svi rezultati koji nešto mjenjaju se upisuju ili u zalihe.json ukoliko se radi o dodavanju novog proizvoda ili u narudzba.json ukoliko se radi o izvještaju

## Tehnologije
Najviše se koristio običan python, pored njega koristio sam i JSON

## Pokretanje
Skripta se pokreće kao i svaki python kod pomoću python main.py

## Struktura projekta
Za pokretanje projekta je potrebno u istoj mapi imati main.py iz kojeg se gleda rječnik zalihe.json, kojeg je također potrebno imati u istoj mapi. Nadalje, funkcije.py su importane u main.py, dok se narudzba.json dinamički napravi sama kao fajl.
