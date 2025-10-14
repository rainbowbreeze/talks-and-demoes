
# 01. Configure and launch Open WebUI and Ollama


## Slides

https://docs.google.com/presentation/d/1HyMKtj2ttpvZKUowFxdOETA9bJ2l3tUYpWv-p2HtidU/edit



## Software installation

There are two main software used in this workshop:
- [Ollama](https://ollama.com/) is a locally deployed AI model runner, designed to allow users to download and execute large language models (LLMs) directly on their personal computer.  
- [Open WebUI](https://docs.openwebui.com/) is an extensible, feature-rich, and user-friendly self-hosted AI platform designed to operate entirely offline. It supports various LLM runners like Ollama and OpenAI-compatible APIs, with built-in inference engine for RAG,

On a Lin/Win CUDA-supported environment, the easiest way to install them is via the `ghcr.io/open-webui/open-webui:ollama` docker image. It includes both of them, with CUDA support enabled.  
[docker-compose example](docker/1-ollama_only/docker-compose.yaml).

On Mac Silicon (M1 - Mx), if Ollama is installed via docker, GPU acceleration is not available. The only way (as for 20251014) to leverage Apple Metal or ANE acceleration, is to install Ollama as a standalone app.



### Ollama standalone

Ollama has standalone [clients](https://ollama.com/download) for Win/Lin/Mac. If accelerated hardware is available, the client uses it.   

On a Mac Intel / Apple Silicon, also the Homebrew way is possible using `brew install ollama`.  Apple Silicon hardware acceleration is supported.  

To install using docker, hardware accelerated images are available `ollama/ollama:latest`.  If installed on Mac, no hardware acceleration is available (_although small models with < 1B parameters are usable_).  
[docker compose example](docker/1-ollama_only/docker-compose.yaml).



### Open WebUI standalone

Two docker images to install only Open WebUI are available:
- with hardware acceleration: `ghcr.io/open-webui/open-webui:cuda`
- without hardware acceleration: `ghcr.io/open-webui/open-webui:latest`



### Ollama and Open WebUI on the same docker container

Finally, it's possible to install Ollama and Open WebUI images separately, but on the same container stack (they will share the same internal network, etc).  
[docker compose example](docker/3-openwebui_ollama_samestack/docker-compose.yaml).  




## Launch Open WebUI

Open WebUI is available at http://localhost:8080
The provided docker compose files also set the environmental variables to connect Open WebUI to Ollama.  
In details:
- When Ollama runs as a standalone app or container on the same machine of Open WebUI image
  - use the `host.docker.internal:host-gateway` directive and reach Ollama at the `http://host.docker-internal` alias
- When Ollama is installed in the same container stack than Open WebUI
  - reach Ollama using the image name assigned to it, for example `http://ollama` alias
- When Ollama is on a different machine / url
  - reach Ollama using the machine ip/address or the Ollama server url


Admin Panel -> Settings -> Connections
- Enable Ollama API
- Manage Ollama API connection
  - Put the most appropriate access for the Ollana servier
  - http://host.docker.internal:11434 (becaose Ollama runs a standalone app in the same machine of Open WebUI)
- Verify the connection



### Download an LLM mode locally

In order to work, Ollana needs an LLM locally installed locally. The [models library](https://ollama.com/search) is always-growing, and can focus on the [Gemma3](https://ollama.com/library/gemma3) model family.

Admin Panel -> Settings -> Connections
- Ollama API -> Manage
  - Pull a model form Ollama.com
    - Select gemma3:4b and pull the model
    - Select qwen3:8b and pull the model



### First chat

In the Open WebUI main page, open a new chat and ask for any queestion




### Checking the logs

In one termina window:
MAC: `ollama serve`
Lin/Win: `docker logs -f ollama | tspin`


In another terminal window
Lin/Win/Mac: `docker logs -f openwebui | tspin`


How to debug json file
https://jsonformatter.curiousconcept.com/#




## Additional resources


Open-WebUI prompts
- https://docs.openwebui.com/features/workspace/prompts/
- https://openwebui.com/prompts


Open-WebUI tools
- https://openwebui.com/tools