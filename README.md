
## Journal Watch Assistant
- Judge whether newly published papers or preprints are relevant to the lab, mainly based on title and abstract (and url/full text if accessible).
- Provide an overview if a paper is relevant.
- Note: the current version uses an API client (probably) without full web search support. Output quality depends heavily on the system prompt, so there is still plenty of room to refine it.


### Preparation
You need an API key for an LLM model. This example uses Deepseek:
https://api-docs.deepseek.com/zh-cn/, compatible with the OpenAI client.

Recommended settings: deepseek-v4-flash, reasoning enabled, reasoning_effort=high (see https://api-docs.deepseek.com/zh-cn/guides/thinking_mode). The cost is under ¥1 for a week of journal and bioRxiv scans.
- Deepseek is also compatible with the Anthropic client: https://api-docs.deepseek.com/zh-cn/guides/anthropic_api
- A Gemini API format is included and requires only minimal replacement.

Create a `.env` file (rename from `.env.example`) and fill in your API key:

```bash
mv .env.example .env
```

Then edit `.env`:

```ini
API_KEY=your_key_here
BASE_URL=https://api.deepseek.com
MODEL_NAME=deepseek-v4-flash
TIMEOUT_SECONDS=120
```

### Extraction tools
- bioRxiv
- RSS feeds for journals
- Crossref (to expand truncated RSS abstracts)
- Europe PMC (full text; not wired into the pipeline yet)

### Run
Main entry script: `python lab_paper_tracker_openai.py`

Output documents:
- Log (.txt): reasoning and outputs. It is recommended to review logs to validate accuracy.
- Report (.md): the final human-readable report.

### Future improvements
- More detailed lab interest descriptions in the prompt
- Few-shot prompt tuning with 1-2 exemplar papers per direction
- Add a prefilter stage, then do full-text analysis
- Move to an agent framework with memory and web search