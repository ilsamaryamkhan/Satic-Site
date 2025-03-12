from src.textnode import TextNode, TextType

def main():
    # Creating a TextNode object with sample data
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.google.com")
    
    # Printing the TextNode object to check its output
    print(node)

if __name__ == "__main__":
    main()
