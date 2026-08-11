import faiss
import pickle
from sentence_transformers import SentenceTransformer


class RAGService:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        self.index = faiss.read_index(
            "docs/faiss.index"
        )

        with open(
            "docs/chunks.pkl",
            "rb"
        ) as f:

            self.documents = pickle.load(f)

    def retrieve(self, query, k=3):

        embedding = self.model.encode(
            [query]
        )

        distances, indices = self.index.search(
            embedding,
            k
        )

        docs = []

        for idx in indices[0]:

            docs.append(
                self.documents[idx]
            )

        return "\n\n".join(docs)