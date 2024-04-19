# How ML and AI can help community events planning, execution and analysis

Author: Alfredo Morresi

## Prework
- Create a GCP Project
- Enable Vertex AI API
- Enable Cloud Assistant API, to ask questions in the console
- Request access to Imagen 2 via https://docs.google.com/forms/d/1cqt9padvfMgqn23W5FMPTqh7bW1KLkEOsC5G6uC-uuM/viewform



## Planning your event
TODO


## Speaker selection
https://github.com/VinciGit00/Scrapegraph-ai


## Preparing the event

### Generate event description

Prompts to try
- You're a social media manager. You need to write social-media tailored prompt to advertise an event about AngularJS and a new library to create responsive websites.
Create different snippets of text
- The more context you give to Gemini, the better it can understand your request and generate a useful response.
  - Instead of..."Write about a sales job.", try this..."Write a job description for a [job title], including the required skills and experience, as well as a summary of [company name] and the position."
  - Instead of..."Create project plan.", try this..."Create a project plan for the launch of a brand new product. The timeframe should be from now until June 2024."

### Generate event creativity

Resouces
- https://cloud.google.com/vertex-ai/generative-ai/docs/image/overview?hl=en
- https://www.youtube.com/watch?v=pN-RTBq6i3I
- https://cloud.google.com/blog/products/ai-machine-learning/imagen-2-on-vertex-ai-is-now-generally-available

Steps
- In the Google Cloud console, go to the Vertex AI Studio page
- Click Vision Powered by Imagen 
- Click "Generate" to write your prompt


In case you wanna use a different model
- In the Google Cloud console, go to the Vertex AI Model Garden page
- Select StableDiffusion or other models



### Generate voice for podcasts and other media
TODO

## Reporting
### Count your attendees

Resources
- https://cloud.google.com/vertex-ai/generative-ai/docs/start/quickstarts/quickstart-multimodal?hl=en

Steps
- Take a photo of the event attendees
- In the Google Cloud console, go to the Vertex AI Studio page
- Click Multimodal
- Under Sample prompts, locate the prompt titled Extract text from images, and click Open
- The prompt page opens and the prompt is populated in the Prompt field.
- Press "Clear Prompt"
- Select model: gemini-1.0-pro-vision-001 ([more on models](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models?hl=en))
- Upload the picture of the attendees
- Prompt: "How many people are in the picture?"
- Submit the prompt by clicking Submit.
- Enjoy an automatic count of the number of attendees


## At the event

### Ask questions to the speaker
- Prompt Gemini
  - Instead of..."Marketing talking points.", try this..."Give me 12 thoughtful questions to ask a Chief Marketing Officer on their strategy for 2024."
  - As usual, If you want Gemini to perform several related tasks, break them apart into separate prompts. This helps the AI understand the task and provide useful responses.


## Attendees Analysis

Resources
- 

Steps
- Open Gemini
- TODO: get your answers from Bevy
- Ask it if it will summarize a set of data, giving as much specifics as possible (i.e. please summarize this survey data from an internal reading challenge). Paste the data and press enter.