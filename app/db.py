import faiss
import numpy as np

# Create FAISS index (384 = embedding size)
index = faiss.IndexFlatL2(384)

# Map index → text
id_to_text = {}


def add_embeddings(vectors, texts):
    global index, id_to_text

    vectors = np.array(vectors).astype("float32")

    start_id = len(id_to_text)

    index.add(vectors)

    for i, text in enumerate(texts):
        id_to_text[start_id + i] = text


def search(query_vector, k=3):
    query_vector = np.array([query_vector]).astype("float32")

    distances, indices = index.search(query_vector, k)

    results = []
    for idx in indices[0]:
        if idx in id_to_text:
            results.append(id_to_text[idx])

    return results