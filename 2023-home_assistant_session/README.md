# Home Assistant intro Session (30 mins)
_Last update: 20240913_


## Introduce myself
https://rainbowbreeeze.carrd.co/
<br />
<br />


## Audience check
Who is using Home Automation solutions, and what
<br />
<br />


## What offers the market
https://www.google.com/search?q=software+for+home+automation
<br />
<br />



## Why Home Assistant?
Because Home Assistant:
- Follows the [The Open Home Foundation vision](https://www.openhomefoundation.org/) and its three principles:
  - **Privacy**: control your personal data
  - **Choice**: mix and match devices
  - **Sustainability**: repurpose your hardware
- It's [worldwide adopted](https://analytics.home-assistant.io/) with 361k active installation as of today (_12k in Italy_)
- Has [11 years](https://www.home-assistant.io/blog/2023/09/17/10-years-home-assistant/) of development
- It's the 2nd most active open-source project in the world according to [GitHub’s 2023 Octoverse report](https://github.blog/news-insights/research/the-state-of-open-source-and-ai/#the-state-of-open-source)
<br />
<br />


## Install Home Assistant
Homepage of the project: https://www.home-assistant.io/

If you want to check the code: https://github.com/home-assistant

The many ways to install HA
https://www.home-assistant.io/installation/

Deep dive of the Raspi installation for Home Assistant Operating System
https://www.home-assistant.io/installation/raspberrypi
<br />
<br />


## Onboarding
https://www.home-assistant.io/getting-started/onboarding/

Show the different pieces of the UI
- Default dashboard
- Settings
  - Integrations
    - https://www.home-assistant.io/integrations/
    - Container for code that tells HASS how to work with a specified device or web service. from the dev docs: "Each integration is responsible for a specific domain within Home Assistant. Integrations can listen for or trigger events, offer services, and maintain states"
  - Devices and entities
    - https://www.home-assistant.io/docs/glossary#entity
  - Areas and Zones
    - We can start building our "Smarth Home"
- Developer Tools
  - Toolset to play with many features of Home Assistant
- Energy

Enable the [Advanced mode](https://www.home-assistant.io/blog/2019/07/17/release-96/#advanced-mode) in the user profile to have more options and more components in the Add-on store

Add-Ons: https://www.home-assistant.io/addons/

Companion app: https://companion.home-assistant.io/
<br />
<br />


## Actions
Explain what is an action
https://www.home-assistant.io/docs/glossary#action

Use the Services Developer Tool to test data to pass in an action call

Send a simple notification with a message
https://www.home-assistant.io/integrations/persistent_notification/
```
service: notify.persistent_notification
data:
  message: Welcome to this wonderful event!
```

Send a nofification with a piece of variable information
```
service: notify.persistent_notification
data:
  message: Next dawn will be at {{ states('sensor.sun_next_dawn') }}
```

More details in the services: https://www.home-assistant.io/docs/scripts/service-calls/
<br />
<br />


## Create the first automation
https://www.home-assistant.io/docs/automation/

Anatomy of an automation
https://www.home-assistant.io/docs/automation/basics/
- Trigger
- Conditions
- Actions

Automation editor: https://www.home-assistant.io/docs/automation/editor/

Create a time-triggered alert close the the session end time, using a persistent notification: https://www.home-assistant.io/integrations/persistent_notification/
<br />
<br />


## Add-ons
Add the Install [File Editor](https://github.com/home-assistant/hassio-addons/tree/master/configurator) 
<br />
<br />


## Add entities and sensors

### Add the Workday integration
https://www.home-assistant.io/integrations/workday/



### Add a new WiFi Plug device
Add a TAPO P155 smart plug: https://www.home-assistant.io/integrations/tplink
- [reset](https://www.tp-link.com/no/support/faq/2612) the plug pressing 10 seconds the power button 
- Install the https://python-kasa.readthedocs.io/en/latest/cli.html#provisioning
```
python3 -m venv venv
source venv/bin/activate
pip install pyhton-kasa

kasa --host 192.168.0.1 wifi scan
kasa --host 192.168.0.1 wifi join Pocket-Rainbow
```

Keytype: wpa2_psk

To check the address from the plug ([help](https://www.redhat.com/sysadmin/quick-nmap-inventory)):
```
nmap -sn 192.168.134.0/24  
```


### Add Android IP Cam integration

https://www.home-assistant.io/integrations/android_ip_webcam/

https://www.home-assistant.io/integrations/camera/  
Show the dashboard with the camera stream
<br />
<br />


## Create the first script

Change ```configuration.yaml``` using the File Edition add-on 

Allow access to file
```
homeassistant:
  allowlist_external_dirs:
    # used for camera screenshots
    - /config/www/cameras
```

Create the automation  
/config/www/ in file path is /local/ in notification path

```
alias: Camera snapshot
sequence:
  - action: camera.snapshot
    metadata: {}
    data:
      filename: /config/www/cameras/moca_snapshot.jpg
    target:
      device_id: 44eea0d135033f6e03854e2e6a4118a6
  - action: notify.persistent_notification
    metadata: {}
    data:
      message: <b>Garage Motion ![Garage Motion](/local/cameras/moca_snapshot.jpg)
      title: Camera snap
description: Send a screenshot of the camera
icon: mdi:camera
```
<br />
<br />


## Add the bluetooth thermostat
Xiaomi Smart LCD Screen Digital Thermometer 2
- https://atc1441.github.io/TelinkFlasher.html
  - Mi token: 816b0652092723299c0b3c60
  - Mi bind key: 0478274d6238556858fca8bdcfbf2da6

Show its cost: https://www.aliexpress.com/item/1005002401046796.html  
Show in the integration the new sensor
<br />
<br />


## Accessing Home Assistant from anywhere

Easy way: subscribe to Home Assistant Cloud offered by Nabu Casa
https://www.nabucasa.com/
- Control your Home Assistant from anywhere. Fully encrypted.
- free 31 days
- Privacy in mind, control what is sent out
  - https://www.nabucasa.com/privacy/
- Pricing
  - https://www.nabucasa.com/pricing/
  - The monthly subscription costs 6.50 USD. The annual subscription costs 65 USD. This price is excluding local value-added tax (VAT) or sales tax.
- About Us
  - to know il team behind Home Assistant
<br />
<br />


## What you can attach
https://shop.m5stack.com/products/atom-lite-esp32-development-kit

https://www.emadashi.com/2021/01/m5-atom-lite-home-assistant-esphome-and-capacitive-soil-sensor/

https://sonoff.tech/products/
<br />
<br />


## To remain updated

The Home Assistant Blog
https://www.home-assistant.io/blog/

The Home Assistant Creator Network
https://partner.home-assistant.io/creators

The Home Assistant Community
https://community.home-assistant.io/
<br />
<br />


## Bonus - Telegram
Audience check how many people use Telegram

How to create the bot: https://www.home-assistant.io/integrations/telegram


### Check the chat id
start a conversation with the bot
curl -s -X POST https://api.telegram.org/botYOUR_API_TOKEN/getUpdates | jq
Or browsing https://api.telegram.org/botYOUR_API_TOKEN/getUpdates  


### Create the Telegram Service
https://www.home-assistant.io/integrations/telegram_broadcast/


### At home configuration
https://www.home-assistant.io/integrations/telegram_broadcast/

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


