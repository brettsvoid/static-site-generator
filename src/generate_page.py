import os

from block_markdown import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            _, title = line.split("# ")
            return title

    raise ValueError("Page needs a single H1 header")


def generate_page(from_path, template_path, dest_path):
    print(f"* {from_path} {template_path} -> {dest_path}")
    with open(from_path, encoding="utf-8") as f:
        markdown = f.read()
    with open(template_path, encoding="utf-8") as f:
        template = f.read()

    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dir = os.path.dirname(dest_path)
    if dir != "":
        os.makedirs(dir, exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(template)
