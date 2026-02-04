import nbformat as nbf

def build_notebook(sections):
    nb = nbf.v4.new_notebook()
    nb.cells.append(nbf.v4.new_markdown_cell("# Algorithm Notebook"))
    for title, md in sections:
        nb.cells.append(nbf.v4.new_markdown_cell(f"## {title}".strip()))
        if "```python" in md:
            before, after = md.split("```python", 1)
            code, rest = after.split("```", 1)
            if before.strip():
                nb.cells.append(nbf.v4.new_markdown_cell(before.strip()))
            nb.cells.append(nbf.v4.new_code_cell(code.strip()))
            if rest.strip():
                nb.cells.append(nbf.v4.new_markdown_cell(rest.strip()))
        else:
            nb.cells.append(nbf.v4.new_markdown_cell(md.strip() or "**Empty output**"))
    return nb
