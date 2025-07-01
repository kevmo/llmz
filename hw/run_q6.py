import numpy as np
from fastembed import TextEmbedding
import requests
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

# Fetch documents
docs_url = 'https://github.com/alexeygrigorev/llm-rag-workshop/raw/main/notebooks/documents.json'
docs_response = requests.get(docs_url)
documents_raw = docs_response.json()

# Filter only ML Zoomcamp documents
documents = []
for course in documents_raw:
    course_name = course['course']
    if course_name != 'machine-learning-zoomcamp':
        continue
    
    for doc in course['documents']:
        doc['course'] = course_name
        documents.append(doc)

print(f"Found {len(documents)} ML Zoomcamp documents")

# Initialize Qdrant client (in-memory mode)
client = QdrantClient(":memory:")

# Create collection with the BAAI/bge-small-en model dimensions (384)
collection_name = "ml_zoomcamp_faq"
client.create_collection(
    collection_name=collection_name,
    vectors_config=VectorParams(size=384, distance=Distance.COSINE)
)

# Initialize the BAAI/bge-small-en embedding model
embedding_model_q6 = TextEmbedding('BAAI/bge-small-en')

# Generate embeddings for all documents
print("Generating embeddings...")
points = []
for idx, doc in enumerate(documents):
    # Combine question and text as specified
    text = doc['question'] + ' ' + doc['text']
    
    # Generate embedding
    embedding = list(embedding_model_q6.embed([text]))[0]
    
    # Create point for Qdrant
    point = PointStruct(
        id=idx,
        vector=embedding.tolist(),
        payload=doc
    )
    points.append(point)

# Upload points to Qdrant
client.upsert(
    collection_name=collection_name,
    points=points
)

print(f"Indexed {len(points)} documents in Qdrant")

# Query with the Q1 question
query_text = 'I just discovered the course. Can I join now?'

# Generate embedding for the query
query_embedding = list(embedding_model_q6.embed([query_text]))[0]

# Search in Qdrant
search_results = client.search(
    collection_name=collection_name,
    query_vector=query_embedding.tolist(),
    limit=5
)

# Display results
print(f"\nQuery: {query_text}\n")
print("Top 5 results:")
for i, result in enumerate(search_results):
    print(f"\n{i+1}. Score: {result.score:.6f}")
    print(f"   Question: {result.payload['question']}")
    print(f"   Text: {result.payload['text'][:100]}...")

# Get the highest score
highest_score = search_results[0].score if search_results else 0
print(f"\n\nHighest score: {highest_score:.6f}")