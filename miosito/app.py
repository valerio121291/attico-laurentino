<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Attico Panoramico a Roma - Landing Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f0f0f0;
            color: #333;
        }
        .header {
            background-color: #008080;
            color: white;
            padding: 20px;
            text-align: center;
        }
        .container {
            width: 80%;
            margin: 20px auto;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h2 {
            border-bottom: 2px solid #008080;
            padding-bottom: 5px;
            margin-top: 30px;
        }
        .photo-gallery {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            margin-top: 20px;
        }
        .photo-gallery img {
            width: 30%;
            height: auto;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        .contact-info a {
            color: #008080;
            text-decoration: none;
            font-weight: bold;
        }
        .map-container {
            position: relative;
            overflow: hidden;
            padding-top: 56.25%;
            margin-top: 20px;
        }
        .map-container iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: 0;
        }
    </style>
</head>
<body>

    <div class="header">
        <h1>Attico Panoramico con Terrazzo a Roma</h1>
        <p>Il tuo rifugio esclusivo per un soggiorno indimenticabile</p>
    </div>

    <div class="container">
        <h2>Descrizione dell'alloggio</h2>
        <p>Accogliente attico al 7° piano di un moderno edificio con ampio terrazzo panoramico in zona tranquilla e nelle immediate vicinanze di negozi, bar pasticceria, ristoranti e pizzerie. È ben collegato al centro di Roma tramite autobus che porta alla Metropolitana B Laurentina, a meno di 20 minuti dall'aeroporto di Fiumicino e meno di 15 dall'aeroporto di Ciampino. In posizione strategica per raggiungere sia il centro di Roma, sia i Castelli Romani che il litorale sud laziale.</p>

        <h2>Lo spazio</h2>
        <p>L'appartamento è adatto per 2 adulti e un neonato. Ampia camera da letto nella quale si può aggiungere un lettino per i bambini fino a 3 anni, un soggiorno con angolo cottura ben attrezzato, un bagno finestrato con cabina doccia. Biancheria da letto, bagno, shampoo, bagnoschiuma e saponi sono inclusi. Nell'ampio terrazzo dotato di tenda da sole sono presenti un tavolo con sedie e sdraio per godere momenti di relax in un'ambiente fresco e naturale. I servizi aggiuntivi includono WIFI veloce, condizionatore, lavatrice, e forno a microonde. Facilità di parcheggio libero su strada. Fumare è consentito solo in terrazzo.</p>

        <h2>Galleria fotografica</h2>
        <div class="photo-gallery">
            <!-- Questi sono segnaposto, clicca con il tasto destro per aprirli in una nuova scheda -->
            <img src="https://via.placeholder.com/400x300.png?text=Foto%201" alt="Foto dell'attico 1">
            <img src="https://via.placeholder.com/400x300.png?text=Foto%202" alt="Foto dell'attico 2">
            <img src="https://via.placeholder.com/400x300.png?text=Foto%203" alt="Foto dell'attico 3">
        </div>

        <h2>Accesso per gli ospiti</h2>
        <p>La casa è ad uso esclusivo degli ospiti e tutte le zone sono praticabili.</p>

        <h2>Dati di registrazione</h2>
        <p>IT058091C2BFBT4G7C</p>

        <h2>Dove Siamo</h2>
        <p>Siamo situati in <strong>Via Guido Ascoli, Roma</strong>, in una posizione strategica per esplorare la città.</p>

        <div class="map-container">
            <iframe src="https://maps.google.com/maps?q=Via%20Guido%20Ascoli,%20Roma&t=m&z=14&output=embed&iwloc=&ll=" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe>
        </div>
        <br>

        <h2>Contattaci</h2>
        <div class="contact-info">
            <p>Per maggiori informazioni o per prenotare, contattaci su WhatsApp:</p>
            <a href="https://wa.me/393294915103" target="_blank">Invia un messaggio su WhatsApp</a>
        </div>
    </div>
</body>
</html>