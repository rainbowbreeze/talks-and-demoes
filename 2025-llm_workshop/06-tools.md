# 06. Using Tools in Open WebUI


## How Tools work in Open WebUI

https://docs.openwebui.com/openapi-servers/open-webui
- Open WebUI v0.6+ supports integration with external tools via the OpenAPI servers
  - Meaning you can easily extend your LLM workflows using custom or community-powered tool servers
- Why OpenAPI support? Strong Security Focus: Built around HTTP/REST APIs, OpenAPI inherently supports widely used, secure communication methods including HTTPS and well-proven authentication standards (OAuth, JWT, API Keys).




## OpenAPI Tool Server
Some tools are available in the https://github.com/open-webui/openapi-servers


### Install the OpenAPI time server
Download the repo and launch a time OpenAPI server
```
git clone https://github.com/open-webui/openapi-servers.git
cd openapi-servers
cd servers
cd time
docker compose up
```

A OpenAPI time server is available at http://localhost:8000   
Look at the function exposed via the [main.py](https://github.com/open-webui/openapi-servers/blob/main/servers/time/main.py) file.


### Configure Open WebUI to use the time server

Tools in Open WebUI can be configured as **User Tool Server** or **Global Tool Server**
- The primary distinction between User Tool Servers and Global Tool Servers is where the API connection and requests are actually made:
  - User Tool Servers
    - Requests to the tool server are performed directly from your browser (the client).
    - This means you can safely connect to localhost URLs (like http://localhost:8000)—even exposing private or development-only endpoints such as your local filesystem or dev tools—without risking exposure to the wider internet or other users.
    - Your connection is isolated; only your browser can access that tool server.
  - Global Tool Servers
    - Requests are sent from the Open WebUI backend/server (not your browser).
    - The backend must be able to reach the tool server URL you specify—so localhost means the backend server's localhost, not your computer's. 
    - Use this for sharing tools with other users across the deployment, but be mindful: since the backend makes the requests, you cannot access your personal local resources (like your own filesystem) through this method.

**User Tool Server** configuration:
- Settings -> External Tools -> Add new tool
- Enter the URL where your OpenAPI tool server is running, eg http://localhost:8000.
  - http://host.docker.internal WON'T work because the tool call is made from the browser
- Test the connection with the tool
- Click "Save".
- The name in the UI will be the name exposed by the Tool server

**Global Tool Server** configuration:
- Admin Panel -> Settings -> External Tools
- Enter the URL where your OpenAPI tool server is running, eg http://host.docker.internal:8000.
  - using http://host.docker.internal:8000 if Open-WebUI was launched as separate docker container
  - using the container name if Open-WebUI and the tool were launched together, or are in the same Docker network
  - using the IP of the machine where tool is hosted
- Id
  - `time_openapi`
    - The id is visible in the log as `"tool_ids":["server:local_time_mcp"]`
- Name
  - `time via openapi`
    - The name will show in the UI to configure the tool
- Description
  - Time server exposed via OpenAPI
- Visibility
  - public or a more fine-graned permission model




## Use the time server

Open a chat with gemma3:4b and ask:
```
What's the current time?
```

Now, open another chat, still with gemma3:4b, select the time tool in the list of available tools, and ask:
```
What's the current time?
```
Check also the log of the docker container with the time tool to see if it was called.


(Optional) Use "Native" Function Calling ReACT-style (Reasoning + Acting) Tool Use
For this to work effectively, your selected model must support native tool calling. Some local models claim support but often produce poor results.  
Open the chat window.
- Go to Chat Controls -> Advanced Params.
- Change the Function Calling parameter from `Default` to `Native`.

If a model without tools calling support (like gemma3) is used, an error message is returned
