# Bringing Doc Brown to life with open source tools and LLM

## Slides
https://docs.google.com/presentation/d/1sw7D6axwrNQSQGYTD4IMqbsXXT1wFFqh6dzFcjN6JsU/edit



## Ollama

Start Ollama

On a CUDA-supported environment, via an independent docker compose file - [example](docker/1-ollama_only/docker-compose.yaml).

On a Mac, as a standalone app
```
brew install ollama
ollama serve 
ollama run gemma2:9b
```
Ask some questions to check if the model works



<br/>

## Open WebUI

On a Mac, as a standalone container - [example](docker/2-openwebui_only_mac/docker-compose.yaml)
```
cd <local_dev_path>/docker
docker compose -p "openwebui_stack" up -d
docker logs -f open-webui
```


On a CUDA-supported environement, in multiple ways
- Open-WebUI + Ollama bundled in a single docker image - [example](docker/3-openwebui_ollama_bundled/docker-compose.yaml)
- Open-WebUI + Ollama in the same docker compose stack - [example](docker/3-openwebui_ollama_samestack/docker-compose.yaml)
- Open-WebUI + Ollama in two separated docker container stacks - [example](docker/3-openwebui_ollama_separated)


While waiting
https://openwebui.com/
https://github.com/open-webui/open-webui
To know all the environment vars: https://docs.openwebui.com/getting-started/env-configuration/


Open browser at localhost:8080
Register a new user: rainbow@bree.ze - rainbow
A quick tour on the interface (chat)



### Connect with Ollama


Go to Open WebUI
Settings - Admin Settings
- Connections
  - Disable OpenAI API
  - Ollama API
    - http://host.docker.internal:11434 (or what is pointed in the docker file for OLLAMA_BASE_URL variable)
    - Verify connection

visit to look for model
https://ollama.com/library

Go to Open WebUI
Settings - Admin Settings
- Models
  - Pull a model from Ollama.com
    - gemma2:9b

Workspace
Create a model
- picture
  - pickup from [file](pictures/Doc_Emmett_Brown.webp)
- name
  - Doc Brown
- Base model
  - Gemma2:2b
- Description
  - Great Scott! Let's go back to the future together

Ask some questions
New Chat - Select Doc Brown - Set as default
_Who are you?_
_Who is Emmet Brown?_



### Acting as the character
visit to look for personalities
https://openwebui.com/m/nihaal007/nikolas-tesla
https://openwebui.com/m/geometric/sigmund-freud


Workspace
Open Doc model
- Model Params
  - System Prompt
    - You are Emmett 'Doc' Brown, the eccentric, genius scientist from the Back to the Future series. Capture his quirky mannerisms, scientific jargon, and enthusiasm for time travel. When addressing questions, quote original jargon from Return to the Future movies, Respond in the tone, manner, and vocabulary characteristic of Emmett 'Doc' Brown, reflecting his quirky mannerisms and enthusiasm. Use maximum two sentences to reply.

Ask some questions
_Who are you?_
_Do you have family, Doc?_


To look at the logs: https://jsonformatter.curiousconcept.com/



<br/>

## Knowledge

### Generate Doc Brown FAQ
Open https://notebooklm.google.com/
Add as a source the [script](scripts/backtothefuture_1_complete_fandom.com.txt) of the first movie

Ask some questions and look at the information provided
_What is the real Doc's name?_
_Does Doc have a family?_

Rename the script to backtothefuture_1
Now add script of [second](scripts/backtothefuture_2_complete_fandom.com.txt) and [third](scripts/backtothefuture_3_complete_fandom.com.txt) movie

Ask the same questions and check for differences
_What is the real Doc's name?_
_Does Doc have a family?_


Generate the FAQ
```
I need a detailed FAQ document about Emmet Brown. It should contain all the information on the character, his role on the story, strenghts and weakenesses , fun facts and relevant actions.
Use a minimum of 20000 words
```

Copy the output, paste it a text document (like [this one](scripts/emmet_brown_faq_15000.txt)), and save the document as text file


### RAG for the model
Return to Open WebUI, and check the RAG configuration

Admin Settings - Documents
Default
- Embedding Model Engine
  - Default (sentence transformers)
  - sentence-transformers/all-MiniLM-L6-v2

Show other models at https://sbert.net/docs/sentence_transformer/pretrained_models.html#original-models
Show https://ollama.com/library/nomic-embed-text

Show performance at https://huggingface.co/spaces/mteb/leaderboard (linked in the previous post, under "_Consider using the Massive Textual Embedding Benchmark leaderboard as an inspiration of strong Sentence Transformer models_")
- search for all-Mini
- search for nomic

Show https://www.bentoml.com/blog/a-guide-to-open-source-embedding-models
Show https://medium.com/@guptak650/nomic-embeddings-a-cheaper-and-better-way-to-create-embeddings-6590868b438f

Return to Open WebUI
Admin Settings - Documents
Change to
- Embedding Model Engine
  - Ollama
  - Address: http://host.docker.internal:11434 (or what is pointed in the docker file for OLLAMA_BASE_URL variable)
- Embedding Model
  - nomic-embed-text:latest



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
_Are you a father?_



<br/>

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



### Kokoro-web (optional)

https://docs.openwebui.com/tutorials/text-to-speech/kokoro-web-integration/

https://github.com/eduardolat/kokoro-web
https://huggingface.co/hexgrad/Kokoro-82M
- with voices

```
services:
  kokoro-web:
    image: ghcr.io/eduardolat/kokoro-web:latest
    ports:
      - "3000:3000"
    environment:
      # Change this to any secret key to use as your OpenAI compatible API key
      - KW_SECRET_API_KEY=your-rainbow
      - KW_PUBLIC_NO_TRACK=
    volumes:
      - /Volumes/Data/development/docker/kokoro-web/volumes/kokoro-cache:/kokoro/cache
    restart: unless-stopped
```

Admin Panel → Settings → Audio
Text-to-Speech Engine: OpenAI
API Base URL: http://host.docker.internal:3000/api/v1
API Key: rainbow
TTS Model: model_q8f16 (best balance of size/quality)
TTS Voice: af_heart (default warm, natural english voice). You can change this to any other voice or formula from the Kokoro Web Demo



### OpenedAI Speech

Show https://docs.openwebui.com/category/%EF%B8%8F-text-to-speech with the different TTS tutorials

https://docs.openwebui.com/tutorials/text-to-speech/openedai-speech-integration/
Open https://github.com/matatonic/openedai-speech

On a Mac, as a standalone container - [example](docker/4-openedai-speech_only/docker-compose.yaml)

On a CUDA-supported environement, Open-WebUI + Ollama + Openedai-Speech in the same docker compose stack - [example](docker/4-openedai-speech-samestack/docker-compose.yaml)

Go to Open WebUI
Settings - Admin Settings
- Audio
  - TTS Settings
    - Text-to-Speech Engine
      - Open AI
    - Host
      - http://host.docker.internal:8000/v1 (or what is pointed in the docker file for AUDIO_TTS_OPENAI_API_BASE_URL variable)
    - API key
      - sk-111111111
  - TTS Model
    - tts-1
  - TTS Voice
    - shimmer

Take an existing reply, and play it (generated by Piper).


Go to Open WebUI
Settings - Admin Settings
- Audio
  - TTS Settings
  - TTS Model
    - tts-1-hd
  - TTS Voice
    - alloy

Take an existing reply, and play it (generated by Coqui)



### Voice Cloning
https://github.com/matatonic/openedai-speech?tab=readme-ov-file#coqui-xtts-v2

Show video of Christopher Lloyd: https://www.youtube.com/watch?v=DFLMc-RRlo8  
Show code to extract voice: https://github.com/matatonic/openedai-speech?tab=readme-ov-file#coqui-xtts-v2  

Create the folder for the voice sample ```volumes/openedai-speech/voices/clone/emmet_brown```
Copy the (sample voice file)[voices/emmet_brown/emmet_brown.wav] to the dir

Append to the file ```volumes/openedai-speech/config/voice-to-speaker.yaml```
```
  doc-brown:
    model: xtts # you can specify an older xtts version
    speaker: voices/clone/emmet_brown/emmet_brown.wav
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
This file file should be like [this one](voices/voice_to_speaker.yaml)

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



<br/>
<br/>

## Appendix - Prepare the RunPod Pod to run Ollama and OpenedAI Speech

Resources 
- https://docs.runpod.io/tutorials/pods/run-ollama
  - (basic pytorch machine, with Cuda and ssh, then it's possible to install software separately (but not via docker))

### RunPod Network disk
Network volume  
EUR-RO-1 (where RTX A4000 - 16Gb are)  
name: doc-brown  
GB: 40  


### Create a Pod
Container image: runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04

Edit template
- http ports: 8888,8000,11434
- tcp ports: 22
- env vars
  - OLLAMA_MODELS: /workspace/ollama/models
  - OLLAMA_HOST: 0.0.0.0
  - OLLAMA_DEBUG: 1
  - TTS_HOME: voices
  - HF_HOME: voices
  - COQUI_TOS_AGREED=1
  - PRELOAD_MODEL=xtts

Update the system
```
apt update && apt dist-upgrade -y && apt install -y vim
```



### Ollama
Connect to Web Terminal

```
apt install -y lshw
curl -fsSL https://ollama.com/install.sh | sh
export (controla vars)
mkdir /workspace/ollama
```

Run Ollala
```
ollama serve
```

Alternatively
```
cd /workspace/ollama
ollama serve > ollama.log 2>&1 &
tail -f ollama.log
```

Preload model
```
ollama pull gemma2:2b
ollama run gemma2:2b
```
```
Hi model!
/bye
```



### OpenedAI Speech

Connect to Web Terminal

Run only once, to prime the network volume
https://github.com/matatonic/openedai-speech?tab=readme-ov-file#installation-instructions
```
cd /workspace/
git clone https://github.com/matatonic/openedai-speech
cd opendai-speech
cp sample.env speech.env
python -m venv .venv
source .venv/bin/activate
pip install -U -r requirements.txt
bash startup.sh
```

Stop the app, anche check ```config``` and ```voices``` folders are created

```
mkdir -f voices/clone/emmet-brown
cd voices/clone/emmet-brown
wget https://www.rainbowbreeze.it/site-media/voices/emmet_brown.wav
```
Copy to ```voices/clone/emmet-brown``` the file ```emmet_brown.wav```

Append to ```config/voice_to_speaker.yaml``` Doc Brown voice
```
  doc-brown:
    model: xtts
    speaker: voices/clone/emmet_brown/emmet_brown.wav # this could be you
    language: auto
    enable_text_splitting: True
    length_penalty: 1.0
    repetition_penalty: 10
    speed: 1.0
    temperature: 0.75
    top_k: 50
    top_p: 0.85
    comment: This is Doc Emmet Brown voice, from Return to the Future
```

All the time the container is restarted
```
apt install -y ffmpeg
cd /workspace/openedai-speech
source .venv/bin/activate
bash startup.sh -L DEBUG
```


<br/>
<br/>

## Appendix Obtain a sample of Emmet Brown voice

Create a emmet_brown.wav file following [guideliles](https://github.com/matatonic/openedai-speech?tab=readme-ov-file#guidelines-for-preparing-good-sample-files-for-coqui-xtts-v2)

```
yt-dlp --extract-audio --audio-format wav --audio-quality 22050 https://www.youtube.com/watch?v=DFLMc-RRlo8

# convert a multi-channel audio file to mono, set sample rate to 22050 hz, trim to 30 seconds, and output as WAV file.
ffmpeg -i input.mp3 -ac 1 -ar 22050 -ss 00:01:26.0 -t 30 -y emmet_brown.wav
```

