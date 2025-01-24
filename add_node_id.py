from llama_index.core import Document
# Create a Document with a custom node ID
document = Document(text="Your document text here", id_="custom_node_id")
# Access the node ID
print("Node ID:", document.id_)
