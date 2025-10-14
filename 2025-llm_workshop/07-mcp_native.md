# 07. User MCP natively in Open WebUI

## What is MCP?
MCP most commonly refers to the **Model Context Protocol**, an open standard for connecting large language models (LLMs) to external tools and data sources.   
It acts as a universal communication bridge, enabling AI assistants to access real-time information and perform tasks beyond their initial training data.  
**How it works**: An AI "client" (like a coding assistant) uses MCP to send requests to an "MCP server," which is built by a service provider (like a company that hosts code repositories). The server handles the specific API details of its tools and returns the results to the client. 

MCP server communicates with the client using one of the following thee channels:
- stdio
- SSE (Server-Sent Events)
- Streamable HTTP
Open WebUI [supports natively](https://docs.openwebui.com/features/mcp) only MCP via HTTP Streaming. [Video](https://www.reddit.com/r/LocalLLaMA/comments/1ns7f86/native_mcp_now_in_open_webui/).




## Connect to an MCP server

There are different catalogs of MCP servers: https://mcp.so/servers, https://mcpservers.org/, etc.

https://mcpservers.org/remote-mcp-servers shows the MCP server with Streameable HTTP, like the [one from CoinGecko](https://mcp.api.coingecko.com/).


[Instructions](https://docs.openwebui.com/features/mcp) to confige the server 

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
- Name
  - CoinGecko MCP via http
- Description
  - Get real time quotation of crypto assets
- Save




## Use the MCP server

Open a chat with qwen3:8b and ask:
```
What's the current BTC value?
```

Now, open another chat, still with qwen3:8b, select the `CoinGecko MCP via http` tool in the list of available tools.

Use "Native" Function Calling ReACT-style (Reasoning + Acting) Tool Use
- Open the chat window.
- Go to Chat Controls -> Advanced Params.
- Change the Function Calling parameter from `Default` to `Native`.

And finally ask again:
```
What's the current BTC value?
```
Check also the log of the docker container with the time tool to see if it was called.

Log example when using MCP over http
``` 
2025-10-12 11:01:30.929 | DEBUG    | mcp.client.streamable_http:streamablehttp_client:480 - Connecting to StreamableHTTP endpoint: https://mcp.api.coingecko.com/mcp

2025-10-12 11:01:30.966 | DEBUG    | mcp.client.streamable_http:post_writer:389 - Sending client message: root=JSONRPCRequest(method='initialize', params={'protocolVersion': '2025-06-18', 'capabilities': {}, 'clientInfo': {'name': 'mcp', 'version': '0.1.0'}}, jsonrpc='2.0', id=0)
```




## Additional Resources




