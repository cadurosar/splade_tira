# splade_tira

command to build the docker image:

```
docker build -t registry.webis.de/code-research/tira/tira-user-tira-user-naverlabseurope/my-software:0.0.1 -f Dockerfile.base .
```

```
tira-run \
    --image registry.webis.de/code-research/tira/tira-user-tira-user-naverlabseurope/my-software:0.0.1 \
    --input-directory sample-input-full-rank \
    --command 'python3 /workspace/run_retrieval.py --input $inputDataset --output $outputDir'
```

tira-run --image registry.webis.de/code-research/tira/tira-user-pan23-cdav-baseline/galicia22a:0.0.2 --input-directory pan23-authorship-verification-train-20230322-training/ --output-directory o --command 'python3 /app/model/codes/predict.py -i $inputDataset -o $outputDir'


Upload the image via:

```
docker push registry.webis.de/code-research/tira/tira-user-tira-user-naverlabseurope/my-software:0.0.1
```

TODO: Maik adjust the tira-run command so that it can use podman as Docker runtime.

### Colab link

https://colab.research.google.com/drive/1PNzl3efkI90BpCiQGfRjd7HMrUo3frxB?usp=sharing
