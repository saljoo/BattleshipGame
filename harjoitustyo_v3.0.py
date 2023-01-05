import random
import time
import ast
import os
from datetime import datetime

# Koneen arpoma vaakakordinaatti
def kone_vaaka() -> str:
    kirjaimet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    vaaka = random.choice(kirjaimet)
    return vaaka

# Koneen arpoma pystykordinaatti
def kone_pysty() -> int:
    pysty = random.randint(1, 10)
    return pysty

#Funktio jolla asetetaan koneen laivat ruudukkoon
def koneen_laivan_teko(pituus: int) -> list:
    kirjaimet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    suunta = random.randint(0,1)
    vaaka = kone_vaaka()
    pysty = kone_pysty()
    koordinaatti = []
    edellisetPysty = [pysty, pysty]
    edellisetVaaka = [vaaka, vaaka]
    pysty1, pysty10, vaaka0, vaaka9 = False, False, False, False
    x = 1
    #Suunta 0 on vaaka
    if suunta == 0:
        #Jos ensimmäinen koordinaatti on reunassa, muodostetaan laiva ruudukon keskiosan suuntaan
        if pysty == 1:
            koordinaatti.append((vaaka, pysty))
            pysty1 = True
        elif pysty == 10:
            koordinaatti.append((vaaka, pysty))
            pysty10 = True
        else:
            koordinaatti.append((vaaka, pysty))
    #Laiva pystyyn
    else:
        #Jos ensimmäinen koordinaatti on reunassa, muodostetaan laiva ruudukon keskiosan suuntaan
        if vaaka == kirjaimet[0]:
            koordinaatti.append((vaaka, pysty))
            vaaka0 = True
        elif vaaka == kirjaimet[9]:
            koordinaatti.append((vaaka, pysty))
            vaaka9 = True
        else:
            koordinaatti.append((vaaka, pysty))
    while x < pituus:
        #Muodostetaan laivat, jotka alkavat reunasta
        if pysty1 == True:
            koordinaatti.append((vaaka, 1 + x))
        elif pysty10 == True:
            koordinaatti.append((vaaka, 10 - x))
        elif vaaka0 == True:
            koordinaatti.append((kirjaimet[0 + x], pysty))
        elif vaaka9 == True:
            koordinaatti.append((kirjaimet[9 - x], pysty))
        else:
            #Muodostetaan laivat, jotka eivät ala reunasta
            #Suunta 0 on vaaka
            if suunta == 0:
                pystySeuraava = random.randint(0, 1)
                #Seuraavan koordinaatin pysty on 1 pienempi kuin edellinen pienin pysty
                if pystySeuraava == 0:
                    koordinaatti.append((vaaka, edellisetPysty[0] - 1))
                    #Pienennetään edellistä pienintä yhdellä
                    edellisetPysty[0] -= 1
                    #Jos uusi pienin on 1, lisätään seuraavat laivan perään keskelle
                    if edellisetPysty[0] == 1:
                        pysty1 = True
                else:
                    #Seuraavan koordinaatin pysty on 1 suurempi kuin edellinen suurin pysty
                    koordinaatti.append((vaaka, edellisetPysty[1] + 1))
                    #Suurennetaan edellistä suurinta yhdellä
                    edellisetPysty[1] += 1
                    #Jos uusi suurin on 10, lisätään seuraavat laivan perään keskelle
                    if edellisetPysty[1] == 10:
                        pysty10 = True
            #Laivan suunta on pysty
            else:
                vaakaSeuraava = random.randint(0, 1)
                #Seuraavan koordinaatin vaaka on 1 pienempi kuin edellinen pienin vaaka
                if vaakaSeuraava == 0:
                    koordinaatti.append((kirjaimet[kirjaimet.index(edellisetVaaka[0]) - 1], pysty))
                    #Muutetaan uusi vaakakoordinaatti uudeksi pienimmäksi vaakakoordinaatiksi
                    edellisetVaaka[0] = kirjaimet[kirjaimet.index(edellisetVaaka[0]) - 1]
                    #Jos uusi pienin on A, lisätään seuraavat laivan perään keskelle
                    if edellisetVaaka[0] == kirjaimet[0]:
                        vaaka0 = True
                else:
                    #Seuraavan koordinaatin vaaka on 1 suurempi kuin edellinen suurin vaaka
                    koordinaatti.append((kirjaimet[kirjaimet.index(edellisetVaaka[1]) + 1], pysty))
                    #Muutetaan uusi vaakakoordinaatti uudeksi suurimmaksi vaakakoordinaatiksi
                    edellisetVaaka[1] = kirjaimet[kirjaimet.index(edellisetVaaka[1]) + 1]
                    #Jos uusi suurin on J, lisätään seuraavat laivan perään keskelle
                    if edellisetVaaka[1] == kirjaimet[9]:
                        vaaka9 = True
        #Kasvatetaan laivan pituutta laskevaa muuttujaa yhdellä
        x += 1
    #Palautetaan järjestettylista, joka sisältää laivan koordinaatit
    koordinaatti.sort()
    return koordinaatti

#Funktio jolla tarkistetaan, etteivät laivat ole päällekkäin tai vierekkäin
def laivojen_tarkistus(laivat: list) -> bool:
    kirjaimet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    a = 0
    b = 0
    x = 1
    y = 0
    #Tarkistetaan kaikki laivat läpi
    while a < len(laivat) - 1:
        b = 0
        while b < len(laivat[a]):
            x = a + 1
            while x < len(laivat):
                y = 0
                while y < len(laivat[x]):
                    #Tarkistetaan etteivät koordinaatit ole täysin samat
                    if laivat[a][b] == laivat[x][y]:
                        return False
                    #Tarkistetaan etteivät koordinaattien numerot ole vierekkäin, jos kirjaimet ovat samat
                    elif laivat[a][b][0] == laivat[x][y][0]:
                        if laivat[x][y][1] == laivat[a][b][1] - 1 or laivat[x][y][1] == laivat[a][b][1] + 1:
                            return False
                    #Tarkistetaan etteivät koordinaattien kirjaimet ole vierekkäin, jos numerot ovat samat
                    elif laivat[x][y][1] == laivat[a][b][1]:
                        if kirjaimet.index(laivat[x][y][0]) == 0:
                            if kirjaimet.index(laivat[x][y][0]) == kirjaimet.index(laivat[a][b][0]) - 1:
                                return False
                        elif kirjaimet.index(laivat[x][y][0]) == 9:
                            if kirjaimet.index(laivat[x][y][0]) == kirjaimet.index(laivat[a][b][0]) + 1:
                                return False
                        else:
                            if kirjaimet.index(laivat[x][y][0]) == kirjaimet.index(laivat[a][b][0]) + 1 or kirjaimet.index(laivat[x][y][0]) == kirjaimet.index(laivat[a][b][0]) - 1:
                                return False
                    y += 1
                x += 1
            b += 1
        a += 1
    return True
    
#Funktio, jolla luodaan kaikki koneen laivat
def koneen_laivat() -> list:
    while True:
        laivat = []
        laivat.append(koneen_laivan_teko(5))
        laivat.append(koneen_laivan_teko(4))
        laivat.append(koneen_laivan_teko(3))
        laivat.append(koneen_laivan_teko(3))
        laivat.append(koneen_laivan_teko(2))
        laivat.append(koneen_laivan_teko(1))
        #Tarkistetaan, etteivät laivat ole päällekkäin tai vierekkäin
        if laivojen_tarkistus(laivat) == True:
            break
    
    return laivat

#Koneen ampumat koordinaatit
def koneen_ampuminen(ammutut: list) -> tuple:
    #Suoritetaan kunnes löytyy koordinaatti, johon ei ole ammuttu
    while True:
        sama = False
        vaaka = kone_vaaka()
        pysty = kone_pysty()
        koordinaatti = (vaaka, pysty)
        #Käydään läpi lista, johon on tallennettu kaikki ammutut koordinaatit
        for i in ammutut:
            if i == koordinaatti:
                sama = True
                break
        if sama == False:
            break
    return koordinaatti

#Funktio, jossa luodaan pelaajan laivat
def laivan_luonti(koordinaatit: str, pituus: int):
    laiva = []
    kirjaimet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    try:
        #Yhden mittaiselle laivalle asetetaan alku ja loppu samaksi
        if pituus == 1:
            alkuVaaka = kirjaimet.index(koordinaatit.strip()[0].upper())
            alkuPysty = int(koordinaatit.strip()[1:])
            loppu = (kirjaimet[alkuVaaka], alkuPysty)
        if pituus > 1:
            #Tarkistetaan, että syöte on oikean mittainen
            if len(koordinaatit) < 7 or len(koordinaatit) > 12:
                print("Koordinaatit on syötetty väärässä muodossa.")
                return False
                #Erotetaan koordinaatit syötteestä
            koordinaatit = koordinaatit.split("ja")
            alkuVaaka = kirjaimet.index(koordinaatit[0].strip()[0].upper())
            alkuPysty = int(koordinaatit[0].strip()[1:])
            loppu = (koordinaatit[1].strip()[0].upper(), int(koordinaatit[1].strip()[1:]))
            #Jos koordinaatit ovat samat:
        #Tarkistetaan, että numerot on annettu oikein
        if alkuPysty < 1 or alkuPysty > 10 or loppu[1] < 1 or loppu[1] > 10:
            print("Numerot ovat väärin.")
            return False
        elif alkuPysty != loppu[1] and abs(loppu[1] - alkuPysty) != pituus - 1:
            print("Numerot ovat väärin.")
            return False
        #Jos koordinaatit syötetään suuremmasta pienempään, käännetään niiden järjestys
        if alkuPysty > loppu[1] or alkuVaaka > kirjaimet.index(loppu[0]):
            uusiLoppu = (kirjaimet[alkuVaaka], alkuPysty)
            alkuVaaka = kirjaimet.index(loppu[0])
            alkuPysty = loppu[1]
            loppu = uusiLoppu
    #Jos syötteessä on vääriä merkkejä       
    except ValueError:
        print("Koordinaatit on syötetty väärässä muodossa.")
        return False
    except IndexError:
        print("Koordinaatit on syötetty väärässä muodossa.")
        return False
    else:
        #Luodaan laiva
        while len(laiva) < pituus:
            #Laiva on vaakatasossa
            if pituus > 1:
                if (kirjaimet[alkuVaaka], alkuPysty) == loppu:
                    print("Koordinaatit on syötetty väärin!")
                    return False
            if kirjaimet[alkuVaaka] == loppu[0]:
                laiva.append((kirjaimet[alkuVaaka], alkuPysty + len(laiva)))
            #Laiva on pystyssä
            elif alkuPysty == loppu[1]:
                laiva.append((kirjaimet[alkuVaaka + len(laiva)], alkuPysty))
            else:
                print("Koordinaateissa on virhe")
                return False
    return laiva

#Funktio, joka kutsuu laivan_luonti() -funktiota ja jossa pelaaja luo omat laivansa
def pelaajan_laivat(pelaajanNimi) -> list:
    laivat = []
    print("\nValitaan laivasi sijainnit!")
    print("Anna laivasi sijainnit koordinaatteina, ensin kirjain ja sitten numero.")
    print("Erota alku- ja päätepisteiden koordinaatit sanalla \"ja\". Voit antaa syötteeksi esimerkiksi \"B9 ja D9\"")
    time.sleep(2)
    ruudukko(pelaajanNimi)
    #Pyydetään pelaajalta koordinaatit kaikkiin laivoihin
    #Apumuuttujat x ja y
    x = 5
    y = 0
    while x >= 1:
        match x:
            case 5:
                laiva = input("Anna lentotukialuksen (5 ruutua) alku- ja päätepiste koordinaatteina: ")
            case 4:
                laiva = input("Anna taistelulaivan (4 ruutua) alku- ja päätepiste koordinaatteina: ")
            case 3:
                laiva = input("Anna risteilijän (3 ruutua) alku- ja päätepiste koordinaatteina: ")
            case 2:
                laiva = input("Anna hävittäjän (2 ruutua) alku- ja päätepiste koordinaatteina: ")
            case 1:
                laiva = input("Anna sukellusveneen (1 ruutu) koordinaatti: ")
        #Jos laivan luonti palauttaa laivan listana, lisätään se kaikkien laivojen listaan
        if laivan_luonti(laiva, x) != False:
            laivat.append(laivan_luonti(laiva, x))
            #Jos tarkistus palauttaa False, poistetaan kaikkien laivojen listalta viimeinen laiva ja pyydetään koordinaatit uudestaan
            if laivojen_tarkistus(laivat) == False:
                laivat.pop(len(laivat) - 1)
                print("Laivat eivät saa olla vierekkäin tai päällekkäin.")
                time.sleep(2)
                os.system("cls" if os.name == "nt" else "clear")
                print("\nValitaan laivasi sijainnit!")
                print("Anna laivasi sijainnit koordinaatteina, ensin kirjain ja sitten numero.")
                print("Erota alku- ja päätepisteiden koordinaatit sanalla \"ja\". Voit antaa syötteeksi esimerkiksi \"B9 ja D9\"")
                ruudukko(pelaajanNimi, laivat)
            else:
                time.sleep(0.5)
                os.system("cls" if os.name == "nt" else "clear")
                print("\nValitaan laivasi sijainnit!")
                print("Anna laivasi sijainnit koordinaatteina, ensin kirjain ja sitten numero.")
                print("Erota alku- ja päätepisteiden koordinaatit sanalla \"ja\". Voit antaa syötteeksi esimerkiksi \"B9 ja D9\"")
                ruudukko(pelaajanNimi, laivat)
                if x == 3:
                    y += 1
                    if y == 2:
                        x -= 1
                else:
                    x -= 1
        else:
            time.sleep(2)
            os.system("cls" if os.name == "nt" else "clear")
            print("\nValitaan laivasi sijainnit!")
            print("Anna laivasi sijainnit koordinaatteina, ensin kirjain ja sitten numero.")
            print("Erota alku- ja päätepisteiden koordinaatit sanalla \"ja\". Voit antaa syötteeksi esimerkiksi \"B9 ja D9\"")
            ruudukko(pelaajanNimi, laivat)
    return laivat

#Funktio, jolla toteutetaan pelaajan ampuminen
def pelaajan_ampuminen(ammutut: list) -> tuple:
    kirjaimet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    sama = False
    try:
        koordinaatti = input("Anna koordinaatti, johon haluat ampua: ")
        if koordinaatti.lower() == "tallenna":
            return koordinaatti.lower()
        elif koordinaatti.lower() == "poistu":
            return koordinaatti.lower()
        koordinaatti = (koordinaatti.strip()[0].upper(), int(koordinaatti.strip()[1:]))
        if koordinaatti[0] not in kirjaimet or koordinaatti[1] not in range(1,11):
            print("Koordinaatti ei ole annettu oikein.")
            return False
        #Käydään läpi lista, jossa on jo ammutut koordinaatit
        for i in ammutut:
            if i == koordinaatti:
                sama = True
                print("Olet ampunut jo kyseiseen koordinaattiin!")
                return False
        if sama == False:
            return koordinaatti
    except IndexError:
        print("Koordinaatti ei ole annettu oikein.")
        return False
    except ValueError:
        print("Koordinaatti ei ole annettu oikein.")
        return False

#Funktio, joka tarkistaa upposiko laiva
def osui_ja_upposi(pelaajaL, koneL, pelaajanOsumat, koneenOsumat, koneenUponneet):
    poistaminenK = False
    poistaminenL = False
    #Tarkistetaan koneen laivat osumien varalta
    for laiva in koneL:
        osui = 0
        for osuma in pelaajanOsumat:
            if osuma in laiva:
                osui += 1
                if osui == len(laiva):
                    poistettavaK = koneL.index(laiva)
                    poistaminenK = True
    #Poistetaan laiva, joka tuhottu kokonaan
    if poistaminenK == True:
        koneenUponneet.append(koneL[poistettavaK])
        koneL.pop(poistettavaK)
        print("Osui ja upposi!")
    #Tarkistetaan pelaajan laivat osumien varalta
    for laiva in pelaajaL:
        osui = 0
        for osuma in koneenOsumat:
            if osuma in laiva:
                osui += 1
                if osui == len(laiva):
                    poistettavaL = pelaajaL.index(laiva)
                    poistaminenL = True
    #Poistetaan laiva, joka on tuhottu kokonaan
    if poistaminenL == True:
        pelaajaL.pop(poistettavaL)
        print("Osui ja upposi!")
    return koneenUponneet

#Funktio, jolla tarkistetaan, onko jompi kumpi tuhonnut toisen kaikki laivat
def pelinpaattyminen(pelaajanOsumat = [], koneenOsumat = [], pelaajanVuorot = 0, koneenVuorot = 0, pelaajanNimi = "", valinta = ""):
    paattyi = False
    if len(pelaajanOsumat) == 18:
        parhaat_tulokset(pelaajanVuorot, pelaajanNimi)
        paattyi = True
        print("""
 _    _  _____  _____ _______ _____ _______       _____  _______ _      _____ __   _   /   /   /
  \  /  |     |   |      |      |      |         |_____] |______ |        |   | \  |  /   /   / 
   \/   |_____| __|__    |    __|__    |         |       |______ |_____ __|__ |  \_| .   .   .  
                                                                                                
        """)
        time.sleep(2.5)
    elif len(koneenOsumat) == 18:
        parhaat_tulokset(koneenVuorot, "Kone")
        paattyi = True
        print("""        
          __  __
 _     _ _______ _    _ _____ _______ _____ _______       _____  _______ _      _____ __   _   /   /   /
 |_____| |_____|  \  /    |   |______   |      |         |_____] |______ |        |   | \  |  /   /   / 
 |     | |     |   \/   __|__ ______| __|__    |         |       |______ |_____ __|__ |  \_| .   .   .  
                                                                                                        
        """)
        time.sleep(2.5)
    tallennetun_poisto(valinta, paattyi)
    if paattyi == True:
        print("1 Päävalikkoon")
        print("2 Lopeta peli")
        print("")
        valinta = input("Valinta: ")
        if valinta == "1":
            os.system("cls" if os.name == "nt" else "clear")
            valikko()
        elif valinta == "2":
            os.system("cls" if os.name == "nt" else "clear")
            quit()

#Pelin visuaalinen alusta
def ruudukko(pelaajanNimi, laivat = [], kone = False, pelaajanOsumat = [], pelaajanHudit = [], koneenOsumat = [], koneenHudit = [], koneenUponneet = []):
    kirjaimet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    peliAlustaPelaaja = [
        ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
        ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
        ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
        ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
        ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
        ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
        ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
        ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
        ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
        ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·']
    ]

    peliAlustaKone = [
        ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
        ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
        ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
        ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
        ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
        ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
        ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
        ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
        ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
        ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·']
    ]

    #Tulostetaan ainoastaan pelaajan ruudukko
    if kone == False:
        if len(laivat) > 0:
            #Muutetaan O -> X niissä koordinaateissa, joissa on laiva
            for laiva in laivat:
                for koordinaatti in laiva:
                    peliAlustaPelaaja[kirjaimet.index(koordinaatti[0])][koordinaatti[1] - 1] = 'X'
        
        print("")
        print(f"{pelaajanNimi}:")
        print("    1 2 3 4 5 6 7 8 9 10")
        print("    ___________________")
        x = 0
        for rivi in peliAlustaPelaaja:
            rivi = str(rivi).replace(",", "")
            rivi = rivi.replace("'", "")
            print(f"{kirjaimet[x]}  |{rivi[1:len(rivi)-1]}")
            x += 1
        print("")
    #Tulostetaan vierekkäin sekä pelaajan, että koneen ruudukot
    else:
        if len(laivat) > 0:
            #Muutetaan . -> X niissä koordinaateissa, joissa on laiva
            for laiva in laivat:
                for koordinaatti in laiva:
                    peliAlustaPelaaja[kirjaimet.index(koordinaatti[0])][koordinaatti[1] - 1] = 'X'
            #Muutetaan osumat -> ¤ ja hudit -> -
            for osumaK in koneenOsumat:
                peliAlustaPelaaja[kirjaimet.index(osumaK[0])][osumaK[1] - 1] = "¤"
            for hutiK in koneenHudit:
                peliAlustaPelaaja[kirjaimet.index(hutiK[0])][hutiK[1] - 1] = "⚬"
            for osumaP in pelaajanOsumat:
                peliAlustaKone[kirjaimet.index(osumaP[0])][osumaP[1] - 1] = "¤"
            for hutiP in pelaajanHudit:
                peliAlustaKone[kirjaimet.index(hutiP[0])][hutiP[1] - 1] = "⚬"
            for laiva in koneenUponneet:
                for osuma in laiva:
                    peliAlustaKone[kirjaimet.index(osuma[0])][osuma[1] - 1] = "X"
            
        
        print("")
        valilyonnit = (29 - (len(pelaajanNimi) + 1)) * " "
        print(f"{pelaajanNimi}:{valilyonnit}KONE:")
        print("    1 2 3 4 5 6 7 8 9 10     " * 2)
        print("    ___________________      " * 2)
        x = 0
        while x < 10:
            riviPelaaja = str(peliAlustaPelaaja[x]).replace(",", "")
            riviPelaaja = riviPelaaja.replace("'", "")
            riviKone = str(peliAlustaKone[x]).replace(",", "")
            riviKone = riviKone.replace("'", "")
            print(f"{kirjaimet[x]}  |{riviPelaaja[1:len(riviPelaaja)-1]}" + "      " + f"{kirjaimet[x]}  |{riviKone[1:len(riviKone)-1]}")
            x += 1
        print("")

#Pelin nimi ja logo
def logo():
    logo = """    

 _      _______ _____ _    _ _______ __   _ _     _  _____   _____  _______ _     _ _______
 |      |_____|   |    \  /  |_____| | \  | |     | |_____] |     |    |    |     | |______
 |_____ |     | __|__   \/   |     | |  \_| |_____| |       |_____|    |    |_____| ______|                                                                                           

                                          __/___            
                                    _____/______|           
                            _______/_____\_______\_____     
                            \              < < <       |    
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """
    print(logo)
    print("                                                                                Versio: 3.0\n")

#Pelin säännöt
def saannot():
    while True:
        with open("saannot.txt", encoding='utf-8') as tiedosto:
            saannot = tiedosto.readlines()
            for rivi in saannot:
                print(rivi.strip())
            tiedosto.close()
        valikkoon = input("\nTakaisin valikkoon (k/e) ")
        if valikkoon.lower() == "k":
            os.system("cls" if os.name == "nt" else "clear")
            valikko()
        elif valikkoon.lower() == "e":
            os.system("cls" if os.name == "nt" else "clear")
        else:
            print("\nSoo soo, syöte ei ollut k tai e!")
            time.sleep(2)
            os.system("cls" if os.name == "nt" else "clear")

#Funktio, jolla tallennetaan pelaajan parhaat tulokset
def parhaat_tulokset(vuorot, nimi):
    tulokset = []
    rivit = []
    with open("parhaatTulokset.txt", "r") as tiedosto:
        for rivi in tiedosto:
            #Tallennetaan koko top tiedosto listaan rivit
            rivit.append(rivi.strip())
            if rivi.find("TOP") == -1:
                tulos = rivi.strip().split(" ")
                if len(tulos) == 4:
                    #Tallennetaan tulokset listaan ainoastaan numerot top tiedostosta
                    tulokset.append(tulos[2])
        tiedosto.close()
    x = 0
    for piste in tulokset:
        if vuorot < int(piste):
            break
        elif vuorot == int(piste):
            x += 1
            break
        x += 1
    if x < 5:
        with open("parhaatTulokset.txt", "w") as tiedosto:
            #Lisätään uusi top tulos oikeaan kohtaan tiedostoon
            match x:
                case 0:
                    tiedosto.write(rivit[0] + "\n" + f"1. {nimi}: {vuorot} vuoroa\n")
                    i = 1
                    while i < 5:
                        tiedosto.write(f"{i+1}." + rivit[i][2:] + "\n")
                        i += 1
                    tiedosto.close()
                case 1:
                    tiedosto.write(rivit[0] + "\n"+ rivit[1] + "\n" + f"2. {nimi}: {vuorot} vuoroa\n")
                    i = 2
                    while i < 5:
                        tiedosto.write(f"{i+1}." + rivit[i][2:] + "\n")
                        i += 1
                    tiedosto.close()
                case 2:
                    tiedosto.write(rivit[0] + "\n"+ rivit[1] + "\n" + rivit[2] + "\n" + f"3. {nimi}: {vuorot} vuoroa\n")
                    i = 3
                    while i < 5:
                        tiedosto.write(f"{i+1}." + rivit[i][2:] + "\n")
                        i += 1
                    tiedosto.close()
                case 3:
                    i = 0
                    while i < 4:
                        tiedosto.write(rivit[i] + "\n")
                        i += 1
                    tiedosto.write(f"4. {nimi}: {vuorot} vuoroa\n" + "5." + rivit[4][2:] + "\n")
                    tiedosto.close()
                case 4:
                    i = 0
                    while i < 5:
                        tiedosto.write(rivit[i] + "\n")
                        i += 1
                    tiedosto.write(f"5. {nimi}: {vuorot} vuoroa\n")
                    tiedosto.close()

#Pelin päävalikko
def valikko():
    #Tulostetaan päävalikkoa kunnes pelaaja valitsee vaihtoehdon, jolla valikosta poistutaan
    while True:
        logo()
        print("PÄÄVALIKKO\n")
        print("1 Aloita uusi peli")
        print("2 Jatka vanhaa peliä")
        print("3 Säännöt ja ohjeet")
        print("4 Parhaat tulokset")
        print("5 Lopeta peli")
        print("")
        valinta = input("Valinta: ")
        print("")
        os.system("cls" if os.name == "nt" else "clear")
        match valinta:
            case "1":
                peli(False, "", "", [], [], [], [], [], [], [], [], [], "", [], [], "", 0, 0)
            case "2":
                tallennetut()
            case "3":
                saannot()
            case "4":
                while True:
                    with open("parhaatTulokset.txt", "r") as tiedosto:
                        rivit = tiedosto.readlines()
                        for rivi in rivit:
                            print(rivi.strip())
                        tiedosto.close()
                    print("")
                    valikkoon = input("Takaisin valikkoon (k): ")
                    if valikkoon.lower() == "k":
                        os.system("cls" if os.name == "nt" else "clear")
                        break
                    else:
                        print("Syöte ei ollut oikein.")
                        time.sleep(1.5)
                        os.system("cls" if os.name == "nt" else "clear")
            case "5":
                while True:
                    varmistus = input("\n\n\n\nHaluatko varmasti lopettaa? (k/e) ")
                    if varmistus.lower() == "k":
                        quit()
                    elif varmistus.lower() == "e":
                        os.system("cls" if os.name == "nt" else "clear")
                        break
                    else:
                        print("\nSoo soo, syöte ei ollut k tai e!")
                        time.sleep(2)
                        os.system("cls" if os.name == "nt" else "clear")

#Funktio, jolla tallennetaan peli ulkoiseen tiedostoon. Pelejä voi tallentaa korkeintaa kolme kappaletta.
#Uusi tallennus tehdään pelaajan valitsemalle paikalle
def tallennus(koneenAmmutut, pelaajanAmmutut, pelaajanHudit, pelaajanOsumat, koneenOsumat, koneenHudit, koneenUponneet, pelaajanLaivat, koneenLaivat,
vuoro, koneL, pelaajaL, pelaajanNimi, pelaajanVuorot, koneenVuorot, tallenteenValinta, tallenne, nimi):
    #Luodaan tiedosto, kun tallennus tehdään ensimmäisen kerran
    try:
        f = open("tallennetutpelit.txt", "x")
        f.close()
    except FileExistsError:
        pass
    #Tämä suoritetaan aina, kun peli tallennetaan
    aika = datetime.now()
    pvm = aika.strftime("%d.%m.%Y")
    #Tyhjä lista, johon tallennetaan tiedostossa jo olevat tallennukset
    pelit = []
    with open("tallennetutpelit.txt", "r") as tallennetut1:
        for rivi in tallennetut1:
            pelit.append(rivi.strip())
        tallennetut1.close()
        #Jos peli on tallenne, se tallennetaan automaattisesti sen pelin päälle, jota on jatkettu
        if tallenne == True:
            tallennettava = {
                pvm + " " + pelaajanNimi + " " + nimi: {
                    "nimi": nimi,
                    "koneenAmmutut": koneenAmmutut,
                    "pelaajanAmmutut": pelaajanAmmutut,
                    "pelaajanHudit": pelaajanHudit,
                    "pelaajanOsumat": pelaajanOsumat,
                    "koneenOsumat": koneenOsumat,
                    "koneenHudit": koneenHudit,
                    "koneenUponneet": koneenUponneet,
                    "pelaajanLaivat": pelaajanLaivat,
                    "koneenLaivat": koneenLaivat,
                    "vuoro": vuoro,
                    "koneL": koneL,
                    "pelaajaL": pelaajaL,
                    "pelaajanNimi": pelaajanNimi,
                    "pelaajanVuorot": pelaajanVuorot,
                    "koneenVuorot": koneenVuorot
                }
            }
            with open("tallennetutpelit.txt", "w") as tallenteet:
                match tallenteenValinta:
                    case "1":
                        if len(pelit) == 1:
                            tallenteet.write(str(tallennettava) + "\n")
                        elif len(pelit) == 2:
                            tallenteet.write(str(tallennettava) + "\n" + pelit[1] + "\n")
                        elif len(pelit) == 3:
                            tallenteet.write(str(tallennettava) + "\n" + pelit[1] + "\n" + pelit[2] + "\n")
                    case "2":
                        if len(pelit) == 2:
                            tallenteet.write(pelit[0] + "\n" + str(tallennettava) + "\n")
                        elif len(pelit) == 3:
                            tallenteet.write(pelit[0] + "\n" + str(tallennettava) + "\n" + pelit[2] + "\n")
                    case "3":
                        tallenteet.write(pelit[0] + "\n" + pelit[1] + "\n" + str(tallennettava) + "\n")
                tallenteet.close()
        else:
            nimi = input("\nAnna tallenteen nimi: ")
            #Tallennetaan sanakirjaan kaikkien peliin vaadittavien muuttujien arvot. Nimetään sanakirja päivämäärän ja pelaajan antaman nimen mukaan
            tallennettava = {
                pvm + " " + pelaajanNimi + " " + nimi: {
                    "nimi": nimi,
                    "koneenAmmutut": koneenAmmutut,
                    "pelaajanAmmutut": pelaajanAmmutut,
                    "pelaajanHudit": pelaajanHudit,
                    "pelaajanOsumat": pelaajanOsumat,
                    "koneenOsumat": koneenOsumat,
                    "koneenHudit": koneenHudit,
                    "koneenUponneet": koneenUponneet,
                    "pelaajanLaivat": pelaajanLaivat,
                    "koneenLaivat": koneenLaivat,
                    "vuoro": vuoro,
                    "koneL": koneL,
                    "pelaajaL": pelaajaL,
                    "pelaajanNimi": pelaajanNimi,
                    "pelaajanVuorot": pelaajanVuorot,
                    "koneenVuorot": koneenVuorot
                }
            }
         #Jos tallennettuja pelejä on alle kolme, lisätään uusi tallennus
            if len(pelit) < 3:
                with open("tallennetutpelit.txt", "a") as tallennus:
                    tallennus.write(str(tallennettava) + "\n")
                    tallennus.close()
            #Jos tallennettuja pelejä on kolme, pyydetään käyttäjää valitsemaan minkä pelin tilalle uusi peli tallennetaan
            else:
                while True:
                    print("Tallennetut pelit\n")
                    print(f"1 {pelit[0][2:pelit[0].index(':') - 1]}")
                    print(f"2 {pelit[1][2:pelit[1].index(':') - 1]}")
                    print(f"3 {pelit[2][2:pelit[2].index(':') - 1]}")
                    valinta = input("\nTallenna paikalle (1, 2, 3): ")
                    if valinta == "1" or valinta == "2" or valinta == "3":
                        break
                    else:
                        print("Syötä joko 1, 2 tai 3.")
                        time.sleep(2)
                        os.system("cls" if os.name == "nt" else "clear")
                with open("tallennetutpelit.txt", "w") as tallennetut2:
                    match valinta:
                        case "1":
                            tallennetut2.write(str(tallennettava) + "\n" + pelit[1] + "\n" + pelit[2] + "\n")
                        case "2":
                            tallennetut2.write(pelit[0] + "\n" + str(tallennettava) + "\n" + pelit[2] + "\n")
                        case "3":
                            tallennetut2.write(pelit[0] + "\n" + pelit[1] + "\n" + str(tallennettava) + "\n")
                tallennetut2.close()
    os.system("cls" if os.name == "nt" else "clear")
    valikko()
    
#Funktio, jolla aloitetaan tallennettu peli
def tallennetut():
    tallenne = True
    pelit = []
    try:
        #Tulostetaan tallennetut pelit ja päävalikkoon paluu vaihtoehdot
        with open("tallennetutpelit.txt", "r") as tallennetut:
                for rivi in tallennetut:
                    pelit.append(rivi.strip())
                tallennetut.close()
        while True:
            if len(pelit) == 1:
                print("Tallennetut pelit\n")
                print(f"1 {pelit[0][2:pelit[0].index(':') - 1]}")
                print("4 PÄÄVALIKKOON\n")
            elif len(pelit) == 2:
                print("Tallennetut pelit\n")
                print(f"1 {pelit[0][2:pelit[0].index(':') - 1]}")
                print(f"2 {pelit[1][2:pelit[1].index(':') - 1]}")
                print("4 PÄÄVALIKKOON\n")
            elif len(pelit) == 3:
                print("Tallennetut pelit\n")
                print(f"1 {pelit[0][2:pelit[0].index(':') - 1]}")
                print(f"2 {pelit[1][2:pelit[1].index(':') - 1]}")
                print(f"3 {pelit[2][2:pelit[2].index(':') - 1]}")
                print("4 PÄÄVALIKKOON\n")
            valinta = input("valinta: ")
            #Tarkistetaan, että syöte on oikein
            if len(pelit) == 1 and valinta != "1" and valinta != "4":
                print("Syötä joko 1 tai 4.")
            elif len(pelit) == 2 and valinta != "1" and valinta != "2" and valinta != "4":
                print("Syötä joko 1, 2 tai 4.")
            elif len(pelit) == 3 and valinta != "1" and valinta != "2" and valinta != "3" and valinta != "4":
                print("Syötä joko 1, 2, 3 tai 4.")
            else:
                break
            time.sleep(2)
            os.system("cls" if os.name == "nt" else "clear")
        #Palautetaan valittu peli
        match valinta:
            case "1":
                tallennettu = ast.literal_eval(pelit[0][pelit[0].index(':') + 2:len(pelit[0]) - 1])
            case "2":
                tallennettu = ast.literal_eval(pelit[1][pelit[1].index(':') + 2:len(pelit[1]) - 1])
            case "3":
                tallennettu = ast.literal_eval(pelit[2][pelit[2].index(':') + 2:len(pelit[2]) - 1])
            case "4":
                os.system("cls" if os.name == "nt" else "clear")
                valikko()
        os.system("cls" if os.name == "nt" else "clear")
        peli(tallenne, valinta, tallennettu["nimi"], tallennettu["koneenAmmutut"], tallennettu["pelaajanAmmutut"], tallennettu["pelaajanHudit"], tallennettu["pelaajanOsumat"], tallennettu["koneenOsumat"],
        tallennettu["koneenHudit"], tallennettu["koneenUponneet"], tallennettu["pelaajanLaivat"], tallennettu["koneenLaivat"], tallennettu["vuoro"], tallennettu["koneL"],
        tallennettu["pelaajaL"], tallennettu["pelaajanNimi"], tallennettu["pelaajanVuorot"], tallennettu["koneenVuorot"])
    except FileNotFoundError:
        print("Tallennettuja pelejä ei löytynyt!\n")
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
        valikko()

#Funktio, joka poistaa tallennuksista loppuun pelatun jatketun pelin
def tallennetun_poisto(valinta, loppu):
    pelit = []
    if loppu == True:
        with open("tallennetutpelit.txt", "r") as tiedosto:
            for rivi in tiedosto:
                pelit.append(rivi.strip())
        tiedosto.close()
        with open("tallennetutpelit.txt", "w") as tallennetut:
            match valinta:
                case "1":
                    if len(pelit) == 1:
                        os.remove("tallennetutpelit.txt")
                    elif len(pelit) == 2:
                        tallennetut.write(pelit[1] + "\n")
                    elif len(pelit) == 3:
                        tallennetut.write(pelit[1] + "\n" + pelit[2] + "\n")
                case "2":
                    if len(pelit) == 2:
                        tallennetut.write(pelit[0] + "\n")
                    elif len(pelit) == 3:
                        tallennetut.write(pelit[0] + "\n" + pelit[2] + "\n")
                case "3":
                    tallennetut.write(pelit[0] + "\n" + pelit[1] + "\n")

#Funktio, jossa toteutetaan itse peli
def peli(tallenne = False, tallenteenValinta = "", nimi = "", koneenAmmutut = [], pelaajanAmmutut = [], pelaajanHudit = [], pelaajanOsumat = [], koneenOsumat = [], koneenHudit = [],
koneenUponneet = [], pelaajanLaivat = [], koneenLaivat = [], vuoro = "", koneL = [], pelaajaL = [], pelaajanNimi = "", pelaajanVuorot = 0, koneenVuorot = 0):
    #Jos aloitetaan uusi peli, suoritetaan seuraavat toimenpiteet
    if tallenne == False:
        pelaajanNimi = input("Syötä pelaajan nimi: ")
        #Asetetaan koneen laivat ja pyydetään pelaajaa asettamaan omansa
        koneenLaivat = koneen_laivat()
        pelaajanLaivat = pelaajan_laivat(pelaajanNimi)
        koneL = koneenLaivat.copy()
        pelaajaL = pelaajanLaivat.copy()
        pelaajanVuorot = 0
        koneenVuorot = 0
        #Arvotaan aloittaja
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            arvaus = input("Arvotaan aloittaja. Valitse kruuna (0) tai klaava (1): ")
            if arvaus == "0" or arvaus == "1":
                arvonta = str(random.randint(0,1))
                break
            else:
                print("Syötä joko 0 tai 1.")
        time.sleep(1)
        if arvaus == arvonta:
            #Nolla tarkoittaa pelaajan vuoroa
            print(f"{pelaajanNimi} aloittaa!")
            vuoro = 0
        else:
            #Yksi tarkoittaa koneen vuoroa
            print("Kone aloittaa!")
            vuoro = 1
    #Tästä eteenpäin suoritetaan aina
    time.sleep(0.5)
    os.system("cls" if os.name == "nt" else "clear")
    #Tulostetaan peliruudukko
    ruudukko(pelaajanNimi, pelaajanLaivat, True, pelaajanOsumat, pelaajanHudit, koneenOsumat, koneenHudit, koneenUponneet)
    while True:
        pelinpaattyminen(pelaajanOsumat, koneenOsumat, pelaajanVuorot, koneenVuorot, pelaajanNimi, tallenteenValinta)
        #Asetetaan osuma aina vuoron alussa arvoon False
        osuma = False
        #Pelaajan vuoro
        if vuoro == 0:
            pelaajanVuorot += 1
            time.sleep(0.5)
            while True:
                koordinaatti = pelaajan_ampuminen(pelaajanAmmutut)
                if koordinaatti == "tallenna":
                    while True:
                        varmistus = input("\nHaluatko varmasti tallentaa? (k/e) ")
                        if varmistus.lower() == "k":
                            os.system("cls" if os.name == "nt" else "clear")
                            tallennus(koneenAmmutut, pelaajanAmmutut, pelaajanHudit, pelaajanOsumat, koneenOsumat, koneenHudit, koneenUponneet,
                            pelaajanLaivat, koneenLaivat, vuoro, koneL, pelaajaL, pelaajanNimi, pelaajanVuorot, koneenVuorot, tallenteenValinta, tallenne, nimi)
                        elif varmistus.lower() == "e":
                            os.system("cls" if os.name == "nt" else "clear")
                            ruudukko(pelaajanNimi, pelaajanLaivat, True, pelaajanOsumat, pelaajanHudit, koneenOsumat, koneenHudit, koneenUponneet)
                            break
                        else:
                            print("\nSoo soo, syöte ei ollut k tai e!")
                            time.sleep(2)
                            os.system("cls" if os.name == "nt" else "clear")
                            ruudukko(pelaajanNimi, pelaajanLaivat, True, pelaajanOsumat, pelaajanHudit, koneenOsumat, koneenHudit, koneenUponneet)
                elif koordinaatti == "poistu":
                    while True:
                        varmistus = input("\nHaluatko varmasti poistua? Peliä ei tallenneta. (k/e) ")
                        if varmistus.lower() == "k":
                            os.system("cls" if os.name == "nt" else "clear")
                            valikko()
                        elif varmistus.lower() == "e":
                            os.system("cls" if os.name == "nt" else "clear")
                            ruudukko(pelaajanNimi, pelaajanLaivat, True, pelaajanOsumat, pelaajanHudit, koneenOsumat, koneenHudit, koneenUponneet)
                            break
                        else:
                            print("\nSoo soo, syöte ei ollut k tai e!")
                            time.sleep(2)
                            os.system("cls" if os.name == "nt" else "clear")
                            ruudukko(pelaajanNimi, pelaajanLaivat, True, pelaajanOsumat, pelaajanHudit, koneenOsumat, koneenHudit, koneenUponneet)
                elif koordinaatti == False:
                    time.sleep(2)
                    os.system("cls" if os.name == "nt" else "clear")
                    ruudukko(pelaajanNimi, pelaajanLaivat, True, pelaajanOsumat, pelaajanHudit, koneenOsumat, koneenHudit, koneenUponneet)
                else:
                    break
            pelaajanAmmutut.append(koordinaatti)
            #Tarkistetaan löytyykö ammuttu koordinaatti koneen laivojen koordinaateista
            for laiva in koneenLaivat:
                #Osui
                if pelaajanAmmutut[len(pelaajanAmmutut) - 1] in laiva:
                    pelaajanOsumat.append(pelaajanAmmutut[len(pelaajanAmmutut) - 1])
                    vuoro = 1 #vaihdetaan vuoro
                    osuma = True
                    print("Osuit!")
                    koneenUponneet = osui_ja_upposi(pelaajaL, koneL, pelaajanOsumat, koneenOsumat, koneenUponneet)
                    time.sleep(1)
                    os.system("cls" if os.name == "nt" else "clear")
                    ruudukko(pelaajanNimi, pelaajanLaivat, True, pelaajanOsumat, pelaajanHudit, koneenOsumat, koneenHudit, koneenUponneet)
                    break
            #Ei osumaa
            if osuma == False:
                vuoro = 1 #vaihdetaan vuoro
                pelaajanHudit.append(pelaajanAmmutut[len(pelaajanAmmutut) - 1])
                print("Ammuit ohi!")
                time.sleep(1)
                os.system("cls" if os.name == "nt" else "clear")
                ruudukko(pelaajanNimi, pelaajanLaivat, True, pelaajanOsumat, pelaajanHudit, koneenOsumat, koneenHudit, koneenUponneet)

        #Koneen vuoro
        elif vuoro == 1:
            koneenVuorot += 1
            time.sleep(1)
            print("Koneen vuoro:")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(". .")
            time.sleep(0.5)
            print(". . .")
            koneenAmmutut.append(koneen_ampuminen(koneenAmmutut))
            time.sleep(0.5)
            #Tarkistetaan löytyykö ammuttu koordinaatti pelaajan laivojen koordinaateista
            for laiva in pelaajanLaivat:
                #Osui
                if koneenAmmutut[len(koneenAmmutut) - 1] in laiva:
                    koneenOsumat.append(koneenAmmutut[len(koneenAmmutut) - 1])
                    vuoro = 0 #vaihdetaan vuoro
                    osuma = True
                    kirjain = koneenAmmutut[len(koneenAmmutut) - 1][0].replace("'", "")
                    ammuttu = f"({kirjain}, {koneenAmmutut[len(koneenAmmutut) - 1][1]})"
                    time.sleep(0.5)
                    print(f"Kone ampui koordinaattiin {ammuttu}")
                    time.sleep(0.5)
                    print("Kone osui!")
                    osui_ja_upposi(pelaajaL, koneL, pelaajanOsumat, koneenOsumat, koneenUponneet)
                    time.sleep(1)
                    os.system("cls" if os.name == "nt" else "clear")
                    ruudukko(pelaajanNimi, pelaajanLaivat, True, pelaajanOsumat, pelaajanHudit, koneenOsumat, koneenHudit, koneenUponneet)
            #Ei osumaa
            if osuma == False:
                koneenHudit.append(koneenAmmutut[len(koneenAmmutut) - 1])
                vuoro = 0 #vaihdetaan vuoro
                kirjain = koneenAmmutut[len(koneenAmmutut) - 1][0].replace("'", "")
                ammuttu = f"({kirjain}, {koneenAmmutut[len(koneenAmmutut) - 1][1]})"
                time.sleep(0.5)
                print(f"Kone ampui koordinaattiin {ammuttu}")
                time.sleep(0.5)
                print("Kone ampui ohi!")
                time.sleep(1)
                os.system("cls" if os.name == "nt" else "clear")
                ruudukko(pelaajanNimi, pelaajanLaivat, True, pelaajanOsumat, pelaajanHudit, koneenOsumat, koneenHudit, koneenUponneet)

os.system("cls" if os.name == "nt" else "clear")
valikko()