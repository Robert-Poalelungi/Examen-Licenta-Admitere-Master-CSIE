import re

def transform(path):
    with open(path, encoding="utf-8") as f:
        content = f.read()

    # Split into question blocks by "---" separator
    # Each question block looks like:
    # ### Întrebarea N  (or ### Question N)
    # ...text...
    # **Răspuns corect: ...**
    # **Explicație:** ...
    # ---

    # Strategy: find each block between ### headings
    # Replace the "Răspuns corect" + "Explicație" section with <details>

    # Pattern: match **Răspuns corect:...** line(s) and **Explicație:**...
    # We want to wrap from "**Răspuns corect" to end of explanation (before "---" or next "###")

    # Match Romanian style
    def replace_ro(m):
        answer = m.group(1).strip()
        explanation = m.group(2).strip()
        return f"""
<details>
<summary>🔍 Răspuns și explicație</summary>

**Răspuns corect: {answer}**

**Explicație:** {explanation}

</details>"""

    # Match English style
    def replace_en(m):
        answer = m.group(1).strip()
        explanation = m.group(2).strip()
        return f"""
<details>
<summary>🔍 Answer & explanation</summary>

**Correct answer: {answer}**

**Explanation:** {explanation}

</details>"""

    # Romanian pattern
    content = re.sub(
        r'\*\*Răspuns corect:\s*(.*?)\*\*\s*\n+\*\*Explicație:\*\*\s*(.*?)(?=\n---|\n###|\Z)',
        replace_ro,
        content,
        flags=re.DOTALL
    )

    # English pattern
    content = re.sub(
        r'\*\*Correct [Aa]nswer:\s*(.*?)\*\*\s*\n+\*\*Explanation:\*\*\s*(.*?)(?=\n---|\n###|\Z)',
        replace_en,
        content,
        flags=re.DOTALL
    )

    # Also handle single-line explanations (no newline before ---)
    # Romanian inline
    content = re.sub(
        r'\*\*Răspuns corect:\s*(.*?)\*\*\n\*\*Explicație:\*\*\s*(.*?)\n',
        lambda m: f'\n<details>\n<summary>🔍 Răspuns și explicație</summary>\n\n**Răspuns corect: {m.group(1).strip()}**\n\n**Explicație:** {m.group(2).strip()}\n\n</details>\n',
        content
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Done: {path}")

base = r"C:\Users\Robert\Desktop\Examen-Licenta-Admitere-Master-CSIE\Admitere Master"
transform(base + r"\CSIE_3\Rezolvari.md")
transform(base + r"\CSIE_4\Rezolvari.md")
print("ALL DONE")
