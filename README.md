
 # NLP Project

## Preparing datasets
1. Training dataset: [ro_rrt-ud-train.conllu](https://github.com/UniversalDependencies/UD_Romanian-RRT/blob/master/ro_rrt-ud-train.conllu) (texte adnotate)
2. Convert dataset to .json 'spacy convert ./condulu/ro_rrt-ud-train.conllu . -t json'
3. Convert .json to .spacy 
4. Repeat for dev and test datasets

## Training models

5. Using Tok2Vec 
    Observations:
        - Very fast training 
        - Accuracy aprox 95%
6. Tok2Vec + static vectors ("ro_core_news_lg")
        - Accuracy 96.98% 
        - Tagger Loss 1954.35
7. Transfowrmer https://huggingface.co/dumitrescustefan/bert-base-romanian-cased-v1.
    Observations: 
        - Slow training
        - Huge Tagger Loss compared to training with Tok2Vec
        - rezultate: 
            - 25 epochs
            - Loss 13302.95
            - Training Accuracy 94.97%


6. Results
    - Test dataset path:  ./datasets/ro_rrt-ud-train.spacy
    - Test command:  python -m spacy evaluate <path to model> <path to dataset> (e.g. python -m spacy evaluate ./outputCuTransformer/model-best ./datasets/ro_rrt-ud-test.spacy) 
    

## 📊 POS Tagging Model Evaluation Results

| Model                                | Tokenization Accuracy (%) | POS Tagging Accuracy (%) | Speed (words/sec) |
|--------------------------------------|--------------------------|-------------------------|------------------|
| **spaCy Tok2Vec**                     | 99.84                     | 95.38                    | 21,355           |
| **spaCy Tok2Vec with 'ro_core_news_lg' pretrained vectors**        | 99.84                     | 96.74                    | 3419           |
| **distilbert-base-multilingual-cased** | 99.84                     | 94.47                    | 405              |
| **dumitrescustefan/bert-base-romanian-cased-v1** |     99.84                |     89               |               |



