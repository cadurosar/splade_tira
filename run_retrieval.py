import pyterrier as pt
pt.init()

import pandas as pd
from tira.third_party_integrations import ensure_pyterrier_is_loaded, get_input_directory_and_output_directory, persist_and_normalize_run
import json
from tqdm import tqdm

import pyt_splade



ensure_pyterrier_is_loaded()
input_directory, output_directory = get_input_directory_and_output_directory('./sample-input-full-rank')

print('Step 2: Load the data.')

queries = pt.io.read_topics(input_directory + '/queries.xml', format='trecxml')

documents = (json.loads(i) for i in open(input_directory + '/documents.jsonl', 'r'))

print('Step 3: Create the Index.')

splade = pyt_splade.SpladeFactory()
iter_indexer = pt.IterDictIndexer("./index", meta={'docno' : 100}, pretokenised=True)

indxr_pipe = splade.indexing() >> indexer
index_ref = indxr_pipe.index(tqdm(documents), batch_size=128)

print('Step 4: Create Run.')
splade_retr = splade.query() >> pt.BatchRetrieve(index_ref, wmodel='Tf')
run = splade_retr(queries)

print('Step 5: Persist Run.')

persist_and_normalize_run(run, output_file=output_directory, system_name='BM25', depth=1000)
