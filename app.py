import nbformat as nbf
import streamlit as st
from dotenv import load_dotenv

from agent.agent_core import NotebookAgent
from agent.md_parser import ensure_single_problem, split_problems
from agent.notebook_builder import build_notebook

load_dotenv()

st.set_page_config(page_title="AI DSA Code Explainer", layout="wide")
st.title("AI DSA Code Explainer")
st.caption("Code with Siddhesh • Text/MD → Jupyter Notebook generator for DSA practice (Groq)")

max_n = st.number_input("Max problems to process (per run)", min_value=1, max_value=20, value=20, step=1)
show_debug = st.checkbox("Show debug JSON per problem", value=False)

tab_text, tab_md = st.tabs(["Text input", "Upload .md file"])

md_text = None

with tab_text:
    st.subheader("Paste one problem or multiple problems")
    st.write(
        "For multiple problems, separate with `##` headings or `---` lines. For a single problem, paste plain text."
    )
    text_in = st.text_area("Paste problem text here", height=320, placeholder="Paste your problem statement(s) here...")
    if text_in and text_in.strip():
        md_text = ensure_single_problem(text_in)

with tab_md:
    st.subheader("Upload a Markdown file")
    uploaded = st.file_uploader("Upload problems.md", type=["md"])
    if uploaded:
        md_text = uploaded.read().decode("utf-8", errors="replace")

problems = []
if md_text:
    problems = split_problems(md_text)
    st.info(f"Detected {len(problems)} problem block(s).")
    if problems:
        st.code((problems[0][:1200] + ("\n..." if len(problems[0]) > 1200 else "")), language="markdown")

run = st.button("Generate Notebook", type="primary", disabled=not md_text)

if run and md_text:
    blocks = split_problems(md_text)[: int(max_n)]
    agent = NotebookAgent(repair_rounds=2)

    sections = []
    debug = []

    for i, pmd in enumerate(blocks, start=1):
        st.info(f"Processing {i}/{len(blocks)}")
        title, out_md, meta = agent.run_one(pmd)
        sections.append((title, out_md))
        debug.append({"title": title, **meta})

    nb = build_notebook(sections)
    data = nbf.writes(nb).encode("utf-8")

    st.success("Notebook generated.")
    st.download_button(
        "Download .ipynb",
        data,
        "solutions_notebook.ipynb",
        mime="application/x-ipynb+json",
    )

    if show_debug:
        st.json(debug)
