import unittest

from textnode import TextNode, TextType

from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

        # Test case 1: No props
        node = HTMLNode(props=None)
        print(node.props_to_html())  # Expected output: ""

        # Test case 2: Single prop
        node = HTMLNode(props={"href": "https://www.example.com"})
        print(node.props_to_html())  # Expected output: ' href="https://www.example.com"'

        # Test case 3: Multiple props
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        print(node.props_to_html())  # Expected output: ' href="https://www.google.com" target="_blank"'

if __name__ == "__main__":
    unittest.main()