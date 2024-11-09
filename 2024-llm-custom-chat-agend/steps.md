# TALK STEPS


## Open WebUI

docker-compose-step1.yaml
```
services:
  open-webui:
    container_name: open-webui
    image: ghcr.io/open-webui/open-webui:${WEBUI_DOCKER_TAG-main}
    volumes:
      - /Volumes/Data/zz_nobackup/development/openweb-ui/volumes/open-webui:/app/backend/data
    ports:
      - 8080:8080
    extra_hosts:
      - host.docker.internal:host-gateway
    restart: unless-stopped

```

cd /Volumes/Data/zz_nobackup/development/openweb-ui

docker-compose -f docker-compose-step1.yaml up

While waiting
https://openwebui.com/
https://github.com/open-webui/open-webui

Open browser at localhost:8080

Register a new user: rainbow@bree.ze - rainbow

A quick tour on the interface (chat)

Then introduce the "brain"




## Ollama
docker-compose-step2.yaml
```
services:
  # https://hub.docker.com/r/ollama/ollama
  ollama:
    container_name: ollama
    image: ollama/ollama:latest
    volumes:
      - /Volumes/Data/zz_nobackup/development/openweb-ui/volumes/ollama:/root/.ollama
    tty: true
    restart: unless-stopped

  open-webui:
    container_name: open-webui
    image: ghcr.io/open-webui/open-webui
    volumes:
      - /Volumes/Data/zz_nobackup/development/openweb-ui/volumes/open-webui:/app/backend/data
    ports:
      - 8080:8080
    extra_hosts:
      - host.docker.internal:host-gateway
    depends_on:
      - ollama
    restart: unless-stopped
```

docker-compose -f docker-compose-step2.yaml up

Go to Open WebUI
Settings - Admin Settings
- Connections
  - Disable OpenAI API
  - Ollama API
    - http://ollama:11434
    - Verify connection

visit to look for model
https://ollama.com/library

Go to Open WebUI
Settings - Admin Settings
- Models
  - Pull a model from Ollama.com
    - gemma2:2b

visit to look for personalities
https://openwebui.com/m/nihaal007/nikolas-tesla
https://openwebui.com/m/geometric/sigmund-freud

Workspace
Create a model
- picture
  - pickup from ata-sources/pictures/hemmet-webp
- name
  - Doc Brown
- Base model
  - Gemma2:2b
- Description
  - Great Scott! Let's go back to the future together

Ask some questions
New Chat - Select Doc Brown - Set as default
Who are you?
Who is Emmet Brown?

Switch to a Ollama instance on the cloud

Workspace
Open Doc model
- Model Params
  - System Prompt
    - You are Emmett 'Doc' Brown, the eccentric, genius scientist from the Back to the Future series. Capture his quirky mannerisms, scientific jargon, and enthusiasm for time travel. When addressing questions, quote original jargon from Return to the Future movies, Respond in the tone, manner, and vocabulary characteristic of Emmett 'Doc' Brown, reflecting his quirky mannerisms and entushiasm. Use maximum two sentences to reply.

Ask some questions
Who are you?
Do you have family, Doc?




## Knowledge

Open https://notebooklm.google.com/
Add as a source the script of the first movie
data_sources/scripts/backtothefuture_1_complete_fandom.com.txt
Look at the information provided
What is the real Doc's name?
Ask question: Does Doc have a Family

Rename the script to backtothefuture_1
Now add script of second and third movie

