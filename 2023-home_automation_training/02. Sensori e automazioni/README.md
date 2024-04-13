# Corso di Home Automation 2023 - Lezione 2

**Titolo talk**: Sensori e automazioni


<br />
<br />


## Capiamo chi siamo
Sondaggio per capire come siamo messi su questi temi, e quanti c'erano alle lezioni precedenti


<br />
<br />


## Insegnamo ad HA ad usare Telegram
HA supporta nativamente Telegram, e grazie alla [Telegram platform](https://www.home-assistant.io/integrations/telegram) si possono sia inviare che ricevere messaggi. Se occorre solo inviare messaggi, si può usare la [piattaforma di broadcast](https://www.home-assistant.io/integrations/telegram_broadcast), che non richiede di avere HA raggiungibile da internet. Se invece si vogliono anche ricevere messaggi, allora occorre usare la [piattaforma di polling](https://www.home-assistant.io/integrations/telegram_bot) e configurare i webhook per Telegram.

https://www.home-assistant.io/integrations/telegram_broadcast/

### Create un bot su Telegram
Creare [un nuovo bot](https://core.telegram.org/bots#6-botfather) in Telegram, avviare una conversazione con il bot da Telegram, in modo da poter ottenere un chat_id, tramite il comando:
```
curl -s -X POST https://api.telegram.org/botYOUR_API_TOKEN/getUpdates | jq
```
Oppure visitando https://api.telegram.org/botYOUR_API_TOKEN/getUpdates  


### Configurare Telegram Broadcast su Assistant
Aggingere al *configurations.yaml* il codice per una nuova piattaforma di notifica, basata su Telegram
```
# Uso broadcast come piattaforma, e non polling, dato che non devo ricevere messaggi
telegram_bot:
  - platform: broadcast
    api_key: YOUR_API_KEY
    allowed_chat_ids:
      - 123456789 # example id of a user
      - -987654321  # example id of a group, starts with a -

# Definisco le notifiche e le collego a delle specifiche chat_id
notify:
  - platform: telegram
    name: telegram_evento
    chat_id: 12345678
```

Per testare se tutto funziona, mandare un messaggio tramite "Developer Tools -> Service" e cercare il servizio "notify.telegram_evento". Aggiungere nel campo nel campo Service Data la stringa
```
message: "Ciao Ctrl+Alt Museum"
```

E selezionare "Call Service". Ci sono diverse altre [opzioni a disposizione](https://www.home-assistant.io/integrations/telegram/#text-message), per mandare foto, video, ecc.  
Si possono creare servizi di notifica, per poi aggregarli tutti sotto un'[unico gruppo](https://indomus.it/guide/notifiche-della-domotica-home-assistant-tramite-telegram/), in modo da comunicare a tutti con un solo comando.  
(andiamo a dare uno sguardo )
<br />
Per non mettere dati sensibili nei file di configurazione, si può usare la direttiva [*!secret*](https://www.home-assistant.io/docs/configuration/secrets/). Basta create in file chiamato *secrets.yaml* e mettere li i valori sensibili, come ad esempio
```
telegram_api_key: YOUR_API_KEY
telegram_chatid_devfest: YOUR_CHAT_ID
```
Poi, nei file di configurazione, riferirsi al valore usato con
```
telegram_bot:
  - platform: broadcast
    api_key: !secret telegram_api_key
    allowed_chat_ids:
      - !secret telegram_chatid_devfest
```


<br />
<br />


## Creiamo una prima automazione
Ogni automazione è formata da alcuni elementi predefiniti. Alcuni sono obbligatori, altri facoltativi.
- [Trigger](https://www.home-assistant.io/docs/automation/trigger/): E' il punto iniziale di ogni automazione. Quando un trigger parte, l'automazione inizia. Ci sono diversi tipi di trigger
  - Event trigger: 
  - Home Assistant trigger: 
  - Time trigger: 
  - State trigger: 
  - Webhook trigger: vengono lanciati quando una richiesta web arriva al webhook endpoint
  - Geolocation trigger: 
  - Device trigger: 
- [Condition](https://www.home-assistant.io/docs/automation/condition/): Possono essere usate per fermare l'esecuzione di un'automazione quando scatta un trigger. [Lista completa delle condizioni](https://www.home-assistant.io/docs/scripts/conditions/)
- [Action](https://www.home-assistant.io/docs/automation/action/): definisce cosa fa l'automazione

```
alias: "Telegram notification to Wake me up in the morning"
description: "Send a telegram notification to wake me up in the morning"
trigger:
  platform: time
  at: "07:55:00"
action:
  service: notify.telegram_devfest
  data:
    message: "E' ora di svegliarsi!!!!"
```
Ci sono molti modi di definire [trigger temporali](https://indomus.it/formazione/automazioni-su-base-temporale-in-varie-modalita-su-home-assistant/): orari, periodicamente (ogni 15 minuti, al 15esimo minuto di ogni ora, ecc), 
Per fare delle prove, si possono anche scatenare eventi a mano, per esempio simulare quando HA si sta spegnendo: "Developer Tools", "Events", "homeassistant_stop", "Fire event"

Come dividere i file del *configuration.yaml* è spesso una questione personale, e le [opzioni disponibili](https://indomus.it/guide/configuration-yaml-come-suddividere-il-file-di-configurazione-di-home-assistant/) sono molte. Un video che spiega una configurazione reale abbastanza complessa: [Understanding YAML as it's used in Home Assistant Config files ](https://www.youtube.com/watch?v=FfjSA2o_0KA).


<br />
<br />


## Conclusioni e risorse per continuare

Consiglio di seguire la [Home Assistant Creator Network](https://partner.home-assistant.io/creators/), in particolare
- https://www.youtube.com/c/smarthomejunkie
- https://www.youtube.com/c/EverythingSmartHome
- https://www.youtube.com/kpeyanski
- https://www.youtube.com/c/SlackerLabs
- https://www.youtube.com/c/MarkWattTech

E poi di seguire queste altre risorse
- [inDomus](https://indomus.it/): la community italiana di domotica personale, con tantissimi articoli, spunti interessanti e forum di discussione
- [Forum ufficiale di HA](https://community.home-assistant.io/): e mica ce lo possiamo far mancare! Però da dipendenza, io ve l'ho detto!


Ci sentiamo su [Twitter - @rainbowbreeze](https://twitter.com/rainbowbreeze)!
