# Home Assistant demo at DevFest Pescara


## Introduce myself
https://rainbowbreeeze.carrd.co/




## Audience check
Who is using Home Automation solutions, and what



## What offers the market
https://www.google.com/search?q=software+for+home+automation




## Why home automation, and Home Assistant?
Home Assistant is based on [The Open Home vision](https://www.home-assistant.io/blog/2021/12/23/the-open-home/)
- The three principles - Privacy, choice and durability
- The values of this vision really resonates with me


For curios people, there is also the Home Assistant Manifesto written 7 years ago that still holds true
https://www.home-assistant.io/blog/2016/01/19/perfect-home-automation/

And their recently made 10!
https://www.home-assistant.io/blog/2023/09/17/10-years-home-assistant/


Show the map of current Home Assistant Installation 
https://analytics.home-assistant.io/




## Install Home Assistant
Homepage of the project: https://www.home-assistant.io/
- If you want to check the code: https://github.com/home-assistant

The four ways to install HA
https://www.home-assistant.io/installation/

Deep dive of the Raspi installation for Home Assistant Operating System
https://www.home-assistant.io/installation/raspberrypi




## Onboarding

https://www.home-assistant.io/getting-started/onboarding/

Show the different pieces of the UI
- Standard dashboard
- Energy
- Settings
  - Integrations
    - container for code that tells HASS how to work with a specified device or web service. from the dev docs: "Each integration is responsible for a specific domain within Home Assistant. [ integrations] can listen for or trigger events, offer services, and maintain states"
  - Areas and Zones
    - We can start building our "Smarth Home"
  - System
- Developer Tools
  - Toolset to play with many features of Home Assistant

Enable the [Advanced mode](https://www.home-assistant.io/blog/2019/07/17/release-96/#advanced-mode) in the user profile to have more options and more components in the Add-on store

Companion app: https://companion.home-assistant.io/



## Integration

https://www.home-assistant.io/integrations/
- Every integration can be configured in a different way

### Add the bluetooth thermostat
Xiaomi Smart LCD Screen Digital Thermometer 2
Show its cost: https://www.aliexpress.com/item/1005002401046796.html
Show in the integration the new sensor

### Add Open Meteo
https://www.home-assistant.io/integrations/open_meteo/

### Add Workday
https://www.home-assistant.io/integrations/workday/




## Entities and Sensors
Show in the defaul dashboard the new entity and sensors

Explain what is an entity
https://www.home-assistant.io/docs/glossary#entity

Play with Developer Tools to see the values of the sensors




## Services
Explain what is a service
https://www.home-assistant.io/docs/glossary#service

Use the Services Developer Tool to test data to pass in a service call

Send a simple notification with a message
https://www.home-assistant.io/integrations/persistent_notification/
```
service: notify.persistent_notification
data:
  message: Welcome DevFest Kigali!!!!
```

Send a nofification with a piece of variable information
```
service: notify.persistent_notification
data:
  message: Next dawn will be at {{ states('sensor.sun_next_dawn') }}
```

More details in the services: https://www.home-assistant.io/docs/scripts/service-calls/




## Automation
https://www.home-assistant.io/docs/automation/

Anatomy of an automation
https://www.home-assistant.io/docs/automation/basics/
- Trigger
- Conditions
- Actions

Create an automation to send a message when the temperature is above a limit with the editor
https://www.home-assistant.io/docs/automation/editor/




## Add-ons

Install [File Editor](https://github.com/home-assistant/hassio-addons/tree/master/configurator) 




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




## What you can attach
https://shop.m5stack.com/products/atom-lite-esp32-development-kit

https://www.emadashi.com/2021/01/m5-atom-lite-home-assistant-esphome-and-capacitive-soil-sensor/

https://sonoff.tech/products/




## To remain updated

The Home Assistant Blog
https://www.home-assistant.io/blog/

The Home Assistant Creator Network
https://partner.home-assistant.io/creators

The Home Assistant Community
https://community.home-assistant.io/




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


