import os 
import json

with open('kodovi.json','r') as f:
    data = json.load(f)

kodovi = open('kodovi.txt','w')
for i in data:
    if i['Level'] == 2:
        kodovi.write(i['RootCpv'] + ": " + i['Name'] + '\n')

        771: Usluge u oblasti poljoprivrede
772: Šumarske usluge
773: Usluge u oblasti hortikulture763: Usluge bušenja731: Usluge u oblasti istraživanja i eksperimentalnog razvoja
732: Savetodavne usluge u oblasti istraživanja i razvoja
733: Planiranje i sprovođenje istraživanja i razvoja
712: Arhitektonske i srodne usluge
713: Tehničke usluge
714: Usluge prostornog planiranja i pejzažne arhitekture
715: Usluge u vezi sa građevinarstvom
716: Usluge tehničkog ispitivanja, analize i konsaltinga
717: Usluge praćenja i nadzora
718: Savetodavne usluge za vodosnabdevanje i otpadne vode
651: Distribucija vode i povezane usluge
631: Usluge rukovanja teretom i skladištenja tereta
635: Usluge putničkih agencija i tur-operatera i usluge pomoći turistima
637: Prateće usluge u kopnenom, vodenom i avio-prevozu
641: Poštanske i kurirske usluge
642: Telekomunikacione usluge
559: Usluge trgovine na malo
601: Usluge drumskog prevoza
602: Usluge železničkog prevoza
603: Usluge cevovodnog transporta
517: Usluge instaliranja opreme za zaštitu od požara
518: Usluge instaliranja metalnih kontejnera
519: Usluge instaliranja sistema vođenja i upravljanja
511: Usluge instaliranja električne i mehaničke opreme
513: Usluge instaliranja komunikacione opreme
515: Usluge instaliranja uređaja i opreme
507: Usluge popravke i održavanja instalacija u zgradama
508: Razne usluge popravke i održavanja
392: Proizvodi za unutrašnje opremanje
393: Razna oprema
395: Tekstilni proizvodi
397: Aparati za domaćinstvo
398: Proizvodi za čišćenje i poliranje
411: Prirodna voda
421: Mašine za proizvodnju i korišćenje mehaničke energije
422: Mašine za preradu hrane, pića i duvana i pripadajući delovi
423: Industrijske ili laboratorijske peći, peći za spaljivanje i pećnice
424: Oprema za dizanje i rukovanje teretom i delovi
425: Rashladni uređaji i oprema za ventilaciju
426: Mašine alatke
427: Mašine za proizvodnju tekstila, odeće i kože
428: Mašine za proizvodnju hartije  ili kartona
429: Razni uređaji opšte i posebne namene
431: Rudarska oprema
432: Mašine za zemljane radove i iskopavanje i pripadajući delovi
433: Građevinske mašine i oprema
434: Mašine za preradu minerala i izradu livničkih kalupa
435: Vozila za polaganje koloseka
436: Delovi mašina za rudarstvo, kamenolome i građevinarstvo
437: Mašine za metalurgiju i pripadajući delovi
438: Oprema za radionice
441: Građevinski materijali i pripadajući proizvodi
442: Konstrukcioni proizvodi
443: Kablovi, žice i srodni proizvodi
444: Razni gotovi proizvodi i srodni artikli
445: Alati, brave, ključevi, šarke, spojni elementi, lanci i opruge
446: Cisterne, rezervoari i kontejneri; radijatori za centralno grejanje i kotlovi
448: Boje, lakovi i smole
449: Građevinski kamen, krečnjak, gips i škriljac
451: Priprema gradilišta
452: Radovi na objektima ili delovima objekata visokogradnje i niskogradnje
453: Radovi na građevinskim instalacijama
454: Završni građevinski radovi
455: Iznajmljivanje mehanizacije i opreme za visokogradnju i niskogradnju sa operaterom