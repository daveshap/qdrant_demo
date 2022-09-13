import os
import json
import tensorflow_hub as hub
import textwrap
from uuid import uuid4
from time import time


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


def save_data(payload):
    filename = '%s.json' % str(uuid4())
    with open('data/%s' % filename, 'w', encoding='utf-8') as outfile:
        json.dump(payload, outfile, ensure_ascii=False, sort_keys=True, indent=1)


if __name__ == '__main__':
    embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder-large/5")  # USEv5 is about 100x faster than 4
    files = os.listdir('contexts/')
    #print(files)
    overall_start = time()
    times = list()
    for file in files:
        #print(file)
        start = time()
        text = open_file('contexts/%s' % file)
        chunks = textwrap.wrap(text, 1000)  # break the file contents up into chunks of 1000 characters (always a list)
        embeddings = embed(chunks)
        vectors = embeddings.numpy().tolist()  # convert to JSON serializable object
        for i in list(range(0, len(chunks))):
            #print(chunks[i], vectors[i])
            save_data({'string': chunks[i], 'embedding': vectors[i]})
        # do some timing
        times.append(time() - start)
        print('Average time per file:', sum(times) / len(times))
    print('Total time:', time() - overall_start)