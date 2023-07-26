# splade_tira

command to build the docker image:

```
docker build -t registry.webis.de/code-research/tira/tira-user-tira-user-naverlabseurope/my-software:0.0.1 -f Dockerfile.base .
```

```
tira-run \
    --image registry.webis.de/code-research/tira/tira-user-tira-user-naverlabseurope/my-software:0.0.1 \
    --command 'python3 /workspace/run_retrieval.py --input $inputDataset --output $outputDir'
    --input ${PWD}/sample-input-full-rank
```

TODO: Maik adjust the tira-run command so that it can use podman as Docker runtime.

### Colab link

https://colab.research.google.com/drive/1PNzl3efkI90BpCiQGfRjd7HMrUo3frxB?usp=sharing
