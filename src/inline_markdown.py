import re

from textnode import (
    TextNode,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_type_link,
    text_type_text,
)


def extract_markdown_images(text):
    return re.findall(r"!\[([^\]]*)\]\(([^)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[([^\]]*)\]\(([^)]*)\)", text)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")

        for i in range(0, len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        current_text = old_node.text
        image_tups = extract_markdown_images(current_text)
        if len(image_tups) == 0:
            new_nodes.append(old_node)
            continue
        for image_tup in image_tups:
            sections = current_text.split(f"![{image_tup[0]}]({image_tup[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(image_tup[0], text_type_image, image_tup[1]))
            current_text = sections[1]
        if current_text != "":
            new_nodes.append(TextNode(current_text, text_type_text))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        current_text = old_node.text
        link_tups = extract_markdown_links(current_text)
        if len(link_tups) == 0:
            new_nodes.append(old_node)
            continue
        for link_tup in link_tups:
            sections = current_text.split(f"[{link_tup[0]}]({link_tup[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(link_tup[0], text_type_link, link_tup[1]))
            current_text = sections[1]
        if current_text != "":
            new_nodes.append(TextNode(current_text, text_type_text))
    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
