# Notikumu piezīmju ģenerators

## Projekta uzdevums

Izveidot sistēmu, kas automatizē ikdienas piezīmju veikšanu — ļauj pievienot notikumu pierakstus ar datuma un laika zīmogu, apskatīt iepriekšējos ierakstus, meklēt pēc konkrēta datuma, kā arī saglabāt piezīmju kopiju pirms aizvēršanas.

## Lietotās Python bibliotēkas

- `datetime` — lai pievienotu automātisku datuma un laika zīmogu
- `os` — failu pārbaudei un kopēšanai
- `pytz` — Latvijas (Rīgas) laika joslas iestatīšanai

## Projekta izstrādes laikā izmantotās datu struktūras

- `.txt` fails (`piezimes.txt`), kur katra piezīme tiek saglabāta atsevišķā rindā, formātā:  
  `DD-MM-YYYY HH:MM:SS - Piezīmes saturs`

- Izvades kopijas fails:  
  `piezimes_kopija_DD-MM-YYYY_HH-MM-SS.txt`, kas tiek ģenerēts pēc lietotāja izvēles pirms programmas iziešanas.

## Programmatūras izmantošanas metodes

- **Pievienot piezīmi:** Lietotājs ievada tekstu, un tas tiek saglabāts ar automātisku datuma un laika zīmogu, izmantojot Latvijas laiku.
- **Apskatīt visas piezīmes:** Parāda visus ierakstus no teksta faila.
- **Meklēt pēc datuma:** Lietotājs ievada datumu formātā `DD-MM-YYYY`, un programma parāda visas atbilstošās piezīmes.
- **Kopijas izveidošana pirms iziešanas:** Programma, pirms iziešanas, piedāvā lietotājam izveidot visu piezīmju kopiju. Kopijas fails tiek nosaukts ar precīzu datumu un laiku.
- Lietotāja saskarne balstīta uz konsoli (`CLI`), tāpēc darbojas jebkurā Python vidē, arī GitHub Codespaces vai serveros bez GUI.

## Piemērs

26-05-2025 17:44:10 - Aizgāju uz lekciju
26-05-2025 18:30:01 - Pabeidzu programmēšanas projektu

## Papildu informācija

- Visas datuma un laika operācijas tiek veiktas, izmantojot **Latvijas laiku (Europe/Riga)**.
- Programma automātiski izveido kopiju tikai tad, ja lietotājs to apstiprina.
- Visi dati tiek glabāti lokāli `.txt` failos.

