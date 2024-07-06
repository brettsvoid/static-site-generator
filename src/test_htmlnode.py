import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"style": "color: red"})
        self.assertEqual(node.props_to_html(), ' style="color: red"')

    def test_repr(self):
        node = HTMLNode("h1", "This is an HTML node", None, {"style": "color: red"})
        self.assertEqual(
            "HTMLNode(h1, This is an HTML node, None, {'style': 'color: red'})",
            repr(node),
        )


if __name__ == "__main__":
    unittest.main()
