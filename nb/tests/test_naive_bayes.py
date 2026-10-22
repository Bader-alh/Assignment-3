import numpy as np
from nb.nb import NaiveBayes
from pathlib import Path
import pandas as pd #prob dont need to since alr 
import pytest
@pytest.mark.parametrize("check",["priors", "likelihoods", "sums"])
def test_nb_class(check):
    data_p = Path(__file__).parent / "data" / "docs.txt" #fropm documentation,, very confusing. basically loading five training doc from jurafsky sample
    df = pd.read_csv(data_p, sep="\t",header=None,names=["author","text"]) #i think proper sep?
    df["author"] = df["author"].map({"negative": 0, "positive": 1}) #maping/converting neg/pos labels to 0/1
    model = NaiveBayes(alpha=1) #add one smoothening smae as jurafsky
    model.train(df)
    #test
    if check == "priors":
        expected_prior = np.array([3/5,2/5])
        assert np.allclose(model.priors, expected_prior)

    elif check == "likelihoods":
        word_index = model.vocabulary["predictable"]
        expeted_like = np.array([2/34,1/29])
        actual_like = model.likelihoods[:,word_index]
        assert np.allclose(actual_like,expeted_like)

    elif check == "sums":
        like_sums = model.likelihoods.sum(axis=1)
        assert np.allclose(like_sums,np.ones(2))
#basically the test goes and test if values are same as jurafsky samples