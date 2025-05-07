# Agentic AI Research Assistant

This project implements a multi-agent system using CrewAI and Serper.dev to perform internet research, summarize findings, and validate the results.

## Author
**Sujith Somanunnithan**

---

## 📁 Folder Structure

```
project/
├── .env                      # API keys for OpenAI and Serper.dev
├── research_crew.py          # Main entry point for running the research crew
├── notebook.ipynb            # Jupyter notebook to test the assistant
└── config/
    ├── agents.yaml           # Agent definitions (roles, goals, backstories)
    └── tasks.yaml            # Task flow and dependencies
```

---

## ⚙️ Requirements

Install dependencies:
```bash
pip install -r requirements.txt
```

Example `requirements.txt`:
```
crewai
crewai-tools
openai
python-dotenv
PyYAML
```

---

## 🔐 Environment Setup

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_key_here
SERPER_API_KEY=your_serper_api_key_here
```

---

## 🚀 How to Test

### Option 1: CLI (Python script)
```bash
python research_crew.py
```

### Option 2: Notebook
Open `notebook.ipynb` and run:
```python
from research_crew import run_research

topic = "AI applications in climate change adaptation"
output = run_research(topic)
print(output)
```

---

## ✅ Outputs

- The result will include a fact-checked summary of the given topic based on real-time web search using Serper.dev.
