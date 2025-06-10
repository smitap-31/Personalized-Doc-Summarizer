import faiss
import numpy as np

class VectorStore():
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.text_chunks = []

    def add(self, embeddings, text_chunks):
        """
        Adds embeddings and corresponding text chunks to the vector store.

        Args:
            embeddings (np.ndarray): The embeddings to be added.
            text_chunks (list): The corresponding text chunks.
        """
        self.index.add(np.array(embeddings).astype(np.float32))
        self.text_chunks.extend(text_chunks)

    def search(self, query_embedding, k=5):
        """
        Searches for the k nearest neighbors of a query embedding.

        Args:
            query_embedding (np.ndarray): The embedding of the query.
            k (int): The number of nearest neighbors to return.

        Returns:
            list: A list of tuples containing the indices and distances of the nearest neighbors.
        """
        distances, indices = self.index.search(np.array([query_embedding]).astype(np.float32), k)
        return [self.text_chunks[i] for i in indices[0]]