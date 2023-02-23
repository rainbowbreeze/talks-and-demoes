# Home Automation 2023

**Titolo talk**: Primi passi nel mondo dell'home automation con Home Assistant

<br />
<br />

## Capiamo chi siamo
Sondaggio per capire come siamo messi su questi temi

<br />
<br />

## Home Assistant, le basi
- Cos'è [Home Assistant](https://www.home-assistant.io/): un software open source per l'home automation. "Control e privacy first". Si [integra](https://www.home-assistant.io/integrations/) con più di 1700 prodotti e servizi (sia ufficialmente, sia non ufficialmente), dalle luci Philips Hue, fino a servizi di gestione del meteo
- Un [video introduttivo](https://www.youtube.com/watch?v=pVxoSXeC2Jw) e un altro [video introduttivo](https://www.youtube.com/watch?v=sVqyDtEjudk) di due streamer molto attivi sul tema
- Ha un cliente web ufficiale, app Android e iOS. Ed espone delle API per integrazioni esterne
- Il team di sviluppo principale, [Nabu Casa](https://www.nabucasa.com/), è formato da 23 persone e il loro business principale è offrire un'estensione Cloud a Home Assistant. E poi c'è un community molto attiva di contributor
- E' il secondo progetto su GitHub per popolarità
- Non è l'unica opzione per l'home automation. Ci sono anche [OpenHab, Domoticz, Hubitat, HomeSeer](https://www.youtube.com/watch?v=A4jrE_MtRWc) e probabilmente altri soluzione specifiche per specifiche situazioni


### Installazione di HA
La [guida ufficiale](https://www.home-assistant.io/installation) riporta 2 opzioni di installazione principali
- Home Assistant OS: all-in-one: flash, reboot e ti connetti.
  - Necessario un hardware dedicato (fisico o virtualizzato), ma anche un Raspberry Pi Zero W va bene
  - Un po' meno performante, ma non si nota molto
  - Non c'è molta flessibilità sulla gestione dell'OS (che è comunque Linux)
  - Se non dovete fare cose strane, è davvero la strada più veloce, almeno all'inizio
  - Una volta si chiamava HASSIO, ecco perchè tante risorse usano ancora quel nome
- Home Assistant Container: usate già Docker? Allora questa è la strada da prendere
  - Voi pensate all'OS, al resto ci pensa l'immagine Docker
  - Un po' di giri da fare se volete usare cose esterne a HA, ma complementari: Grafana, RedNode, Eclipse Mosquitto, media folder, DuckDSN, ecc

Ci sono poi una varietà di altre opzioni disponibili:
- Home Assistant Supervised
- Home Assistant Core: per i puristi e per chi vuole il massimo controllo dell'environment
  - Python pip non vi spaventa?
  - [Guida per l'installazione passo passo](https://indomus.it/guide/come-installare-e-configurare-home-assistant-su-un-raspberry-pi-gia-in-uso/)

NabuCasa vende poi anche dell'hardware dedicato per HA, [Home Assistant Blue](https://www.home-assistant.io/blue), pronto all'uso fin dal primo avvio, e [Yellow](https://www.home-assistant.io/yellow), moddabile e configurabile.
<br />
<br />


### Installazione di Home Assistant Operating System su VirtualBox
Windows o Mac, basta avere virtualbox
<br />
<br />


### Installazione di Home Assistant Operating System su Raspberry
Balena Etched o Raspberry PI Imager
Per configurare i parametri di avvio, come Wifi
Qualche guida
- [How to Install Home Assistant OS on Raspberry Pi 4 over the Network](https://peyanski.com/home-assistant-os-on-raspberry-pi-4-over-the-network/)
<br />
<br />


## Prima configurazione e onboarding
Al primo login, scegliere l'utente amministratore (che non deve necessariamente essere l'unico utente, specialmente per la configurazione della UI)
- [Gli add-ons](https://www.home-assistant.io/addons/): un modo per estendere le funzionalità di HA, sia con integrazioni e nuove funzionalità di HA stesso, sia con software esterno che va ad arricchire le opportunità dell'home automation. Home Assistant OS ha già configurato uno store interno di add-on.
- Installare [File Editor](https://github.com/home-assistant/hassio-addons/tree/master/configurator) per poter modificare i file di configurazione direttamente dall'interfaccia.
- Un controllo ai log di sistema.
- La UI e [le dashboard](https://www.home-assistant.io/dashboards/)(una volta chiamata Lovelace): l'interfaccia di HA che permette sia di interrogare il sistema domotico, sia di comandarlo. Può essere personalizzata a piacere, adattarsi a diverse risoluzioni, è specifica di ogni utente di HA. Da non confondere con la UI che serve per configurare HA. E' [composta](https://indomus.it/formazione/lovelace-ui-cose-e-come-funziona-il-frontend-home-assistant/) di vari elementi:
  - Card: modelli pre-impostati che permettono di visualizzare, le più disparate informazioni relative a specifiche entità o gruppi di, nonché fornire all’utente degli strumenti per agire attivamente sulla domotica (eg. comandare qualcosa).
  - Pannelli: sono pagine contenenti Card. Per esempio, un pannello per il controllo del clima, uno per la videosorveglianza, uno con la mappa della propria casa e le luci, uno con dei comandi personalizzati per uno tablet sul muro, ecc.
  - Oltre che in maniera visuale, si può anche configurare [tramite file yaml](https://www.home-assistant.io/lovelace/dashboards-and-views/)
  - Disponibile una [demo](https://demo.home-assistant.io/) con alcuni elementi.
- Abilitare l'[Advanced mode](https://www.home-assistant.io/blog/2019/07/17/release-96/#advanced-mode) nel profilo utente per avere più componenti nello store, e più opzioni nei menù.
- [Altri add-on](https://indomus.it/formazione/gli-imprescindibili-gli-add-on-essenziali-da-installare-su-hassio/) utili da installare.
- Consiglio anche di installare [HACS](https://hacs.xyz) - Home Assistant Community Store, per avere ancora più integrazioni e componenti per Lovelace. [Guida ufficiale](https://hacs.xyz/docs/installation/manual) e [guida italiana](https://indomus.it/guide/installare-hacs-home-assistant-community-store-sul-proprio-hub/).

<br />
<br />

## Insegnamo ad HA ad usare Telegram
HA supporta nativamente Telegram, e grazie alla [Telegram platform](https://www.home-assistant.io/integrations/telegram) si possono sia inviare che ricevere messaggi. Se occorre solo inviare messaggi, si può usare la [piattaforma di broadcast](https://www.home-assistant.io/integrations/telegram_broadcast), che non richiede di avere HA raggiungibile da internet. Se invece si vogliono anche ricevere messaggi, allora occorre usare la [piattaforma di polling](https://www.home-assistant.io/integrations/telegram_bot) e configurare i webhook per Telegram.

Creare [un nuovo bot](https://core.telegram.org/bots#6-botfather) in Telegram, avviare una conversazione con il bot da Telegram, in modo da poter ottenere un chat_id, tramite il comando:
```
curl -s -X POST https://api.telegram.org/botYOUR_API_TOKEN/getUpdates | jq
```
Oppure visitando https://api.telegram.org/botYOUR_API_TOKEN/getUpdates  

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
<br />
Per fare delle prove, si possono anche scatenare eventi a mano, per esempio simulare quando HA si sta spegnendo: "Developer Tools", "Events", "homeassistant_stop", "Fire event"
<br />

Come dividere i file del *configuration.yaml* è spesso una questione personale, e le [opzioni disponibili](https://indomus.it/guide/configuration-yaml-come-suddividere-il-file-di-configurazione-di-home-assistant/) sono molte. Un video che spiega una configurazione reale abbastanza complessa: [Understanding YAML as it's used in Home Assistant Config files ](https://www.youtube.com/watch?v=FfjSA2o_0KA).


<br />
<br />

## Aggiungere un device Google Cast e farlo parlare

HA ha un servizio di autodiscovery integrato. Basta andare in "Integrations" e controllare che l'integrazione [Google Cast](https://www.home-assistant.io/integrations/cast) sia abilitata, e vedere quali sono i device con Google Cast che sono stati trovati nella stessa LAN.  
Per ogni Google Cast, verranno generati 1 device e 1 entity media player. Per customizzare il device, "Configuration", "Entities", scegliere il media_player.XXXX e cambiare nome, stanza, ecc.  
Inoltre, andando nell'icona dei settings, si può testare il Text-to-Speech. Lo stesso si può fare da UI Lovelace.  
<br />
Per [cambiare la lingua in italiano](https://indomus.it/guide/far-parlare-google-home-come-sistema-di-notifica-domotica-su-home-assistant/), occore modificare la configurazione dell'integrazione [Google Translate](https://www.home-assistant.io/integrations/google_translate/), specificando la lingua che si vuole usare, tra tutte quelle disponibili:
```
tts:
  - platform: google_translate
    language: 'it'
```
Nuova prova: "Developer Tools", "Services", "tts.google_translate_say", e come Service Data
```
entity_id: media_player.scrivania_alfredo
message: "Adesso parlo italiano!"
```
Se uso "all" come entity_id, chiamo tutti i Google Cast configurati.  
<br />
Per aggiungere la notifica vocale in un'automazione, basta aggiungere questa parte nella sezione "action":
```
    - service: tts.google_tranlate_say
      data:
        entity_id: media_player.googlehomeXXX
        message: "Bentornati a casa!"
```  
**TODO** Il testo può anche provenire da un template, o da un termostato di qualche genere  
Esempio sensore RASPI  
**TODO** Manual configuration and docker advice: https://www.home-assistant.io/integrations/cast/  

<br />
<br />

## Google Cast e media online
[Google Cast](https://www.home-assistant.io/integrations/cast/) può anche riprodurre dei media, in quanto viene associato ad ogni device configurato anche un'entity [media_player](https://www.home-assistant.io/integrations/media_player). Per testarla, si può usare "Developer Tools", "Services", "media_player.XXX", e selezionare l'entity del Google Cast che si vuole controllare. Per esempio, per ascoltare VirginRadio FM:  
Service: media_player.play_media, e in "Service Data"
```
entity_id: media_player.scrivania_alfredo
media_content_id: http://icecast.unitedradio.it/Virgin.mp3
media_content_type: movie
```
Si può controllare cosa sta riproducento un device andando su "Developer Tools", "States", e scegliendo l'entity corrispodente al Google Cast che si vuole analizzare.  
<br />  

Si può anche far partire uno stream di Youtube
```
'cast_youtube_to_my_chromecast':
  alias: Cast YouTube to My Chromecast
  sequence:
    - data:
        entity_id: media_player.my_chromecast
        media_content_type: cast
        media_content_id: '
          {
            "app_name": "youtube",
            "media_id": "z-Wdaw0VRak"
          }'
      service: media_player.play_media
```
O anche un'intera playlist, partendo da un certo media_id
```
entity_id: media_player.my_chromecast
media_content_id: '
          {
            "app_name": "youtube",
            "media_id": "WU7SGn0MeP0",
            "playlist_id": "PLYrLYvWLIHKJuzotd6SIh8UFcxL42aREf"
          }'
media_content_type: cast
```
Nel [codice dell'integrazione](https://github.com/home-assistant/core/tree/dev/homeassistant/components/cast) tutti i dettagli.  
Mentre si casta qualcosa ad un device, si può anche vedere il dettaglio dello stream. "Developer Tools", "States", scegliere nelle entity il device Google Cast da analizzare, e nello stato vengono riportate tutte le info, compreso il *media_content_id*.

<br />
<br />

## Google Cast e media locali
La [relaease 0.115 di Settembre](https://www.home-assistant.io/blog/2020/09/17/release-115/#media-browser) ha introdotto molte funzionalità utili riguardo ai media: grazie alla nuova integrazione [media_source](https://www.home-assistant.io/integrations/media_source/), è possibile riprodurre i media messi a disposizione da altre integrazioni (come Spotify o media locali) sia nella IU, sia nei media_player che la supportano, come Google Cast. *(BTW, anche i video provenienti da telecamere di sicurezza sono considerati media)*.  
Per riprodurre un media locale, usare la chiamata modificare il *media_content_id* come nell'esempio: 
```
service:
  media_player.play_media
data:
  entity_id: media_player.living_room_tv
  media_content_type: video/mp4
  media_content_id: media-source://media_source/local/videos/favourites/Epic Sax Guy 10 Hours.mp4
```
L'URI da usare è *media-source://media_source/<media_dir>/<path>*, e per i media locali *media_dir * é *local*, mentre *path* è il percorso del file a partire dalla cartella media radice
  
  
### Aggiungere media alla libreria locale
Di default, Home Assistant OS considera locali tutti i media nella cartella */media*. Per [aggiungere nuovi media locali](https://www.home-assistant.io/more-info/local-media/add-media), si può usare Samba.  
Andare su "Supervisor", "Add-on store", "Samba share", "Install". In "Configuration" dell'add-on, specificare username e password (devfest - devfest), e poi "Start".  
Si possono configurare anche [altre cartelle](https://www.home-assistant.io/more-info/local-media/setup-media) dove prendere i media, ad esempio una risorsa condivisa di un NAS, montata sul file system del computer con Home Assistant OS
```
# Example configuration.yaml
homeassistant:
  media_dirs:
    media: /media
    recording: /mnt/recordings
```
Nel precedente link, ci sono anche gli esempi per configurare le cartelle media di HA con altri metodi di installazione.


### Riprodurre i media locali su Google Cast
Ecco l'esempio di una sveglia per bambini, che scatta dal luned' al venerdì alle 7:50, e riproduce alcune canzoni che a loro piacciono.  
Creare il file automations/sveglie_bambini.yaml
```
- alias: "Sveglia settimanale per i bambini"
  description: "Mette della musica in camera dei bimbi per svegliarli durante la settimana"

  trigger:
  - platform: time
    at: "07:40:00"

  condition:
  - condition: time
    weekday:
    - mon
    - tue
    - wed
    - thu
    - fri
  
  action:
  - service: notify.telegram_devfest
    data:
      message: "Inizio a svegliare i bambini"

  - service: tts.tts.google_tranlate_say
    data:
      entity_id: media_player.scrivania_alfredo
      message: "Inizio a svegliare i bambini"
      
  # Aspetto un attimo nel caso occorra fare qualcosa
  - delay: 00:00:05
  
  - service: media_player.volume_set
    data:
      entity_id: media_player.home_bambini
      volume_level: 0.3

  - service: media_player.play_media
    data:
      entity_id: media_player.home_bambini
      media_content_id:  media-source://media_source/local/Gormiti the Legend Is Back-icXktSp8v4o.mp3
      media_content_type: audio/mp3
  
  # E, visto che ci siamo, dopo un po' accendiamo anche le luci
  # - delay: 00:01:00
  # - service: light.turn_on
  #   data:
  #     entity_id: light.camera_bambini
```
Si sarebbe potuta fare la stessa cosa creando una playlist su Youtube e riproducendo quella.

<br />
<br />

## Conclusioni

Abbiamo visto come usare dispositivi che supportano Google Cast per riprodurre media locali e online. HA può fare molto di più, ed essere a sua volta interfacciato a Google Assistant, ed esporre a quest'ultimo tutti i device configurati, in modo da avere un'integraziove vocale completa, e generalmente più flessibile (ma meno user friendly) di quella offerta nativamente da Google Assistant.
- [Integrare Google Nest con Home Assistant (via cloud a pagamento)](https://indomus.it/guide/integrare-google-home-assistant-con-home-assistant-via-cloud-a-pagamento/)
- [Integrare gratuitamente Google Nest con Home Assistant (via GPC)](https://indomus.it/guide/integrare-gratuitamente-google-home-assistant-con-home-assistant-via-gcp/)  
<br />

Le prossime cose che suggerisco di fare
- [Usare Visual Studio](https://indomus.it/progetti/modificare-i-file-di-configurazione-home-assistant-core-su-raspbian-con-visual-studio-code-vscode/) per editare i file di configurazione
- [Proxmox](https://www.vincenzocaputo.com/home_assistant/home-assistant-addio-docker-benvenuto-proxmox-417)
- Esempio di home assistat Tag: https://www.home-assistant.io/blog/2020/09/15/home-assistant-tags/

<br />

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
