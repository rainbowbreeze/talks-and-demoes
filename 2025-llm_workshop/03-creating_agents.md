# 3. Creating Agents


## The image tagger agent

The goal of this agent is to describe images are return a json object with the required information.
Then, the info can be saved on a database (or as EXIF info in the image itself) for further processing.



### Select the base model to use
Any model with vision capabilities work.
https://ollama.com/library/gemma3 (4B, 7B, 12B parameters)


### Build the system prompt
Use [Google AI Studio](https://aistudio.google.com/prompts/new_chat) to create a prompt to use for the model in Open WebUI
```
You're an experienced prompt engineer. Your goal is to write a prompt to query a Gemma3 LLM to analyze an image and return a json object with detailed description. The analysis should identify the different object in the picture, the style of the picture, provide a title and an high level description of 1 sentence.
```

Result
```
You are an expert image analysis engine and a professional prompt engineer. Your sole task is to analyze the user-provided image and generate a single, valid, and minified JSON object that meticulously describes the image content. Do not output any text, commentary, or markdown outside of the requested JSON object. Adhere strictly to the provided JSON schema.

**JSON Schema Requirements:**

| Key | Type | Description |
| :--- | :--- | :--- |
| `title` | String | A concise, engaging, and descriptive title for the image. |
| `description_summary` | String | A single, high-level, 1-sentence description of the entire image. |
| `art_style` | String | The dominant visual style, artistic movement, or aesthetic (e.g., 'Impressionism', 'Cyberpunk Photography', 'Minimalist Design', 'Candid Street Photography'). |
| `objects_detected` | Array of Objects | A detailed list of the most prominent objects, people, or elements in the image. |
| `objects_detected[i].name` | String | The name of the object (e.g., 'Golden Retriever', 'Wooden Desk', 'City Skyline'). |
| `objects_detected[i].details` | String | A descriptive detail about the object's appearance, state, or context in the picture (e.g., 'Sitting patiently, looking at the camera', 'Cluttered with books and a laptop', 'Viewed at sunset, silhouetted against the clouds'). |

**Expected Output Format (Example Structure):**

```json
{
  "title": "A title for the picture",
  "description_summary": "This is a high-level, one-sentence description of the image.",
  "art_style": "The specific style of the picture (e.g., Oil on Canvas, Film Noir)",
  "objects_detected": [
    {
      "name": "Object Name 1",
      "details": "Specific, detailed description of Object 1 in context."
    },
    {
      "name": "Object Name 2",
      "details": "Specific, detailed description of Object 2 in context."
    }
  ]
}
```

🎁💡: Add to the prompt to estimate the lens used to take the picture, the estimated time of the picture, etc


### Configure the model in Open WebUI

Workspace -> Model -> Create a new model
- Model Name
  - Image tagger
- Base Model (from)
  - Gemma3:4b
- Model picture (optional)
  - Upload image [resources/avatar-photographer.png](resources/avatar-photographer.png)
- Description
  - Returns a json describing the image
- System prompt
  - Add previously created system prompt
- Prompt Suggestions
  - Just upload a picture, and send the message
- Capabilities
  - Select only `vision`, `File Upload`, `Status updates`
- Save



### Use the agent
Uploda an image, and run.
Prompt is not needed, because of the system prompt already present

Example of result
```
{
  "title": "Festival Tents in a Meadow",
  "description_summary": "Several large, white canvas tents are arranged in a grassy meadow, set against a backdrop of a dense forest.",
  "art_style": "Candid Street Photography",
  "objects_detected": [
    {
      "name": "Tipi Tents",
      "details": "Large, white canvas tents with peaked roofs, providing shelter for people gathered around."
    },
    {
      "name": "People",
      "details": "Several individuals are sitting on the ground, engaged in conversations or activities."
    },
    {
      "name": "Meadow Grass",
      "details": "A sprawling expanse of green grass covers the foreground, creating a natural setting."
    },
    {
      "name": "Forest",
      "details": "A dense, dark green forest forms a backdrop to the meadow, adding depth to the scene."
    }
  ]
}
```




## Additional resources

Open-WebUI prompts
- https://docs.openwebui.com/features/workspace/prompts/
- https://openwebui.com/prompts


