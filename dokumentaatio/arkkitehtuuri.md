# Arkkitehtuuri

## Rakenne

Peli koostuu eri moduuleista. Kun peli käynnistetään, title_screen.py välittää valitut asetukset eteenpäin GameLoopiin ja EventHandlerille.

## Käyttöliittymä

Pelissä on kaksi päänäkymää. Ensin on title screen eli aloitusnäyttö jossa pelaaja voi valita asetukset ja pelaaja näkee myös miten peliä käytetään (kontrollit) ja tilastoja.

Itse pelinäkymässä näkyy mailojen ja pallon lisäksi pistetilanne. Pelin päätyttyä, ohjelma palaa aloitusnäytölle.

## Tiedon tallennus

Peli tallentaa SQLite tietokantaan pelin lopputuloksen ja muita tietoja. Tästä vastaa database.py tiedosto.

## Luokkakaavio

![luokkakaavio](./kuvat/luokkakaavio.png)

## Sekvenssikaavio

![sekvenssikaavio](./kuvat/sekvenssi.png)
