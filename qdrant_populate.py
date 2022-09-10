import numpy as np
#import json
import os
from sentence_transformers import SentenceTransformer
from time import time
from qdrant_client import QdrantClient


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

result = list()
sentences = list()
for file in os.listdir('logs/'):
    info = {'filename': file, 'content': open_file('logs/%s' % file).strip()}
    result.append(info)
    sentences.append(info['content'])

#print(result)

start = time()
model = SentenceTransformer('all-mpnet-base-v2')  # https://www.sbert.net/docs/pretrained_models.html
sentence_embeddings = model.encode(sentences)
print(time() - start)
print(sentence_embeddings)



qdrant_client = QdrantClient(host='localhost', port=6333)

qdrant_client.upload_collection(
    collection_name='startups',
    vectors=sentence_embeddings,
    payload=result,
    ids=None,  # Vector ids will be assigned automatically
    batch_size=256  # How many vectors will be uploaded in a single request?
)