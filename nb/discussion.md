## Problem 1

### Part A


### Part C
The three tests all passed sucessfully.

```text
================================================= test session starts =================================================
platform win32 -- Python 3.14.7, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\alhod\anaconda3\envs\dsan5400\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\alhod\OneDrive\Desktop\5400_HW3\nb
configfile: pytest.ini
plugins: anyio-4.14.2
collected 3 items

tests/test_naive_bayes.py::test_nb_class[priors] PASSED                                                          [ 33%]
tests/test_naive_bayes.py::test_nb_class[likelihoods] PASSED                                                     [ 66%]
tests/test_naive_bayes.py::test_nb_class[sums] PASSED                                                            [100%]

================================================== 3 passed in 0.74s ==================================================
```

## Problem 2

### Part E
for the query "system", all three tokenizers gave the same 10 document ids:
- **Whitespace tokenizer:**  ['3', '1127', '2552', '3319', '5653', '8772', '8935', '14398', '16515', '16638']
- **library tokenizer:**  ['3', '1127', '2552', '3319', '5653', '8772', '8935', '14398', '16515', '16638']
- **n-gram tokenizer (n=4):**  ['3', '1127', '2552', '3319', '5653', '8772', '8935', '14398', '16515', '16638']

all three tokenizers gave the exact same result for this query. Whitespace and library tokenizer use different ways of splitting text, while ngram tokenizer splits text into four character sequences. regardless, output was the same for "system". morover, search is also NOT affected by case since all tokens were converted to lower case in normalization.

### Part F
for the query "compatibility", all three tokinizers returned same 2 document ids:
- **whitespace tokenizer:** ['8772', '14398']
- **library tokenizer:** ['8772', '14398']
- **n-gram tokenizer (n=4):** ['8772', '14398']

results here are identical, same as E, despite the different tokenization methods, these methods will work the same given one word,

### Part G
For the query "system compatibility", I INITIALLY got:
- **whitespace tokenizer:** ['8772', '14398']
- **library tokenizer:** ['8772', '14398']
- **n-gram tokenizer (n=4):** ['8772']

the n-gram tokenizer initially returned less documents than the other two. this happened because i was tokenizing the entire query as one string, which created a four character sequence that crossed the space between "system" and "compatibility". since my search function uses set intersection, a document had to contatin every generate n-gram to match

**Changes made and improved version:**

I modified the search function to tokenize each query word seperately before doing the set intersection. this stopped ngram tokenizer from generating sequences that were affected by the space between query words.

**final result:**
- **whitespace tokenizer:** ['8772', '14398']
- **library tokenizer:** ['8772', '14398']
- **n-gram tokenizer (n=4):** ['8772', '14398']

after the change, all tokenizers returned same two documents. search now checks for tokens from both words without checking ngrams that take space between them