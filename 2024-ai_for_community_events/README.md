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


## Attendees Analysis
TODO