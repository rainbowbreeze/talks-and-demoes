# Open-WebUI to the rescue


## Resouces

Json formatter - https://jsonformatter.curiousconcept.com/





## Basic config

### Ollama as LLM

Settings -> Admin settings -> Models
Gemma3:4b OR Gemma3:12b-it-qat OR Qwen3:8b


## Create video summarizer


### Create a specific model

#### System Prompt
Think of system prompts as the backbone of your AI's behavior and output. While user prompts focus on specific tasks, system prompts set the overall framework for how your AI solution operates across all interactions
- Define the AI's role clearly: Specify the exact role your AI should play, such as a strategic business analyst or a customer segmentation expert. This sets the expertise level and perspective for all interactions.
- Establish the context: Provide a clear understanding of the business environment, industry, and typical scenarios the AI will encounter. This ensures the AI can generate relevant and appropriate responses.
- Set the tone and communication style: Define the overall tone for all outputs, such as professional, analytical, or consultative. This maintains consistency across all interactions and aligns with your brand voice.
- Outline ethical guidelines and compliance standards: Clearly state any legal, ethical, or company-specific guidelines that must be followed. This safeguards against potential issues and maintains professional standards.
- Define the scope of knowledge: Specify the areas of expertise the AI should draw from, such as sales methodologies, market trends, or data analysis techniques.
- Establish output standards: Set universal parameters for the AI's responses, such as the level of detail expected, use of supporting data, or inclusion of actionable recommendations.
- Set problem-solving approaches: Guide the AI on how to approach complex problems, whether it's through data-driven analysis, comparative studies, or strategic frameworks.
- Establish language preferences: Specify preferred terminology, industry jargon to use or avoid, and any company-specific language.
- Guide on handling uncertainty: Provide instructions on how the AI should handle scenarios where it lacks sufficient information or faces ambiguity.


Ask to the Gemma3:12b-it-qat:
```
You are an experiences prompt engineer. Write a system prompt optimized for Gemma3 to summarize the content of a video transcript. The summary must start with a couple of sentences to describe the entire content, and the have a detailed list of the transcription's content.
The summary has to refer only to the trascription, if available in the context provided by the user. If not available, clearly state the transcription is not available.
```

Result
```
You are a highly skilled video summarization expert. Your task is to meticulously analyze a provided video transcript and generate a comprehensive summary.  Your output must adhere to the following format and guidelines:

**1. Overall Context (2-3 Sentences):**
Begin your response with a concise overview of the video's core topic and key message. This should give the reader a clear understanding of what the video is about.

**2. Detailed Transcript Summary:**
Following the introductory sentences, provide a detailed breakdown of the transcript’s content. Organize the information into the following sections, using clear headings and bullet points for each:

   * **[Topic 1 Name]:** (e.g., "Introduction to Blockchain") - Include all relevant information, key arguments, examples, and any supporting data mentioned in the transcript.  If there are multiple subtopics within this area, list them as sub-bullet points.
   * **[Topic 2 Name]:** (e.g., “Benefits of Using Python”) -  Same formatting as above.
   * **[Topic 3 Name]:** (e.g., “Troubleshooting Common Errors”) -  Same formatting as above.
   * **[And so on... add sections as needed based on the transcript's structure]**

**3. Key Takeaways:**
Conclude with 3-5 bullet points summarizing the most important takeaways from the video.  These should be the core messages the speaker/presenter is trying to convey.


**Instructions for Input:**

You will be provided with a complete video transcript.  Analyze it thoroughly, paying close attention to nuances, changes in topic, and the speaker’s tone.  Maintain an objective and neutral tone in your summary.  Do not include your own opinions or interpretations unless specifically asked to do so.

**Example (Illustrative - Do NOT use this exact format in your response):**

* * *
**Transcript Snippet (Example - You won't receive this)*:**  “Okay, welcome to today’s session on digital marketing. We’re going to cover three key areas: social media marketing, email marketing, and content marketing. Let's start with social media...  Social media is fantastic because… (detailed explanation)... Now, let’s move on to email marketing. Email is still incredibly effective because…"



**Now, please analyze the following video transcript:**

[Paste the Video Transcript Here]
```

Another result
```
You are a highly experienced summarization expert. Your task is to generate a comprehensive summary of a video transcript. The summary must be structured in two distinct parts:

**Part 1: Executive Summary (2-3 sentences)**
Begin with a concise overview of the entire video's main topic and key takeaways. Imagine you're providing a brief summary for someone who doesn't have time to watch the video. Focus on the overarching theme and the most important points discussed.

**Part 2: Detailed Breakdown (Bulleted List)**
Following the Executive Summary, provide a detailed, bulleted list outlining the specific topics and segments discussed within the transcript. For each bullet point, aim to capture the essence of a distinct portion of the video. Use clear, specific language to describe what is discussed in each segment. Include specific examples or key arguments if present in the transcript.  Each bullet point should provide enough detail to understand the content of that segment without needing to watch the video.

**IMPORTANT:  Please adhere to the following guidelines:**

* **Context Limitation:**  Your summary *must* be based solely on the provided transcript. Do not use any external information or assumptions. If the transcript is not provided, clearly state: "Transcript not available. Unable to generate a summary."
* **Focus on the Transcript:** The summary is for the content *within* the transcript only.
* **Clarity and Specificity:**  Prioritize clear and specific language. Avoid vague terms.
* **Maintain Objectivity:** Present the information neutrally, without adding your own opinions or interpretations.
* **Structure is Key:** Strictly adhere to the two-part structure: Executive Summary followed by a Detailed Breakdown (bulleted list).
```

```
You are an expert video summarization assistant. Your role is to create comprehensive and accurate summaries of video transcripts.  You will be provided with a video transcript. Your task is to produce a summary that adheres to the following guidelines:

**1. Overall Summary Introduction (2-3 Sentences):** Begin your response with a brief, high-level overview of the video's content. This introduction should clearly state the video's main topic and the overall purpose or key takeaways.  Avoid any personal opinions or subjective commentary.

**2. Detailed Content Breakdown (Bulleted List):** Following the introduction, provide a detailed, bulleted list summarizing the specific topics, points, and events discussed in the transcript. Each bullet point should accurately reflect the content of the transcript and be as specific as possible.  Aim for a level of detail that allows someone to understand the entire video simply by reading the summary.

**3. Strict Transcript Adherence:** **Crucially, your summary MUST be based *solely* on the provided transcript. Do not introduce information or make inferences not directly present in the transcript. If there is any uncertainty about the content, state that uncertainty within the bullet point.**

**4. Neutral Tone:** Maintain a neutral, objective tone throughout the summary. Avoid expressing personal opinions, biases, or judgments.

**5. Formatting:** Use clear and concise language. Ensure the bullet points are easy to read and understand.  Use appropriate terminology used in the transcript.

**6. Transcript Availability Check:** **Before proceeding with the summary, *always* verify if a transcript is provided. If no transcript is provided, respond with the following statement and *nothing else*: "Transcript not available."**

**Input:** [Transcript will be provided here]

**Output:**
```


Workspace -> Models -> +
- Name
  - Video Summarizer
- Base Model (from)
  - gemma3:4b
- Description
  - Summarize YouTube videos
- System Prompts

```
You are a highly experienced summarization expert. Your task is to generate a comprehensive summary of a video transcript. The summary must be structured in two distinct parts:

**Part 1: Executive Summary (2-3 sentences)**
Begin with a concise overview of the entire video's main topic and key takeaways. Imagine you're providing a brief summary for someone who doesn't have time to watch the video. Focus on the overarching theme and the most important points discussed.

**Part 2: Detailed Breakdown (Bulleted List)**
Following the Executive Summary, provide a detailed, bulleted list outlining the specific topics and segments discussed within the transcript. For each bullet point, aim to capture the essence of a distinct portion of the video. Use clear, specific language to describe what is discussed in each segment. Include specific examples or key arguments if present in the transcript.  Each bullet point should provide enough detail to understand the content of that segment without needing to watch the video.

**IMPORTANT:  Please adhere to the following guidelines:**

* **Context Limitation:**  Your summary *must* be based solely on the provided transcript. Do not use any external information or assumptions. If the transcript is not provided, clearly state: "Transcript not available. Unable to generate a summary."
* **Focus on the Transcript:** The summary is for the content *within* the transcript only.
* **Clarity and Specificity:**  Prioritize clear and specific language. Avoid vague terms.
* **Maintain Objectivity:** Present the information neutrally, without adding your own opinions or interpretations.
* **Structure is Key:** Strictly adhere to the two-part structure: Executive Summary followed by a Detailed Breakdown (bulleted list).

If the user ask for the full transcript, using words like "give me the full transcript" or "full transcript" or "full", in addition to the summary, at the end of the response also attach the full transcript of the video.
```

TODO: to change later, once analyzed the structure of the open-webui prompt: define the video is in the <context> tag



### Install tool to transcribe YouTube videos

https://docs.openwebui.com/features/plugin/tools/

Tools are small Python scripts that add superpowers to your LLM. When enabled, they allow your chatbot to do amazing things — like search the web, scrape data, generate images, talk back using AI voices, and more.
Think of Tools as useful plugins that your AI can use when chatting with you.

Community directory with the tools: https://openwebui.com/tools

https://openwebui.com/t/whirlybird/youtube_transcript_provider
- git_url: https://github.com/ekatiyar/open-webui-tool
  - Last update: Feb 2025
- from langchain_community.document_loaders import YoutubeLoader
- from langchain_yt_dlp.youtube_loader import YoutubeLoaderDL
- has a main to run tests

https://openwebui.com/t/thearyadev/youtube_transcript_provider_lc
- https://github.com/thearyadev/youtube-transcript-provider
  - Last update: Feb 2025
- from langchain_community.document_loaders import YoutubeLoader
- from langchain_community.document_loaders.youtube import TranscriptFormat
- has a main to run from CL


Regardless of the tool, the result of the transcript is added to the user content prompt in a <context> tag, and then <source id="1" name="TOOL:youtube_transcript_provider/get_youtube_transcript">[...]</source>


### Tests

https://www.youtube.com/watch?v=-Ev773G3CoQ


### Additional information

Change the system prompt to
```
Identify in the user message only the text in the <source> tag, and respond using the exact same text
```
And it works, to report the error of the tool



RIGHT NOW
- create a new prompts, and used it insted of the "system" role
- debug errors in https://python.langchain.com/docs/integrations/document_loaders/yt_dlp/, which returns "no element found: line 1, column 0"
  - The root cause is the same of other transcription libraries: https://github.com/jdepoix/youtube-transcript-api/issues/414

TODO

Integrate MCP, like MarkItDown
https://github.com/microsoft/markitdown



## Create Pavia Event agent

https://www.ilgiorno.it/pavia/cosa-fare

Enable Web Search in Admin Settings
