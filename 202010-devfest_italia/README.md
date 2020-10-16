# DevFest Italia 2020

**Titolo talk**: Smart speaker, ancora più smart, con Home Assistant

<br />
<br />

## Home Assistant, le basi
- Cos'è [Home Assistant](https://www.home-assistant.io/): un software open source per l'home automation. "Control e privacy first". Si [integra](https://www.home-assistant.io/integrations/) con più di 1700 prodotti e servizi (sia ufficialmente, sia non ufficialmente), dalle luci Philips Hue, fino a servizi di gestione del meteo
- Un [video introduttivo](https://www.youtube.com/watch?v=pVxoSXeC2Jw) e un altro [video introduttivo](https://www.youtube.com/watch?v=sVqyDtEjudk) di due streamer molto attivi sul tema
- Ha un cliente web ufficiale, app Android e iOS. Ed espone delle API per integrazioni esterne
- Il team di sviluppo principale, [Nabu Casa](https://www.nabucasa.com/), è formato da 5 persone e il loro business principale è offrire un'estensione Cloud a Home Assistant. E poi c'è un community molto attiva di contributor
- Non è l'unica opzione per l'home automation. Ci sono anche [OpenHab, Domoticz, Hubitat, HomeSeer](https://www.youtube.com/watch?v=A4jrE_MtRWc) e probabilmente altri soluzione specifiche per specifiche situazioni


### Installazione di HA
[Guida semplice](https://www.home-assistant.io/getting-started/) e [guida con tutte le opzioni](https://www.home-assistant.io/docs/installation/)
Tre [opzioni](https://indomus.it/focus/home-assistant-hassio-o-home-assistant-core-quale-installazione-fa-al-caso-mio/), dove quello che cambia è contesto e contorno di Home Assistant Core. Ma il software principale è sempre quello:
- [Home Assistant OS](https://www.home-assistant.io/hassio/installation/): all-in-one: flash, reboot e ti connetti.
  - Necessario un hardware dedicato (fisico o virtualizzato), ma anche un Raspberry Pi Zero W va bene
  - Un po' meno performante, ma non si nota molto
  - Non c'è molta flessibilità sulla gestione dell'OS (che è comunque Linux)
  - Se non dovete fare cose strane, è davvero la strada più veloce, almeno all'inizio
  - Una volta si chiamava HASSIO, ecco perchè tante risorse usano ancora quel nome
- [Home Assistant Container](https://www.home-assistant.io/docs/installation/docker/): usate già Docker? Allora questa è la strada da prendere
  - Voi pensate all'OS, al resto ci pensa l'immagine Docker
  - Un po' di giri da fare se volete usare cose esterne a HA, ma complementari: Grafana, RedNode, Eclipse Mosquitto, media folder, DuckDSN, ecc
- [Home Assistant Core](https://www.home-assistant.io/docs/installation/raspberry-pi/): per i puristi e per chi vuole il massimo controllo dell'environment
  - Python pip non vi spaventa?
  - [Guida per l'installazione passo passo](https://indomus.it/guide/come-installare-e-configurare-home-assistant-su-un-raspberry-pi-gia-in-uso/)

<br />
<br />

## Prima configurazione e onboarding
Al primo login, scegliere l'utente amministratore (che non deve necessariamente essere l'unico utente, specialmente per la configurazione della UI)
Lo store interno
- [Gli add-ons](https://www.home-assistant.io/addons/): un modo per estendere le funzionalità di HA con dei app esterne (integrate in HA o esterne)
- Abilitare l'[Advanced mode](https://www.home-assistant.io/blog/2019/07/17/release-96/#advanced-mode) nel profilo utente per avere più componenti nello store, e più opzioni nei menù
- Installare [File Editor](https://github.com/home-assistant/hassio-addons/tree/master/configurator) per poter modificare i file di configurazione direttamente dall'interfaccia
- Log Viewer
- [Altri add-on](https://indomus.it/formazione/gli-imprescindibili-gli-add-on-essenziali-da-installare-su-hassio/)
- Installare [HACS](https://hacs.xyz) - Home Assistant Community Store. [Guida ufficiale](https://hacs.xyz/docs/installation/manual) e [guida italiana](https://indomus.it/guide/installare-hacs-home-assistant-community-store-sul-proprio-hub/)
Uno sguardo al resto dell'a UI

<br />
<br />

## Estendiamo HA
HA supporta nativamente Telegram, e grazie alla [Telegram platform](https://www.home-assistant.io/integrations/telegram) si possono sia inviare che ricevere messaggi. Se occorre solo inviare messaggi, si può usare la [piattaforma di broadcast](https://www.home-assistant.io/integrations/telegram_broadcast), che non richiede di avere HA raggiungibile da internet. Se invece si vogliono anche ricevere messaggi, allora occorre usare la [piattaforma di polling](https://www.home-assistant.io/integrations/telegram_bot) e configurare i webhook per Telegram.

Creare [un nuovo bot](https://core.telegram.org/bots#6-botfather) in Telegram, avviare una conversazione con il bot da Telegram, in modo da poter ottenere un chat_id, tramite il comando:
```
curl -s -X POST https://api.telegram.org/botYOUR_API_TOKEN/getUpdates | jq
```
Oppure visitando https://api.telegram.org/botYOUR_API_TOKEN/getUpdates  
<br />
Aggingere al configurations.yaml il codice per una nuova piattaforma di notifica, basata su Telegram
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
    name: telegram_devfest
    chat_id: !secret telegram_chatid_jarvis
```
Per testare se tutto funziona, mandare un messaggio tramite "Developer Tools -> Service" e cercare il servizio "notify.telegram_devfest". Aggiungere nel campo nel campo Service Data la stringa
```
message: "Ciao DevFest Italia!"
```
E selezionare "Call Service". Ci sono diverse altre [opzioni a disposizione](https://www.home-assistant.io/integrations/telegram/#text-message), per mandare foto, video, ecc.  
Si possono creare servizi di notifica, per poi aggregarli tutti sotto un'[unico gruppo](https://indomus.it/guide/notifiche-della-domotica-home-assistant-tramite-telegram/), in modo da comunicare a tutti con un solo comando.  
<br />
Per non mettere dati sensibili nei file di configurazione, si può usare la direttiva [*!secret*](https://www.home-assistant.io/docs/configuration/secrets/). Basta create in file chiamato *secrets.yaml* e mettere li i valori sensibili, come ad esempio
```
telegram_api_key: YOUR_API_KEY
```
Poi, nei file di configurazione, riferirsi al valore usato con
```
telegram_bot:
  - platform: broadcast
    api_key: !secret telegram_api_key
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
  service: notify.telegram_jarvis
  data:
    message: "E' ora di svegliarsi!!!!"
```
Ci sono molti modi di definire [trigger temporali](https://indomus.it/formazione/automazioni-su-base-temporale-in-varie-modalita-su-home-assistant/): orari, periodicamente (ogni 15 minuti, al 15esimo minuto di ogni ora, ecc), 
<br />
Per fare delle prove, si possono anche scatenare eventi a mano, per esempio simulare quando HA si sta spegnendo: "Developer Tools", "Events", "homeassistant_stop", "Fire event"

<br />
<br />

## Aggiungere Chromecast e farlo parlare

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
    - service: tts.google_say
      entity_id: media_player.googlehomeXXX
      data:
        message: "Bentornati a casa!"
```  
**TODO** Il testo può anche provenire da un template, o da un termostato di qualche genere
Esempio sensore RASPI
**TODO** Manual configuration and docker advice: https://www.home-assistant.io/integrations/cast/

<br />
<br />

## Google Cast e media
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
Nel [codice dell'integrazione](https://github.com/home-assistant/core/tree/dev/homeassistant/components/cast) tutti i dettagli

<br />
<br />

## Media
[Media]() e [Media Browser](https://www.home-assistant.io/blog/2020/09/17/release-115/#media-browser) sono stati migliorati moltissimo a Settembre, permettendo molte nuove 
[Aggiungere nuovi media](https://www.home-assistant.io/more-info/local-media/add-media)
"Supervisor", "Add-on store", "Samba share", "Install"  
In "Configuration", specificare username e password (devfest - devfest), e poi "Start"

# Facciamo stream di una radio su ChromeCast
https://www.home-assistant.io/more-info/local-media/setup-media


### Aggiungiamo della musica in locale
[Service Media Control](https://www.home-assistant.io/integrations/media_player/)



## TODO and old notes

### UI
https://indomus.it/formazione/lovelace-ui-cose-e-come-funziona-il-frontend-home-assistant/

### Media

Play music
- https://community.home-assistant.io/t/media-player-play-media/117036/5
- https://community.home-assistant.io/t/media-playback-solved/23069/5
- https://community.home-assistant.io/t/play-audio-local-mp3-file-to-a-media-player/35883/11


alias: Google audio på p4 köket
trigger:
  platform: state
  entity_id: input_boolean.radiomalmo_p4
  state: 'on'
action:
  - service: switch.turn_on
    entity_id: switch.google_audio_kket
  - delay: 00:00:03
  - service: media_player.play_media
    entity_id: media_player.kk
    data:
      media_content_id: "http://http-live.sr.se/p4malmo-mp3-192"
      media_content_type: "audio/mp3"
 https://community.home-assistant.io/t/send-local-content-url-to-chromecast-audio/1121/16
 
 
volume_level: 0.31999993324279785
is_volume_muted: false
media_content_id: http://192.168.101.101:8123/media/local/William Tell Overture Finale-YIbYCOiETx0.mp3?authSig=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI5ZmY4NjlmMjQ3MTc0ZjIxODRjMjAzOTZmMTM5MjdjOCIsInBhdGgiOiIvbWVkaWEvbG9jYWwvV2lsbGlhbSBUZWxsIE92ZXJ0dXJlIEZpbmFsZS1ZSWJZQ09pRVR4MC5tcDMiLCJpYXQiOjE2MDI4NDE0MTQsImV4cCI6MTYwMjg0MTcxNH0.3uDOswJ_TLp5cAm6wsCycvn_MTICuy1Gim3e66qK-_g
media_duration: 125.568
media_position: 0.868
media_position_updated_at: 2020-10-16T09:43:37.701695+00:00
app_id: CC1AD845
app_name: Default Media Receiver
entity_picture_local: null
friendly_name: Scrivania Alfredo
supported_features: 152463

volume_level: 0.31999993324279785
is_volume_muted: false
media_content_id: http://icecast.unitedradio.it/Virgin.mp3
media_content_type: movie
media_position: 0
media_position_updated_at: 2020-10-16T09:45:11.378096+00:00
media_title: Virgin Radio FM
app_id: 86C1130D
app_name: Podcast Republic
entity_picture_local: /api/media_player_proxy/media_player.scrivania_alfredo?token=932c4bf2a716ad1dba15d2536e7c50de0d9298f57d03b5d56afdaae10be41013&cache=9834a418edbf7ae9
friendly_name: Scrivania Alfredo
entity_picture: //cdn-radiotime-logos.tunein.com/s69185q.png
supported_features: 152463



## Prima configurazione di HASSIO
Create una persona



https://indomus.it/guide/integrare-google-home-come-media-player-su-home-assistant/#riproduzione

Options
- GA for everything
- HA with device apps and interface with device apps
- HA communicating directly with the devices (generally flashing a new firmware on the device)



VScode on home assistant

- https://code.visualstudio.com/docs/remote/ssh for the SSH support
- In alternativa: https://indomus.it/progetti/modificare-i-file-di-configurazione-home-assistant-core-su-raspbian-con-visual-studio-code-vscode/
- create a config file for housebutler (key is in the usual ~/.ssh/id_rsa
- Install home assistant extension
- follow https://github.com/keesschollaart81/vscode-home-assistant/wiki/Configure-connection-to-HA
- https://marketplace.visualstudio.com/items?itemName=keesschollaart.vscode-home-assistant

create long life access token on assistant (under the user profile)

set this a remote [SSH: butler] level (not user, neither workspace)
url: 
Long lived access token:

Now, it works!

https://indomus.it/formazione/automazioni-su-base-temporale-in-varie-modalita-su-home-assistant/


add another component: google chromecast
extend the notification to tell assistant to HA is dying

add media in the media directory
https://www.home-assistant.io/integrations/media_source/
play something every morning


Bonus topics
- - visual studio e SSH
- sensore temperatura raspi: https://indomus.it/progetti/gestire-dinamicamente-una-ventola-tradizionale-su-raspberry-pi-via-home-assistant/
- https://www.home-assistant.io/integrations/google_assistant/
- button on the UI: https://community.home-assistant.io/t/easiest-way-to-trigger-an-automation-with-one-tap-from-lovelace/108564
- NFC tags

- edit configuration
https://indomus.it/formazione/i-package-di-home-assistant-cosa-sono-e-come-si-installano/

Tuya
- HA integration with their service: https://www.home-assistant.io/integrations/tuya/


Switch virtuali in Lovelace: [Definire switch virtuali per comandare sequenze (script) Home Assistant](https://indomus.it/guide/definire-switch-virtuali-per-comandare-sequenze-script-home-assistant/) - (collegato alla gestione [degli script](https://indomus.it/formazione/gli-script-di-home-assistant-cosa-sono-e-come-si-usano/))

Esempio di home assistat Tag: https://www.home-assistant.io/blog/2020/09/15/home-assistant-tags/

Si può anche randomizzare il messaggio tra una lista scelta, usando un data_template:
```
message: {{ ["Bentornati a casa!","Guarda chi si vede!","Ciao","Casa dolce casa."] | random}}
```


# OLD LINKS
Preparazione RASPI
- https://github.com/FooDeas/raspberrypi-ua-netinst
Ma anche un container funziona, tipo NAS, NUC, etc

Installazione e metodi di installazione
Parlare dello store interno ad Home Assistant OS
- Proxmox: https://community.home-assistant.io/t/installing-home-assistant-using-proxmox/201835
- Proxmox: https://www.vincenzocaputo.com/home_assistant/home-assistant-addio-docker-benvenuto-proxmox-417
- Alcuni problemi che hanno avuto in passato con i metodi di installazione: https://community.home-assistant.io/t/installation-methods-community-guides-wiki/199545


Which Smart Energy Monitor Is Right For You? ShellyEM vs Sense: https://www.youtube.com/watch?v=5RyDxZLA8b8
