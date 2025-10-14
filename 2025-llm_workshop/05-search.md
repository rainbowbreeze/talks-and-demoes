# 05. Web Seach in Open WebUI


## Check capabilities of the LLM

Let's start with this prompt, for Gemma3:4b model.  
Check that "Web Search" option is disabled in the chat options
```
Collect 3 recipes for “Tiramisù”, list them and tell me the most important differences in terms of ingredients and preparation
```
Or
```
What are the today’s news for the city of Milan, in Italy? Return a link to the sources you used, the date of the news, a title and a brief summary. Collect at least 10 news from various sources.
```

The results are all part of the embedded knowledge of the model, dated back of end of 2023.  



## Enable Web Search in Open-WebUI

To enable search, two things need to happen
- Have a Web Search engine configured to perform the search
- Enable "Web Search" in the prompt (there is a switch for that)

Tutorials with step-to-step instructions
- https://docs.openwebui.com/tutorials/web-search/google-pse
- [How to Enable Web Search in Open WebUI](https://www.youtube.com/watch?v=fwscnJu_Md0)


Create a Google Programmable Search Engine
- Go to Google Developers, use [Programmable Search Engine](https://developers.google.com/custom-search), and log on or create account.
- Go to [control panel](https://programmablesearchengine.google.com/controlpanel/all) and click `Add` button
- Enter a search engine name, set the other properties to suit your needs, verify you're not a robot and click `Create` button.
- Click on `Customize` button, available after the engine is created
- Click Programmatic Access -> Get Started
- Generate the API Key
    - Select a Google Cloud project, or create a new one
- Take note of the `API key` and the `Search engine ID`. 

Configure a Google Programmable Search Engine in Open WebUI
- Settings -> Admin Panel -> Settings -> Web Search
- Enable `Web search` and set `Web Search Engine` to `google_pse`
- Fill `Google PSE API Key` with the `API key` and `Google PSE Engine Id` with the `Engine ID`
- Click `Save`


Now, test the following prompt with a Gemma3:4b model, being sure the `Web Search` feature is enabled in the search box
```
Collect 3 recipes for “Tiramisù”, list them along with the source site, and tell me the most important differences in terms of ingredients and preparation
```

Check the different sources used to get the information




## Create a Event Scout agent
Any model will work

### Build the system prompt
Use [Google AI Studio](https://aistudio.google.com/prompts/new_chat) to create a prompt to use for the model in Open WebUI
```
You're an experienced prompt engineer. Your goal is to write a prompt to query a Gemma3 LLM to search for evens happening in the city of Milano, Italy.
Present events in a list.
For each event on the list, provide the title, a brief description, when and where the event is happening, and the url describing the event.
```


Output:
```
### Role and Goal
You are an expert event search and data aggregation assistant. Your primary goal is to search for a list of current and upcoming public events happening in the city of **Milano (Milan), Italy**. Focus on events happening **starting from today, and into the immediate future (the next 7-10 days)**.

### Constraints
1.  **Strictly limit the results** to events occurring *only* in Milano, Italy.
2.  Provide a **minimum of 5** distinct events.
3.  Do not include permanent attractions, ongoing museum exhibitions (unless they have a specific special event/opening on the specified dates), or general city services. Focus on time-bound events like concerts, festivals, markets, special performances, etc.

### Output Format Instructions
Present the information for each event in a clear, numbered list format. For each event, you **must** include the following five data points, using the bolded labels exactly as shown:

1.  **Title:** The full, official name of the event.
2.  **Description:** A concise (1-2 sentence) summary of what the event is.
3.  **When & Where:** The exact date(s) and time(s) of the event, and the full physical address or venue name in Milano.
4.  **URL:** The direct link (URL) to the event's official page for more details, tickets, or booking.

**Example of Desired Format:**

1.  **Title:** [Event Title]
    **Description:** [Brief summary of the event.]
    **When & Where:** [Date(s) and Time(s)] at [Venue Name/Address in Milano]
    **URL:** [Direct URL to event page]

2.  **Title:** [Event Title]
    **Description:** [Brief summary of the event.]
    **When & Where:** [Date(s) and Time(s)] at [Venue Name/Address in Milano]
    **URL:** [Direct URL to event page]
    
... and so on for all 5-15 events.
```



### Configure the model in Open WebUI
Workspace -> Model -> Create a new model
- Model Name
  - Milano Event Scout
- Base Model (from)
  - Gemma3:4b
- Description
  - Scout for events happening today in a Milano
- System prompt
  - The prompt define above
- Prompt Suggestions
  - Returns the list of events happening in Milano today
- Capabilities
  - Select only `Web Search`, `Citation`, `Status updates`
- Default Features
  - Web Search
- Save


### Test the agent
Prompt
```
Events today
```

Analise the output of the initial search

``` bash
docker logs -f openwebui | tspin
```

``` log
open_webui.routers.retrieval:process_web_search:2061 - urls: ['https://www.milanotoday.it/eventi/', 'https://www.yesmilano.it/eventi/tutti-gli-eventi/weekend-milano', 'https://www.eventimilano.it/', 'https://zero.eu/milano/eventi/', 'https://vivimilano.corriere.it/', 'https://www.ticketone.it/city/milano-215/concerti-55/festival-1095/', 'https://www.milanolatinfestival.it/', 'https://www.milanofilmfest.it/', 'https://www.yesmilano.it/eventi/tutti-gli-eventi/concerti-milano', 'https://vivimilano.corriere.it/altri-eventi/feste-e-mercati/', 'https://www.ilsole24ore.com/art/ledru-tiffany-per-nostra-alta-gioielleria-gemme-uniche-ed-eventi-speciali-AHuQTpqC', 'https://www.daagata.it/blog-detail/post/204739/mercato-ittico-di-milano-il-pesce-piu-fresco-di-italia', 'https://www.mercatocentrale.it/news/mercato-centrale-milano-tutti-gli-eventi-di-aprile/', 'https://www.arera.it/amministrazione-trasparente/organizzazione/contatti-telefonici-e-caselle-di-posta']
```




## Create a Press Review agent
Any model will work

### Build the system prompt
Use [Google AI Studio](https://aistudio.google.com/prompts/new_chat) to create a prompt to use for the model in Open WebUI
```
You're an experienced prompt engineer. Your goal is to write a prompt to query a Gemma3 LLM to search for the web about events in the city the user will specify, happening in the current day. Events are presented in a list. For each event on the list, provide the title, a brief description, when and where the event is happening, and the source of the event.
If the user doesn't specify the city, ask for it.
```


Output:
```
```



### Configure the model in Open WebUI
Workspace -> Model -> Create a new model
- Model Name
  - Press Review agent
- Base Model (from)
  - Gemma3:4b
- Description
  - Scout for events happening today in a given city
- System prompt
  - The prompt define above
- Prompt Suggestions
  - Ask to search for events in a given city
- Capabilities
  - Select only `Web Search`, `Citation`, `Status updates`
- Default Features
  - Web Search
- Save
Use the same prompt, but with this new agent, while cheching the Web Search icon is visible in the prompt
```
What are the today’s news for the city of Milan, in Italy? Return a link to the sources you used, the date of the news, a title and a brief summary. Collect at least 10 news from various sources.
```

```
Cerca le notizie di oggi per la città di Milano, in Italia. Le notizie devono essere relative al giorni di oggi, e non al passato. Cerca in almeno 10 diverse fonti. Con le notizie trovate, crea una lista dove per ogni notizia c’è il titolo, una descrizione, il link sorgente, la data della notizia e 4 tag per catalogare la notizia
```


Search for today's news about the city of Pavia, Italy, about the current day. Return a list with the most prominent of them. Each list entry should have title of the next, description of the news, date it refers to and source of the news. Search 15 news




## Additional resources

- It's possible to enable Web Search provide via environmental variables directly in the `docker-compose.yaml` file
  - https://docs.openwebui.com/tutorials/web-search/brave
- [How to Enable Web Search in Open WebUI](https://www.youtube.com/watch?v=fwscnJu_Md0)




## Next session
[Tools](06-tools.md)


