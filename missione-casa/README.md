# Missione casa — escape room

Escape room per il telefono che ripassa l'unità «Cercare casa a Bari»
(italiano L2, livello A0/A1). Si apre con un link, senza app e senza account.

Link: https://italianol2sai.github.io/missione-casa/

## I file

| File | A cosa serve |
|---|---|
| `index.html` | la pagina del gioco |
| `persone.js` | i ritratti disegnati e i nomi dei personaggi |
| `domande.js` | **le domande, le risposte, gli aiuti**: per cambiare il gioco si modifica solo questo file |
| `gioco.js` | il programma che fa funzionare il gioco (lo stesso di `missione-lavoro/`) |
| `stile.css` | colori e grafica |

## La storia

Maryam, 26 anni, è in Italia da due anni e vive a Bari in un appartamento del progetto SAI.
Ha un lavoro a tempo pieno e tra due mesi deve lasciare l'appartamento: cerca una casa sua.
La aiuta Serena, operatrice di Etnie (progetto SAI di Bari). Alla fine la signora Rosa, la proprietaria,
le dà le chiavi del bilocale a San Pasquale. I ritratti sono disegni (file `persone.js`), non foto.

## Le 6 porte

Ogni porta ripassa una parte di `cercare-casa/` e dà una lettera. Le lettere formano la parola segreta **CHIAVI**.

1. LE STANZE DELLA CASA → C
2. LE PAROLE DEGLI ANNUNCI → H
3. LEGGO GLI ANNUNCI → I
4. DOCUMENTI E SOLDI → A
5. SCRIVO AL PROPRIETARIO → V
6. LA TELEFONATA → I

## Come funziona

- 35 prove: scegli la risposta, vero o falso, completa la frase, collega, metti in ordine, trova l'errore.
- 10 punti se la risposta è giusta al primo tentativo, 5 punti dopo un errore o con l'aiuto.
- Dopo 2 errori l'aiuto compare da solo. Non si perdono mai punti.
- 🔊 ASCOLTA legge la domanda con la voce del telefono (se il telefono la ha).
- I progressi restano salvati sul telefono dello studente (localStorage). Nessun dato personale.
- Alla fine: punteggio, prove superate, percentuale, argomenti da ripassare con il link alla lezione.

## Cambiare una domanda

1. Su GitHub apri `missione-casa/domande.js` e tocca la matita ✏️ (Edit).
2. Cambia il testo tra virgolette. Scrivi sempre in MAIUSCOLO.
3. `correct: 0` vuol dire che la risposta giusta è la prima della lista (le risposte vengono mescolate nel gioco).
4. Tocca **Commit changes**. Dopo circa un minuto il sito è aggiornato.
