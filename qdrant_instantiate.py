# Import client library
from qdrant_client import QdrantClient

qdrant_client = QdrantClient(host='localhost', port=6333)

qdrant_client.recreate_collection(
    collection_name='startups', 
    vector_size=768, 
    distance="Cosine"
)