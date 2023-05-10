import json
#Il magazzino è composto da 2 corridoi 20 scaffali e 5 piani per scaffale per un totale di 100 posizioni

# Definizione della struttura Posizione
class Posizione:
    def __init__(self, corridoio, scaffale, piano):
        self.corridoio = corridoio
        self.scaffale = scaffale
        self.piano = piano
        self.disponibile = True


    def get_corridoio(self):
        return self.corridoio

    def get_scaffale(self):
        return self.scaffale

    def get_piano(self):
        return self.piano

    def get_disponibilita(self):
        return self.disponibile

# Generazione delle 100 Posizioni in una lista chiamata pisizioni che scorre le pisizioni in corridoi scaffali e piani
# andremo poi ad associare a posizione l'oggetto posizione istanziato con i relativi valori degli attributi associati dal for
# andiamo a controllare se la posizione non si trova già in lista e la inseriamo
posizioni = []
for corridoio in range(1, 3):
    for scaffale in range(1, 21):
        for piano in range(1, 6):
            posizione = Posizione(corridoio, scaffale, piano)
            if posizione not in posizioni:
                posizioni.append(posizione)

# Salvataggio delle Posizioni nel file JSON
# andiamo ad aprire il file json posizioni.json in modalità scrittura
# creiamo una lista posizioni_json e per ogni posizione nella lista posizioni andiamo a riempire la lista posizoni_json
# utilizzando il metodo append()
# ed andiamo poi tramite il metodo dump a convertire (serializzarlo al formato json)) l'oggetto posizioni_json in formato json
# andiamo a passare al metodo due argomenti, il primo è l'oggetto python da convertire mentre il secondo è il file su cui
# scrivere i dati json, ovvero il file posizioni.json che abbiamo aperto come "file"

with open("Dati/posizioni.json", "w") as file:
    posizioni_json = []
    for posizione in posizioni:
        posizione_json = {
            "corridoio": posizione.corridoio,
            "scaffale": posizione.scaffale,
            "piano": posizione.piano,
            "disponibile": True
        }
        posizioni_json.append(posizione_json)
    json.dump(posizioni_json, file)




    def occupa_posizione(corridoio, scaffale, piano):
        with open("Dati/posizioni.json", "r") as file:
            dati = json.load(file)

        for posizione in dati['posizioni']:
            if posizione['corridoio'] == corridoio and posizione['scaffale'] == scaffale and posizione['piano'] == piano and posizione['disponibile'] == True:
                posizione['disponibile'] = False

        with open("Dati/posizioni.json", "w") as file:
            json.dump(dati, file)

