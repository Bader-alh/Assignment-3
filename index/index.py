import xml.etree.ElementTree as ET
from nltk.tokenize import wordpunct_tokenize
import string
from nltk.stem import PorterStemmer
from collections import Counter
import argparse
#really had to stare at documenation for problem 2 :(
#sources for problem 2: https://lxml.de/2.2/tutorial.html
#go through each document

def load_document(filepath): #redo,, edit:previously had one version for testing, this should work for all documents in both
    tree = ET.parse(filepath)
    root = tree.getroot()
    documents = {}
    for doc in root.findall("doc"):
        doc_id = doc.findtext("docid")
        text = doc.findtext("msgtext")
        documents[doc_id] = text
    return documents

class Tokenizer:
    def tokenize(self,text):
        pass #do later, might just leave it, but raise before to debug and error check but removed once done
#source here: https://experienceleague.adobe.com/en/tools/aem-api-documentation/cloud-service/javadoc/org/apache/lucene/analysis/core/WhitespaceTokenizer.html

class WhitespaceTokenizer(Tokenizer): #tokenizer which splits text using whitespace
    def tokenize(self,text):
        return text.split()

class libtoken(Tokenizer): #tokenizer using nltk wordpunct (check hugging face doc)
    def tokenize(self,text):
        return wordpunct_tokenize(text)
#source: https://lucenenet.apache.org/docs/4.8.0-beta00005/api/Lucene.Net.Analysis/Lucene.Net.Analysis.NGram.NGramTokenizer.html
class NGramTokenizer(Tokenizer):
    def __init__(self,n=4):
        self.n = n #num of char per token

    def tokenize(self,text):
        tokens = [] #store ngrams
        for i in range(len(text) - self.n + 1): 
            tokens.append(text[i:i + self.n])#loop to get n characters from position i

        return tokens #should be list of character ngrams

def normalize_tokens(tokens): #conv to lwoercase and remove puncuation
    normalised = []
    for token in tokens:
        word = token.lower().strip(string.punctuation)
        if word:
            normalised.append(word)
    return normalised

#c: stem tokens, got from documentation
def stem_tokens(tokens):
    stemmer = PorterStemmer() #create porter stem object
    stemm = []
    for token in tokens:
        stemm.append(stemmer.stem(token))
    return stemm

#self note: rev. pseudocode was very helpful actually
def build_index(documents,tokenizer,use_stemming=False): #stemming false, will if later
    index = {} #sotre tokens 
    for doc_id,text in documents.items():
        tokens = tokenizer.tokenize(text) #tokenize document using a tokenizer
        tokens = normalize_tokens(tokens) #normalize tokens (case and puncuation normalization)
        if use_stemming:
            tokens = stem_tokens(tokens)
        term_frequency = Counter(tokens)
        for token in term_frequency:
            if token in index:
                index[token].append((doc_id, term_frequency[token]))
            else:
                index[token] = [(doc_id,term_frequency[token])]
    return index
#testing/debugg (removed after i finished for brevity)

#e
def search_index(index,query,tokenizer,use_stemming=False):#search inverted index for document that have specific query
    #tokenize/normalise query (same as documents)
    tokens = []
    for word in query.split():
        tokens.extend(normalize_tokens(tokenizer.tokenize(word))) #this was ADDED LAST since ngram could not pick up the other document

    #stemming if needed
    if use_stemming:
        tokens = stem_tokens(tokens)

    match_docs = [] #get doc id that have each token
    for token in tokens: #get posting list for token, [] if not found
        posting = index.get(token,[])
        ids = {doc_id for doc_id,frequency in posting} #take document id from doc_id, frequency pair, then store unique doc ids
        match_docs.append(ids)
    if match_docs: #if gives tokens, find documents in common to all tokens
        return set.intersection(*match_docs) #source: documentaion #intersection takes document that has EVERY query token, could have looped maybe? this was easier.
    #in theory should work? test later. "system compatability" should return documents that have BOTH
    return set() #return empty set if no tokens

#cmd interface. very close to hw2,, still feeling rusty about this, should work

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Inverted Index") #argument parser 
    parser.add_argument("-f", "--file", required=True,help="path to XML file")#-f for which xml to load
    parser.add_argument("-t", "--tokenizer", required=True,choices=["whitespace","library","ngram"],help="tokenizer to use") #-t lets user choose one of the tokenizer, did choices to limit inout to three options
    parser.add_argument("-s", "--stem", action="store_true", help="use porter stemming") #-s for if porter stemming is used,, store true is true if -s is given, false otherwise, basically boolean flag
    args = parser.parse_args()
    #this part took me too long, was super confused how to connect for some reason, its fairly straighforward too
    documents = load_document(args.file)
#select tokenizer based on -t
    if args.tokenizer == "whitespace":
        tokenizer = WhitespaceTokenizer()
    elif args.tokenizer == "library":
        tokenizer = libtoken()
    else:
        tokenizer = NGramTokenizer()

    #building inverted index with tokenizer
    #args.stem for if stemming used
    index = build_index(documents,tokenizer,use_stemming=args.stem)

    #query search index test
    queries = ["system", "compatibility", "system compatibility"]
    for query in queries:
        res = search_index(index,query,tokenizer,use_stemming=args.stem) #SHOULD work this time
        print("query: ", query)
        print("matching document ID's: ", sorted(res, key=int))
        print() #print doc id in numerical order (for brevity sake and ocd honestly, i know any order is fine)

#COMMENTs ON RESULTS IN DISCUSSION
#testing/debugg (removed after i finished for brevity)
