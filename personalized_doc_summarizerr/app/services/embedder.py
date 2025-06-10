from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embeddings(text_chunks):
    """
    Generates embeddings for a list of text chunks using a pre-trained SentenceTransformer model.

    Args:
        text_chunks (list): A list of text strings to be embedded.

    Returns:
        list: A list of embeddings corresponding to the input text chunks.
    """
    return model.encode(text_chunks, show_progress_bar=True, convert_to_tensor=False)