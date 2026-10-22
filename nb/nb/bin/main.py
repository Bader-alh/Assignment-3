import argparse
from nb.nb import NaiveBayes
from nb.utils.load_data import build_dataframe

#same as hw2 but putting in main func
#basically copying from hw2
def main():
    parser = argparse.ArgumentParser(description="Naive Bayes Algorithm")
    parser.add_argument("-f", "--indir", required=True, help="Data directory")
    args = parser.parse_args()
    training_df, test_df = build_dataframe(args.indir)
    #above from hw2, now small tweaking to make it work here
    model = NaiveBayes(alpha=0.1)
    model.train(training_df) #naive bayes model
    class_predictions = model.test(test_df) #test unseen doc
    print("predictions: ", class_predictions) #print pred

if __name__ == "__main__": #move
    main()

