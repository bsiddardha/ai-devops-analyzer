from sentence_transformers import SentenceTransformer

# Load model once (important for performance)
model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_texts(texts):
    """
    Convert list of texts into embeddings
    """
    return model.encode(texts)


def embed_query(query):
    """
    Convert a single query into embedding
    """
    return model.encode([query])[0]




# Optional test
if __name__ == "__main__":
    sample = ["ERROR: DB connection failed"]
    vectors = embed_texts(sample)

    print("Embedding working ✅")
    print("Vector length:", len(vectors[0]))
    print("Sample:", vectors[0][:5])