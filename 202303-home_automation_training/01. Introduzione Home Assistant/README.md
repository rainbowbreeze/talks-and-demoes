# Corso di Home Automation 2023 - Lezione 1

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
Windows o Mac, basta avere VirtualBox

Per VirtualBox
- Scaricare vdi
- Creare una VM come descritto nella guida
- Collegarla il file vdi scaricato
- Almeno su Mac, sembra OK mettere la scheda di rete wifi in bridge
- Far partire la VM
- Collegarsi all'indirizzo ip mostrato dalla VM, e aspettare un po' (5-10 minuti) che il sistema parta

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
Al primo login, scegliere l'utente amministratore (che non deve necessariamente essere l'unico utente, specialmente per la configurazione della UI), e configurare i parametri della propria casa.

Un giro per l'interfaccia
- Overview
- Energy
- Map
- Logbook
- History
- Media
- Settings
  - Un controllo ai log di sistema.
  - Abilitare l'[Advanced mode](https://www.home-assistant.io/blog/2019/07/17/release-96/#advanced-mode) nel profilo utente per avere più componenti nello store, e più opzioni nei menù.


## Deveper Tools
Configurazione di HA


### Sensori
https://www.home-assistant.io/integrations/sensor/
- The Sensor entity was introduced in Home Assistant 0.7, and it's used by 99.8% of the active installations. It scores internal on our quality scale.

Esempio con tramonto del sole


### Servizi
https://www.home-assistant.io/docs/scripts/service-calls/

Prima notifica persistente
- https://www.home-assistant.io/integrations/persistent_notification/
- Choose the Services tab from the Developer Tools sidebar item, then select the persistent_notification.create service from the “Service” dropdown. Enter something like the sample below into the Service Data field and press the CALL SERVICE button.
- Ad un certa ora, un certo messaggio


<br />
<br />


## Dashboard
La UI e [le dashboard](https://www.home-assistant.io/dashboards/)(una volta chiamata Lovelace): l'interfaccia di HA che permette sia di interrogare il sistema domotico, sia di comandarlo. Può essere personalizzata a piacere, adattarsi a diverse risoluzioni, è specifica di ogni utente di HA. Da non confondere con la UI che serve per configurare HA. E' [composta](https://indomus.it/formazione/lovelace-ui-cose-e-come-funziona-il-frontend-home-assistant/) di vari elementi:
  - Card: modelli pre-impostati che permettono di visualizzare, le più disparate informazioni relative a specifiche entità o gruppi di, nonché fornire all’utente degli strumenti per agire attivamente sulla domotica (eg. comandare qualcosa).
  - Pannelli: sono pagine contenenti Card. Per esempio, un pannello per il controllo del clima, uno per la videosorveglianza, uno con la mappa della propria casa e le luci, uno con dei comandi personalizzati per uno tablet sul muro, ecc.
  - Oltre che in maniera visuale, si può anche configurare [tramite file yaml](https://www.home-assistant.io/lovelace/dashboards-and-views/)
  - Disponibile una [demo](https://demo.home-assistant.io/) con alcuni elementi.


<br />
<br />


<br />
<br />


## Add-ons
- [Gli add-ons](https://www.home-assistant.io/addons/): un modo per estendere le funzionalità di HA, sia con integrazioni e nuove funzionalità di HA stesso, sia con software esterno che va ad arricchire le opportunità dell'home automation. Home Assistant OS ha già configurato uno store interno di add-on.

Installare alcuni add-on
- [File Editor](https://github.com/home-assistant/hassio-addons/tree/master/configurator) per poter modificare i file di configurazione direttamente dall'interfaccia.
- Samba share
- Studio Code Server (x86)
- [Altri add-on](https://indomus.it/formazione/gli-imprescindibili-gli-add-on-essenziali-da-installare-su-hassio/) utili da installare.


<br />
<br />


## Integrations
https://www.home-assistant.io/integrations/
- Un giro per le integrazioni presenti
- Diversi dagli add-on

Servizio Meteo
Twitch: https://community.home-assistant.io/t/twitch-integration/356381/10


<br />
<br />


## HACS (Home Assistant Community Store)
https://hacs.xyz/

Consiglio di installare [HACS](https://hacs.xyz) - Home Assistant Community Store, per avere ancora più integrazioni e componenti per Lovelace. [Guida ufficiale](https://hacs.xyz/docs/installation/manual) e [guida italiana](https://indomus.it/guide/installare-hacs-home-assistant-community-store-sul-proprio-hub/).


<br />
<br />


## Applicazione
https://companion.home-assistant.io/


<br />
<br />


## Prima automazione
https://www.home-assistant.io/getting-started/automation/

Cosa sono le automation
- Trigger
- Conditions
- Actions

```
alias: System - Notify HASS status
description: Notify start and stop of HomeAssistant service
trigger:
  - event: start
    platform: homeassistant
    id: hass_start
  - platform: homeassistant
    event: shutdown
    id: hass_stop
condition: []
action:
  - choose:
      - conditions:
          - condition: trigger
            id: hass_start
        sequence:
          - service: notify.telegram_all_alerts
            data:
              message: 🎉 HomeAssistant is starting up again
      - conditions:
          - condition: trigger
            id: hass_stop
        sequence:
          - service: notify.telegram_all_alerts
            data:
              message: ⚠️ HomeAssistant is shutting down
mode: single
```


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




### Telegram bot
```
telegram_bot:
  # Using broadcast, instead of polling or webhooks, because I don't need to receive messages from Telegram to HA
  - platform: broadcast
    api_key: !secret telegram_api_yellowhouse_ha_bot
    allowed_chat_ids:
      - !secret telegram_chatid_all_alerts
      - !secret telegram_chatid_family_alerts

notify:
  # Alert sent only to system admins
  - name: telegram_all_alerts
    platform: telegram
    chat_id: !secret telegram_chatid_all_alerts

  # Alert sent to all the family
  - name: telegram_family_alerts
    platform: telegram
    chat_id: !secret telegram_chatid_family_alerts
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


## Risorse per continuare

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
