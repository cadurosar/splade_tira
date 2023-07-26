import os
os.environ["PYTERRIER_VERSION"] = '5.7'
os.environ["PYTERRIER_HELPER_VERSION"] = '0.0.7'
import pyterrier as pt
if not pt.started():
  pt.init()

import pandas as pd
from tira.third_party_integrations import ensure_pyterrier_is_loaded, get_input_directory_and_output_directory, persist_and_normalize_run
import json
from tqdm import tqdm

import pyt_splade


ensure_pyterrier_is_loaded()
input_directory, output_directory = get_input_directory_and_output_directory('./splade_tira/sample-input-full-rank/')


ensure_pyterrier_is_loaded()
input_directory, output_directory = get_input_directory_and_output_directory('./sample-input-full-rank')

print('Step 2: Load the data.')

queries = pt.io.read_topics(input_directory + '/queries.xml', format='trecxml')

documents = [json.loads(i) for i in open(input_directory + '/documents.jsonl', 'r')]

print('Step 3: Create the Index.')
splade = pyt_splade.SpladeFactory()
iter_indexer = pt.IterDictIndexer("./index", pretokenised=True, meta={'docno' : 100})

from pyterrier_pisa import PisaIndex
index = PisaIndex('./index', stemmer='none')

# indexing
idx_pipeline = splade.indexing() >> index.toks_indexer()

index_ref = idx_pipeline.index(documents, batch_size=2)


print('Step 4: Create Run.')
splade_retr = splade.query() >> index.quantized()
run = splade_retr(queries)


print('Step 5: Persist Run.')

persist_and_normalize_run(run, output_file=output_directory, system_name='SPLADE++-CoCondenser-EnsembleDistil', depth=1000)
