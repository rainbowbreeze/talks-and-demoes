# 08. User MCP with MCPO


## What is MCPO

[mcpo](https://github.com/open-webui/mcpo) means MCP (Model Context Protocol)-to-OpenAPI proxy server.  
The MCP-to-OpenAPI proxy server lets you use tool servers implemented with MCP (Model Context Protocol) directly via standard REST/OpenAPI APIs—. If you're an end-user or application developer, this means you can interact easily with powerful MCP-based tooling directly through familiar OpenAPI REST-like endpoints

https://docs.openwebui.com/openapi-servers/mcp/
- MCP servers typically rely on raw stdio communication, which is:
  - 🔓 Inherently insecure across environments
  - ❌ Incompatible with most modern tools, UIs, or platforms
  - 🧩 Lacking critical features like authentication, documentation, and error handling
- The mcpo proxy eliminates those issues—automatically:
  - ✅ Instantly compatible with existing OpenAPI tools, SDKs, and clients
  - 🛡 Wraps your tools with secure, scalable, and standards-based HTTP endpoints
  - 🧠 Auto-generates interactive OpenAPI documentation for every tool, entirely config-free
  - 🔌 Uses plain HTTP—no socket setup, daemon juggling, or platform-specific glue code
- As soon as it starts, the MCP Proxy (mcpo) automatically:
  - Discovers MCP tools dynamically and generates REST endpoints.
  - Creates interactive, human-readable OpenAPI documentation accessible at:
  - http://localhost:8000/docs
  - Simply call the auto-generated API endpoints directly via HTTP clients, AI agents, or other OpenAPI tools of your preference.

Additional notes:
- mcpo can start MCP servers with both uvx of npx
- in case extra libraries are required, they're installed on the fligth




## Install MCPO with docker

Tutorial: https://lobehub.com/it/mcp/baronco-open-webui-and-mcpo

Looking at the [Dockerfile of the mcpo container](https://github.com/open-webui/mcpo/blob/main/Dockerfile), 
```
# Entrypoint set for easy container invocation
ENTRYPOINT ["mcpo"]

# Default help CMD (can override at runtime)
CMD ["--help"]
```
It shows it starts the command `mcpo`, with the `--help` param.


Based on this, it's possible to modify the command to take the configuration from a config file, instead of having it embedded in the docker config.  
[docker compose example](docker/4-mcpo/docker-compose.yaml) to start the container using a config file, which autoreload on changes.

[Optional] A bash file to run it
```
#!/bin/bash

# Without the -p, the stack takes the name of the folder
docker compose -p "mcpo" up -d
sleep 2
docker logs -f mcpo
```


### Configure MCP Servers to run

[Examples](https://github.com/open-webui/mcpo?tab=readme-ov-file#-using-a-config-file) of configuration based on different MCP to run:
```
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    },
    "time": {
      "command": "uvx",
      "args": ["mcp-server-time", "--local-timezone=America/New_York"],
      "disabledTools": ["convert_time"] // Disable specific tools if needed
    },
    "mcp_sse": {
      "type": "sse", // Explicitly define type
      "url": "http://127.0.0.1:8001/sse",
      "headers": {
        "Authorization": "Bearer token",
        "X-Custom-Header": "value"
      }
    },
    "mcp_streamable_http": {
      "type": "streamable-http",
      "url": "http://127.0.0.1:8002/mcp"
    } // Streamable HTTP MCP Server
  }
}
```

Edit `config.json` and add the time server
```
{
  "mcpServers": {
    "time": {
      "command": "uvx",
      "args": ["mcp-server-time", "--local-timezone=America/New_York"]
    }
  }
}
```
Note: Each tool is mounted under its own unique path (`time`in this case).


http://localhost:8000/docs to see the existing servers, and the docs the LLM will see.




## Configure Open-WebUI

Open-WebUI settings, Admin Panel, Settings, External Tools, Add a new one
- Type: OpenAI
- URL: http://host.docker.internal:8000/time
- Auth: None
- ID: time_mcpo
- Name: time via mcpo

Configure the Model to Use Tools
- Go to the Models section in Open WebUI
- Select the model you want to configure
- Click on Advanced Params
- Change the Function Calling setting from "Default" to "Native"
- Step 4: Enable Tools in the Model 🛠️
- On the same model configuration page, scroll down to the Tools section
- Enable the MCP tools you added in the previous step



## Adding a YouTube transcription MCP

https://github.com/jkawamoto/mcp-youtube-transcript


Edit the file `config.app` file:
```
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    },
    "time": {
      "command": "uvx",
      "args": ["mcp-server-time", "--local-timezone=America/New_York"]
    },
    "youtube-transcript": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/jkawamoto/mcp-youtube-transcript",
        "mcp-youtube-transcript"
      ]
    }
  }
}
```




## Additional Resources

Additional MCP servers to play with
- Kali Linux MCP: See NetworkChuck video at https://www.youtube.com/watch?v=GuTcle5edjk
- Open Meteo: https://mcpservers.org/servers/cmer81/open-meteo-mcp
- Playwrite: https://mcpservers.org/servers/microsoft/playwright-mcp
  - See also what Open-WebUI offers natively
