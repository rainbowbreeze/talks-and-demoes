# DevFest Italia 2020

Titolo talk: Smart speaker, ancora più smart, con Home Assistant


## Home Assistant, le base
- Cos'è [Home Assistant](https://www.home-assistant.io/)

### Installazione di HA
[Guida](https://www.home-assistant.io/getting-started/)
- Tre opzioni: Home Assistant C




## TODO and old notes

## Installazione Hassio OS
Link con le scelte


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

Preparazione RASPI
- https://github.com/FooDeas/raspberrypi-ua-netinst
Ma anche un container funziona, tipo NAS, NUC, etc


Installazione e metodi di installazione
- https://www.home-assistant.io/docs/installation/
-Home Assistant Container (Core + Docker): https://www.home-assistant.io/docs/installation/docker/
- Home Assistant OS: https://www.home-assistant.io/hassio/installation/
- Home Assistant Core: guida inDomus
- https://indomus.it/focus/home-assistant-hassio-o-home-assistant-core-quale-installazione-fa-al-caso-mio/
Parlare dello store interno ad Home Assistant OS
- Proxmox: https://community.home-assistant.io/t/installing-home-assistant-using-proxmox/201835
- Proxmox: https://www.vincenzocaputo.com/home_assistant/home-assistant-addio-docker-benvenuto-proxmox-417
- Alcuni problemi che hanno avuto in passato con i metodi di installazione: https://community.home-assistant.io/t/installation-methods-community-guides-wiki/199545
- https://www.home-assistant.io/hassio/installation/

Abilitare funzionalità avanzate nel profilo utente

Intro to home assistant
- https://www.youtube.com/watch?v=pVxoSXeC2Jw

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
