# Käyttöohje

## Konfigurointi

Tällä hetkellä pelin loputtoman moodin saa päälle muuttamalla tiedostossa index.py rivi 16 ENDLESS = True

## Käynnistäminen

Suorita komennot projektin juurihakemistossa:

poetry install

poetry run invoke start

## Pelaaminen

Pelaaja 1 liikuttaa näytön vasemmalla puolella olevaa mailaa w, s näppäimillä ja pelaaja 2 näytön oikealla puolella olevaa mailaa ylä- ja alanuolilla.

Pelin tavoite on saada pallo vastustajan puoleiseen seinään. Pallo kimpoaa ylä- ja alaseinistä samalla tavalla joka kerta mutta maila muuttaa pallon suuntaa ja nopeutta.

Peli loppuu 11 pisteeseen paitsi jos loputon moodi on päällä.

Pelin voi koska tahansa sulkea painamalla ESC-näppäintä.
