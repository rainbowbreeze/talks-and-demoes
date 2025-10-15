# 01. Workshop prerequisites



## Hardware Prerequisites

A Mac with Apple Silicon (M1 and above) and at least 8GB or RAM (recommended 16GB).  
A laptop with at the very least 8GB of RAM (recommended 16GB), and an NVIDIA/AMD GPU with at least 4GB of VRAM (recommended 8GB).  

At least 15/20GB of free disk space.




## Software Prerequisites

### Docker
Mac/Win: install Docker Desktop: https://docs.docker.com/desktop/.  
Linux: install Docker Desktop: https://docs.docker.com/desktop/ or Docker Engine is enough: https://docs.docker.com/engine/install/. 

Win/Linux with an nVidia GPU, install CUDA Toolkit for Docker: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/index.html.   
Win/Linux with an AMD GPU, install ROCm runtime: https://instinct.docs.amd.com/projects/container-toolkit/en/latest/container-runtime/overview.html. 




## Nice to have tools

### Tailspin
[Tailspin](https://github.com/bensadeh/tailspin): A log file highlighter.
```
# Read from stdin and print to stdout
docker logs -f openwebui | tspin
```


### Json formatter
https://jsonformatter.curiousconcept.com/#


### mactop
[mactop](https://github.com/context-labs/mactop) is a terminal-based monitoring tool "top" designed to display real-time metrics for Apple Silicon chips



## A note on running this workshop.

This workshop requires at least 6-10Gb of data download. Because we all know it's impossible to download various GBs over a conference network.

As a workaround, it's possible to download the majority of the data **before** the workshop.

**Ollama model**
Mac/Win/Linux: connect to the standalone Ollama app to download the models used in this workshop
```
ollama run gemma3:4b
ollama run qwen3:4b
```
Docker container: run these commands to download the models used in this workshop
```
docker exec -it ollama ollama run gemma3:4b
docker exec -it ollama ollama run qwen3:4b
``` 


**Open WebUI**
Mac/Win/Linux: run this command so Docker will download the Open-WebUI image 
```
docker run -d ghcr.io/open-webui/open-webui:main --name open-webui -v openweb-ui:/app/backend/data
```




## Cloud-hosted alternatives

In case an Apple Silicon or a Windows/Linux computer is not available, it would be possible to use a cloud service to run Ollama+Open-WebUI.

The suggestion is to create an account on RunPod ([affiliated link](https://runpod.io?ref=9ph6k4oh)), and charge it with 2-3 dollars, which are enough to run the entire workshop.  

Otherwise, any other cloud provider offering a VM with GPU, or a docker with GPU support will work. In this case, arrive to the workshop with the cloud setup already configured following your preference.

