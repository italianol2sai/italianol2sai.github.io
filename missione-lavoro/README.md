# Missione lavoro — escape room

Escape room per il telefono che ripassa le lezioni di orientamento al lavoro
(italiano L2, livello A0/A1). Si apre con un link, senza app e senza account.

Link: https://italianol2sai.github.io/missione-lavoro/

## I file

| File | A cosa serve |
|---|---|
| `index.html` | la pagina del gioco |
| `persone.js` | i ritratti disegnati e i nomi dei personaggi |
| `domande.js` | **le domande, le risposte, gli aiuti**: per cambiare il gioco si modifica solo questo file |
| `gioco.js` | il programma che fa funzionare il gioco |
| `stile.css` | colori e grafica |

## La storia

Mohammad, 19 anni, è in Italia da due anni e vive a Bari nel progetto SAI. Vuole lavorare.
Lo aiutano Silvia, Francesco e Giulio, operatori di orientamento al lavoro di Etnie (progetto SAI di Bari).
I ritratti sono disegni (file `persone.js`), non foto.

## Le 7 porte

Ogni porta ripassa una lezione del sito e dà una lettera. Le lettere formano la parola segreta **ASSUNTO**.

1. CHE LAVORO FAI? → `che-lavoro-fai/` → A
2. I MIEI DOCUMENTI → `cercare-lavoro/` → S
3. CERCO LAVORO → `cercare-lavoro/` → S
4. IL MIO CURRICULUM → `curriculum/` → U
5. IL COLLOQUIO → `colloquio-contratti/` → N
6. IL CONTRATTO → `colloquio-contratti/` → T
7. LA BUSTA PAGA → `busta-paga/` → O

## Come funziona

- 33 prove: scegli la risposta, vero o falso, completa la frase, collega, metti in ordine, trova l'errore.
- 10 punti se la risposta è giusta al primo tentativo, 5 punti dopo un errore o con l'aiuto.
- Dopo 2 errori l'aiuto compare da solo. Non si perdono mai punti.
- 🔊 ASCOLTA legge la domanda con la voce del telefono (se il telefono la ha).
- I progressi restano salvati sul telefono dello studente (localStorage). Nessun dato personale, niente arriva all'insegnante.
- Alla fine: punteggio, prove superate, percentuale, argomenti da ripassare con il link alla lezione.

## Cambiare una domanda

1. Su GitHub apri `missione-lavoro/domande.js` e tocca la matita ✏️ (Edit).
2. Cambia il testo tra virgolette. Scrivi sempre in MAIUSCOLO.
3. `correct: 0` vuol dire che la risposta giusta è la prima della lista (le risposte vengono mescolate nel gioco).
4. Tocca **Commit changes**. Dopo circa un minuto il sito è aggiornato.

## Pubblicazione su GitHub Pages

Il sito https://italianol2sai.github.io/ è già pubblicato con GitHub Pages dal branch `main`.
Basta che la cartella `missione-lavoro/` sia nel repository: GitHub la pubblica da solo.
