# 07. Use MCP natively in Open WebUI




## Some background information

### What is MCP?
MCP most commonly refers to the **Model Context Protocol**, an open standard for connecting large language models (LLMs) to external tools and data sources.   
It acts as a universal communication bridge, enabling AI assistants to access real-time information and perform tasks beyond their initial training data.  
**How it works**: An AI "client" (like a coding assistant) uses MCP to send requests to an "MCP server," which is built by a service provider (like a company that hosts code repositories). The server handles the specific API details of its tools and returns the results to the client. 

MCP server communicates with the client using one of the following three channels:
- stdio
- SSE (Server-Sent Events)
- Streamable HTTP
Open WebUI [supports natively](https://docs.openwebui.com/features/mcp) only MCP via HTTP Streaming. [Video](https://www.reddit.com/r/LocalLLaMA/comments/1ns7f86/native_mcp_now_in_open_webui/).



#### Catalogs with MCP servers

There are many online catalogs listing MCP servers. Here some:
- https://mcpservers.org/remote-mcp-servers (it lists only MCP servers, search for the ones supporting http)
- https://mcp.so/servers


### Additional resources with info
- Official instruction on how to configure an MCP server: https://docs.openwebui.com/features/mcp.




## Connect Open WebUI to an MCP server

The goal is to access the [CoinGecko MCP server](https://mcp.api.coingecko.com/), which is accessible via Streameable HTTP.


Admin Panel -> Settings -> External Tools.
- Click `Add Server`.
- Type
  - MCP Streamable HTTP.
- URL
  - https://mcp.api.coingecko.com/mcp
- Auth
  - None
- ID
  - coingecko_mcp_http
  - this is the name reported in the logs
- Name
  - CoinGecko MCP via http
  - this is the name used in the UI
- Description
  - Get real time quotation of crypto assets
- Save




## Use the MCP server

To use an MCP server, the model needs to have the tool calling capabily. It means it understands the user's query, decides whether an external function needs to be called, correctly formats the call, and integrates the tool's output into the conversation. [qwen3:8b](https://ollama.com/library/qwen3) has them.


First, let's see what happens when the model can only use its internal knowledge. Open a chat with qwen3:8b and ask:
```
What's the current BTC value?
```
The model should return a BTC value linked to its latest data cut. Which, of course, is not updated.


Now, open another chat, still with qwen3:8b and
- Select the `CoinGecko MCP via http` tool in the list of available tools, and enable it.
- Go to Chat Controls -> Advanced Params (top right of the chat window).
- Change the Function Calling parameter from `Default` to `Native`.
  - This option enables Function Calling ReACT-style (Reasoning + Acting) tool use.

And finally ask again:
```
What's the current BTC value?
```
The model should now show it has called the CoinGecko MCP and return the right current value of BTC is USD.  


The same info (MCP to call and native Function Calling can also be preset in a new agent).


To check the model called the MCO server, check the log of the docker container. Log example when using MCP over http:
``` 
2025-10-12 11:01:30.929 | DEBUG    | mcp.client.streamable_http:streamablehttp_client:480 - Connecting to StreamableHTTP endpoint: https://mcp.api.coingecko.com/mcp

2025-10-12 11:01:30.966 | DEBUG    | mcp.client.streamable_http:post_writer:389 - Sending client message: root=JSONRPCRequest(method='initialize', params={'protocolVersion': '2025-06-18', 'capabilities': {}, 'clientInfo': {'name': 'mcp', 'version': '0.1.0'}}, jsonrpc='2.0', id=0)
```




## Additional Resources



## Next session
[MCP via mcpo](08-mcp_via_mcpo.md)
