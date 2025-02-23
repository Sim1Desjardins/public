from textnode import TextNode, TextType

def main():
    # Create a TextNode instance here with some test values
    test_node = TextNode(
        "This is a text node",
        TextType.BOLD_TEXT,
        "https://www.boot.dev"
    )
    # Print the instance
    print(test_node)

if __name__ == "__main__":
    main()