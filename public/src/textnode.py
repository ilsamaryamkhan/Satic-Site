from enum import Enum

class TextType(Enum):
    """Enum for different types of text nodes"""
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    """Represents a text node with type and optional URL"""
    
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        """Checks if two TextNode objects are equal"""
        if not isinstance(other, TextNode):
            return False
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        """Returns a string representation of the TextNode"""
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
