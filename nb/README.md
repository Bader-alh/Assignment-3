
# Naive Bayes text Classifier
## Problem 1
## Description for project
This project implements a multinomial naivee bayes classifier to predict authors of the presedential speech, Kennedy or Johnson. initial adaptation is taken from assignment 2 and reorganized into a python project by creating a class (object oriented programming).

the classifier uses whitespace tokenization, bag of words, and Lidstone smoothening to calculate prior probabilities and word likelihoods.

### Structure
- `nb/nb.py` - contains NaiveBayes class with training and testing methods
- `nb/utils/load_data.py` - laods text documents into pandas dataframe
- `tests/` - unit test using pytest
- `data/` - presidentail speech datasets

### Testing
to run unit tests from the project directly, I used anaconda prompt with the following commands:
```bash
python -m pytest tests/ -v
```
this test checks prior probability, likelihoods, and if likelihoods sum to 1 for each class

### Usage
ran clasifier from project directory using:
```bash
python -m nb.bin.main -f data
```

`-f` argument specifies directory which has train and test documents

the programme loads kennedy and johnson speeches, trains naive bayes classifier, and prints the predicted autho label for the test documents.

in our case, author labesl are:
- `0` = Kennedy
- `1` = Johnson


## Problem 2: inverted index

this program builds an inverted index from the XML documents usign different tokenizer methods. the program then noramlzes tokens by making them lower case and removing punctuation. 
the inverted index stores document ids and term frequency for each token.

### Usage
to run program, use index directory and this command:
```bash
python index.py -f 20newsgroups-initial.xml -t whitespace
```

command line arguments:

- `-f`: path to XML dataset
- `-t`: tokenizer selection (`whitespace`,`library`,`ngram`)
- `-s`: boolean flag to enable proter stemming (optional).

for example, tu run with character n-grams and stemming:
```bash
python index.py -f 20newsgroups-initial.xml -t ngram -s
```

the program prints the document ids matching the queries "system","compatibility", and both terms together