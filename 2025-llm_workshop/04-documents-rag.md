# 04. Documents and RAG in Open WebUI


## What is RAG



## Passing a document to provide context

Create a new chat with a model like gemma3:4b or qwen3:8b.  

Ask simple questions on Pokemon Trading card game, like
```
What are the energies in the Pokemon card game?

What is a Sudden Death in the Pokemon card game?
```

As you can see, the model knows how to play Pokemon.

But a Sudden Death is something different, and defined in page 21 of the [Pokemon Trading Card rulebook](resources/pokemon-training_card_rulebook_en.pdf).


In the prompt, upload the [Pokemon Trading Card rulebook](resources/pokemon-training_card_rulebook_en.pdf), and ask the same question than before:
```
What is a Sudden Death in the Pokemon card game?
```

This time the reply is different, and aligned with the manual




## Create a permanent knowledge base

To make the knowledge "permanent" in the model, we need to create a "Knowledge repository"

Workspace -> Knowledge -> New Knowledge
- Name of the knowledge base
  - Pokemon secrets
- Description
  - All about pokemon game
- Visibility
  - Public

In the Knowledge page -> Add a Collection -> Upload files
- Upload [Pokemon Trading Card rulebook](resources/pokemon-training_card_rulebook_en.pdf) and [Pokemon Pla! Tournament rulebook](resources/play-pokemon-tournament-rules-handbook-en.pdf)

System prompt for the agent
```
**ROLE:** You are the ultimate Pokémon Professor and an encyclopedic authority on the entire Pokémon franchise (including games, anime, TCG, lore, history, spin-offs, and characters from all generations).

**TASK:** Your sole purpose is to provide the most accurate, detailed, and insightful answers possible to any question related to Pokémon.

**STRICT CONSTRAINT (Crucial):**
You **MUST NOT** answer questions on any topic other than Pokémon. This includes other video game franchises, history, science, general knowledge, math, or any other non-Pokémon subject.

**REFUSAL PROTOCOL:**
If a question is asked that is *not* about Pokémon, you **must** courteously decline the request and state your purpose. You must use the following exact response template for any off-topic question:

**"I apologize, but my expertise is strictly limited to the world of Pokémon. Please ask me a question about a Pokémon, character, game, or any related lore."**

**FUN FACT**
Every time you reply to a question, at the end also provide a fun or interesting fact about the Pokémon world, using the format "💡 <FACT HERE>"
```


Workspace -> Models -> New Model
- Model Name
  - Pokemon Expert
- Base Model (from)
  - Gemma3:4b
- Model picture (optional)
  - Upload image [resources/avatar-pokemon.png](resources/avatar-pokemon.png)
- Description
  - A Pokemon buddy that knows everything about Pokemon game world
- System prompt
  - The prompt above
- Knowledge
  - Select Knowledge -> Pokemon secrets
- Prompt Suggestions
  - Ask me anything about the Pokemon world
- Capabilities
  - Select only `vision`, `File Upload`, `Citations`, `Status updates`
- Save


Ask the question
```
What is a Sudden Death in the Pokemon card game?
```