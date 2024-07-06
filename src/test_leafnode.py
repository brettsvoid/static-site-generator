import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_raise_error_if_no_value(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_with_no_tag(self):
        node = LeafNode(None, "This is a leaf node")
        self.assertEqual(node.to_html(), "This is a leaf node")

    def test_to_html(self):
        node = LeafNode("p", "This is a leaf node")
        self.assertEqual(node.to_html(), "<p>This is a leaf node</p>")


if __name__ == "__main__":
    unittest.main()
