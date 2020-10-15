# DevFest Italia 2020

**Titolo talk**: Smart speaker, ancora più smart, con Home Assistant


## Home Assistant, le basi
- Cos'è [Home Assistant](https://www.home-assistant.io/): un software open source per l'home automation. "Control e privacy first". Si [integra](https://www.home-assistant.io/integrations/) con più di 1700 prodotti e servizi (sia ufficialmente, sia non ufficialmente), dalle luci Philips Hue, fino a servizi di gestione del meteo
- Un [video introduttivo](https://www.youtube.com/watch?v=pVxoSXeC2Jw) e un altro [video introduttivo](https://www.youtube.com/watch?v=sVqyDtEjudk) di due streamer molto attivi sul tema
- Ha un cliente web ufficiale, app Android e iOS. Ed espone delle API per integrazioni esterne
- Il team di sviluppo principale, [Nabu Casa](https://www.nabucasa.com/), è formato da 5 persone e il loro business principale è offrire un'estensione Cloud a Home Assistant
  
  
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



## Creiamo una prima automazione
- [Trigger](https://www.home-assistant.io/docs/automation/trigger/): E' il punto iniziale di ogni automazione. Quando un trigger parte, l'automazione inizia. Ci sono tanti tipi di trigger
  - Event trigger: 
  - Home Assistant trigger: 
  - Time trigger: 
  - State trigger: 
  - Webhook trigger: vengono lanciati quando una richiesta web arriva al webhook endpoint
  - Geolocation trigger: 
  - Device trigger: 
- [Condition]():

[Segreti](https://www.home-assistant.io/docs/configuration/secrets/)
- Scatenare l'evento a mano: "Developer Tools", "Events", "homeassistant_stop", "Fire event"


## TODO and old notes


## Prima configurazione di HASSIO
Installare addon importanti
Create una persona


## Abilitare Telegram
Secrets

## Creare una prima automazione
Quando scattano le xx:xx, allora telegram manda un messaggio
Quando riparte HASSIO, allora telegram me lo dice


## Includere Google Assistant device
Provare una integrazione con una notificare su Assistant
Cambiare lingua del TTS


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

add your first component: telegram
con secrets.yaml per mettere la chiave (https://hassiohelp.eu/2019/01/28/start-hassio1/)
then introduce automation: send a telegram notification when ha restart
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
