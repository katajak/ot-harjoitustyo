# Käyttöohje

## Käynnistäminen

Suorita komennot projektin juurihakemistossa:

poetry install

poetry run invoke start

## Konfigurointi

Pelin aloitusruudussa toimivat seuraavat valinnat (näppäimistöllä):

- E: Endless eli loputon moodi
- N: Normal eli perusmoodi (11 pisteeseen)
- 1: Yhden pelaajan peli
  - 7: Helppo vaikeustaso
  - 8: Kohtalainen vaikeustaso
  - 9: Vaikea vaikeustaso
- 2: Kahden pelaajan peli

## Pelaaminen

Kun olet valinnut haluamasi asetukset aloitusnäytöllä, voit aloittaa pelin painamalla välilyöntiä tai enteriä.

Pelaaja 1 liikuttaa näytön vasemmalla puolella olevaa mailaa w, s näppäimillä ja pelaaja 2 näytön oikealla puolella olevaa mailaa ylä- ja alanuolilla.

Pelin tavoite on saada pallo vastustajan puoleiseen seinään. Pallo kimpoaa ylä- ja alaseinistä samalla tavalla joka kerta mutta maila muuttaa pallon suuntaa ja nopeutta.

Peli loppuu 11 pisteeseen paitsi jos loputon moodi on päällä.

Pelin voi koska tahansa sulkea painamalla ESC-näppäintä.

Huomaathan että tietokantaan tallennetaan vain normaalimoodin tulokset. Loputtomassa moodissa tietokantaan ei tallenneta mitään.
