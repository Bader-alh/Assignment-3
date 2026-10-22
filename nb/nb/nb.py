import numpy as np

class NaiveBayes:
    def __init__(self,alpha=0.1):
        self.alpha = alpha #smooth val lidstone
        self.vocabulary = {} #dict for unique word/index
        self.priors = None #later store prob of each class k or j
        self.likelihoods = None #prob for class


    def train(self,df): #basically copied from hw 2 but turning into class rather than standalone,, mostly same
        self.vocabulary = {} #reset vocab each time we train model
        for text in df["text"]:
            for word in text.split():
                if word not in self.vocabulary:
                    self.vocabulary[word] = len(self.vocabulary) #build dict of unique woird and index

        n_docs = df.shape[0] #num train speech (doc and class)
        n_classes = df["author"].nunique() #2
        self.priors = df["author"].value_counts(normalize=True).sort_index().to_numpy() #from documentation,,
        #probably could have copied and paste directly and made the minor adjustments, but that confused me even more and looked messy with all the todo

        #bow matrix
        training_matrix = np.zeros((n_docs,len(self.vocabulary)))
        for i, text in enumerate(df["text"]):
            for word in text.split():
                training_matrix[i,self.vocabulary[word]] += 1 #row is speech, col is unique words. each cell stores frequency of word

        word_counts_per_class = np.zeros((n_classes,len(self.vocabulary)))
        for c in range(n_classes):
            word_counts_per_class[c] = training_matrix[df["author"] == c].sum(axis=0) #sum of total word count
        self.likelihoods = np.zeros((n_classes, len(self.vocabulary))) #one row per author, one col per vocab w
        for c in range(n_classes):
            total_ww = word_counts_per_class[c].sum()
            self.likelihoods[c] = (word_counts_per_class[c] + self.alpha) / (total_ww + self.alpha * len(self.vocabulary))

    def test(self,df): #again just copied and adjusted var
        class_predictions = []
        for text in df["text"]:
            test_vector = np.zeros(shape=(len(self.vocabulary)))
            for word in text.split():
                if word in self.vocabulary:
                    test_vector[self.vocabulary[word]] += 1 #go through every word in test, check if wrod exists in train, if yes add 1
            preds = np.log(self.priors) + np.sum(test_vector * np.log(self.likelihoods), axis=1) #log,, avoid underflow and turn product to sum, avoid naive bayes issue of multiplying probabilities and getting 0
       
            yhat = np.argmax(preds) #preds[0] score for kennedy, 1 for johnsonn. argmax will give index of larger score/
            class_predictions.append(yhat)
        return class_predictions