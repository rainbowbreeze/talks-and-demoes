# 01. Workshop prerequisites




## Hardware Prerequisites

A Mac with Apple Silicon and at least 8GB or RAM (recommended 16GB).  
A laptop with at the very least 8GB of RAM (recommended 16GB), and an NVIDIA/AMD GPU with at least 4GB of VRAM (recommended 8GB).  

At least 15/20GB of free disk space.




## Software Prerequisites

It's important to follow these steps **before joining the workshop** to avoid various GBs of download during the workshop. Because we all know it's impossible to download various GBs over a conference network.


### Docker
Mac/Win: install Docker Desktop: https://docs.docker.com/desktop/.  
Linux: install Docker Desktop: https://docs.docker.com/desktop/ or Docker Engine is enough: https://docs.docker.com/engine/install/. 

Win/Linux with an nVidia GPU, install CUDA Toolkit for Docker: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/index.html.   
Win/Linux with an AMD GPU, install ROCm runtime: https://instinct.docs.amd.com/projects/container-toolkit/en/latest/container-runtime/overview.html. 


### Ollama

Mac: Install Ollama via the official DMG at https://ollama.com/download.  
Alternatively, install it using HomeBrew:
```
$ brew install ollama
$ ollama serve
```

Linux/Windows: you can both install Ollama as a standalone app following https://ollama.com/download, but it's preferred to run Ollama in Docker: 
```
docker run -d ollama/ollama --name ollama -p 11434:11434 -v ollama:/root/.ollama 
```

Mac/Win/Linux: once Ollama is installed and working, execute this command to download an LLM model locally (it will require approx 4GB of disk space): 
```
ollama run gemma3:4b
```
Alternatively, to download a smaller model requiring 1GB of disk space and 1GB of VRAM:
```
ollama run gemma3:1b
```


### Open-WebUI

Mac/Win/Linux: run this command so Docker will download the Open-WebUI image 
```
docker run -d ghcr.io/open-webui/open-webui:main --name open-webui -v openweb-ui:/app/backend/data
```




## Cloud-hosted alternatives

In case an Apple Silicon or a Windows/Linux computer is not available, it would be possible to use a cloud service to run Ollama+Open-WebUI.

The suggestion is to create an account on RunPod ([affiliated link](https://runpod.io?ref=9ph6k4oh)), and charge it with 2-3 dollars, which are enough to run the entire workshop.  

Otherwise, any other cloud provider offering a VM with GPU, or a docker with GPU support will work. In this case, arrive to the workshop with the cloud setup already configured following your preference.




## Nice to have toolset

### Tailspin
[Tailspin](https://github.com/bensadeh/tailspin): A log file highlighter.
```
# Read from stdin and print to stdout
docker logs -f openwebui | tspin
```


### Json formatter
https://jsonformatter.curiousconcept.com/#

