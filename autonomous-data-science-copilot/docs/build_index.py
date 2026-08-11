from pathlib import Path
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = []

for file in [
    "docs/pandas_docs.txt",
    "docs/python_docs.txt"
]:

    text = Path(file).read_text(encoding="utf-8")

    chunks = [
        text[i:i+800]
        for i in range(0, len(text), 800)
    ]

    documents.extend(chunks)

embeddings = model.encode(
    documents,
    convert_to_numpy=True
)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

faiss.write_index(index, "docs/faiss.index")

with open("docs/chunks.pkl", "wb") as f:
    pickle.dump(documents, f)

print("Index created successfully!")