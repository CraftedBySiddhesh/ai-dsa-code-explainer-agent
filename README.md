<div align="center">

# DSA Notebook Builder
### Text / Markdown → Jupyter Notebook Generator for DSA Practice (College + Interview)

<p>
  <a href="https://github.com/CraftedBySiddhesh/code-with-siddhesh/actions/workflows/ci.yml">
    <img src="https://github.com/CraftedBySiddhesh/code-with-siddhesh/actions/workflows/ci.yml/badge.svg" alt="CI Status" />
  </a>
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue.svg" />
  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B.svg" />
  <img src="https://img.shields.io/badge/Output-Jupyter%20Notebook-blue.svg" />
  <img src="https://img.shields.io/badge/Use-College%20Practice-success.svg" />
  <img src="https://img.shields.io/badge/Engine-Groq-blueviolet.svg" />
</p>

<b>Paste problems once.</b> Generate a reusable Jupyter notebook with explanation, dry-run, clean Python solution, and complexity.

</div>

---

## Why this project exists

Most students practice DSA like this:

- solve quickly  
- copy code  
- forget reasoning  

**DSA Notebook Builder** converts raw practice into **long-term revision material** by enforcing a structured notebook format.

---

## What the notebook contains (per problem)

- **Problem Explanation** – inputs, outputs, constraints, edge cases  
- **Intuition / Thought Process** – brute force → optimized insight  
- **Step-by-Step Dry Run** – example walkthrough  
- **Solution**
  - Approach explanation  
  - Single clean Python implementation  
- **Time & Space Complexity** – Big-O with reasoning  

---

## Input methods

### Option 1 — Text box (single or multiple problems)

- Paste **one** problem → auto-treated as single problem
- Paste **multiple** problems → separate using:
  - `##` headings, or
  - `---` on its own line

Example:
```md
## Problem 1
<description>

---

## Problem 2
<description>
```

### Option 2 — Upload `.md` file

- Same separators (`##` or `---`)
- No scraping
- No external links required

---

## Output

- One downloadable notebook: `solutions_notebook.ipynb`
- Markdown + code cells per problem
- Consistent structure across problems

---

## Limits

- Max **5 problems per run**
- Python-only solutions
- Notebook output only

---

## Quickstart (Windows)

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Edit `.env`:
```env
GROQ_API_KEY=YOUR_API_KEY
GROQ_MODEL=llama-3.1-70b-versatile
```

Run:
```bash
python -m streamlit run app.py
```

Open:
```
http://localhost:8501
```

---

## Project structure

```text
app.py
agent/
  agent_core.py
  llm.py
  prompts.py
  md_parser.py
  notebook_builder.py
.github/workflows/ci.yml
.pre-commit-config.yaml
pyproject.toml
```

---

## Reliability guarantees

- Uses only user-provided content
- No assumptions on missing constraints
- Validation + repair loop for notebook correctness
- Never crashes on malformed model output

---

## Repo hygiene

Included by default:
- `.gitignore`
- Pre-commit hooks (ruff, black)
- CI checks before merge
- PR template + contribution guide

---

## Intended usage

- College DSA practice
- Interview revision
- Lab notebooks
- Personal study

Educational use only.

---

## Author

**CraftedBySiddhesh**