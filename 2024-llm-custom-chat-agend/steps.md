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

Ask some questions and look at the information provided
What is the real Doc's name?
Does Doc have a family?

Rename the script to backtothefuture_1
Now add script of second and third movie
data_sources/scripts/backtothefuture_2_complete_fandom.com.txt
data_sources/scripts/backtothefuture_3_complete_fandom.com.txt

Ask the same questions and check for differences
What is the real Doc's name?
Does Doc have a family?

Generate the FAQ
I need a detailed FAQ document about Emmet Brown. It should contain all the information on the character, his role on the story, strenghts and weakenesses , fun facts and relevant actions.
Use a minimum of 20000 words

Copy the output, paste it a text document, and save the document as text file

Return to Open WebUI
Workspace - Knowledge
Create a knowledge base (+ button)
- Name
  - Emmett Brown FAQ
- What are you triving to achieve
  - Provide a reference on Emmet Brown character
- Collection - Add Content (+ button)
  - Select the FAQ file previously saved

Workspace - Models
- Edit Doc Brown
  - Knowledge, select Knowledge, add "Emmet Brown FAQ"

New Chat, and ask
Are you a father?




## Voice 

### Web Speech API

Quick demo of Web Speech API
https://mdn.github.io/dom-examples/web-speech-api/speak-easy-synthesis/

Open Open WebIU
Go to Open WebUI
Settings - Admin Settings
- Audio
  - TTS Settings
    - Text-to-Speech Engine
      - Web API
  - TTS Voice
    - Fred

Go to a previous chat version
Play button

Show the other settings for the Text-to-Speech Engine


### OpenedAI Speech
Open https://github.com/matatonic/openedai-speech
docker-compose-step3.yaml
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

  # https://github.com/matatonic/openedai-speech/releases/
  tts:
    # piper for all models, no gpu/nvidia required, ~1GB
    #container_name: openedai-speech-min
    #image: ghcr.io/matatonic/openedai-speech-min

    # support also coqui-tts
    container_name: openedai-speech
    image: ghcr.io/matatonic/openedai-speech
#    env_file:
#      /Volumes/Data/zz_nobackup/development/openweb-ui/volumes/openedai-speech/speech.env
    environment:
      - 'TTS_HOME=voices'
      - 'HF_HOME=voices'
      - 'PRELOAD_MODEL=xtts'
    ports:
      - "8000:8000"
    volumes:
      - /Volumes/Data/zz_nobackup/development/openweb-ui/volumes/openedai-speech/voices:/app/voices
      - /Volumes/Data/zz_nobackup/development/openweb-ui/volumes/openedai-speech/config:/app/config
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
      - tts
    restart: unless-stopped
```

docker-compose -f docker-compose-step3.yaml up

Go to Open WebUI
Settings - Admin Settings
- Audio
  - TTS Settings
    - Text-to-Speech Engine
      - Open AI
    - Host
      - http://host.docker.internal:8000/v1
    - API key
      - sk-111111111
  - TTS Model
    - tts-1
  - TTS Voice
    - shimmer

Take an existing reply, and play it.


Go to Open WebUI
Settings - Admin Settings
- Audio
  - TTS Settings
    - Text-to-Speech Engine
      - Open AI
    - Host
      - http://host.docker.internal:8000/v1
    - API key
      - sk-111111111
  - TTS Model
    - tts-1-hd
  - TTS Voice
    - alloy

Take an existing reply, and play it.



### Voice Cloning
https://github.com/matatonic/openedai-speech?tab=readme-ov-file#coqui-xtts-v2


append to the file volumes/openedai-speech/config/voice-to-speaker.yaml
```
  doc-brown:
    #model: xtts_v2.0.2 # you can specify an older xtts version
    model: xtts # you can specify an older xtts version
    speaker: voices/clone/emmet_brown/emmet_brown.wav # this could be you
    language: auto
    enable_text_splitting: True
    length_penalty: 1.0
    repetition_penalty: 10
    speed: 1.0
    temperature: 0.75
    top_k: 50
    top_p: 0.85
    comment: You can add a comment here also, which will be persistent and otherwise ignored.
```


Show video
Christopher Lloyd
https://www.youtube.com/watch?v=DFLMc-RRlo8

Show code to extract voice
https://github.com/matatonic/openedai-speech?tab=readme-ov-file#coqui-xtts-v2

Show file 
volumes/openedai-speech/config/voice-to-speaker.yaml

Go to Open WebUI
Settings - Admin Settings
- Audio
  - TTS Model
    - tts-1-hd
  - TTS Voice
    - doc-brown

Take an existing reply, and play it.
Go to Open WebUI
Settings
- Audio
  - TTS Settings
    - Auto-playback response
      - On


And now start chatting with your Doc Brown bot!



