# How ML and AI can help community events planning, execution and analysis

Author: Alfredo Morresi

## Planning your event
TODO

## Preparing the event


### Generate event description and creativity
TODO

## Reporting
### Count your attendees

Resources
* https://cloud.google.com/vertex-ai/generative-ai/docs/start/quickstarts/quickstart-multimodal?hl=en

Steps
* Take a photo of the event attendees
* In the Google Cloud console, go to the Vertex AI Studio page
* Click Multimodal
* Under Sample prompts, locate the prompt titled Extract text from images, and click Open
* The prompt page opens and the prompt is populated in the Prompt field.
* Press "Clear Prompt"
* Select model: gemini-1.0-pro-vision-001 ([more on models](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models?hl=en))
* Upload the picture of the attendees
* Prompt: "How many people are in the picture?"
* Submit the prompt by clicking Submit.
* Enjoy an automatic count of the number of attendees


## Attendees Analysis
TODO