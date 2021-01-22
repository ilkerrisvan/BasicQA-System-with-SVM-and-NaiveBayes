import json
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.feature_selection import *
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline #pipeline to implement steps in series
import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt


result_data = []

def svm(train_path,input_data):
        global result_data

        with open(f"{train_path}") as data_file:
            lines = data_file.readlines()
            joined_lines = "[" + ",".join(lines) + "]"

        json_data = json.loads(joined_lines)

        data = pd.DataFrame(json_data)

        words = stopwords.words("turkish")

        data['cleaned'] = data['text']

        X_train, X_test, y_train, y_test = train_test_split(data['cleaned'], data.stars, test_size=0.2)

        pipeline = Pipeline([('vect', TfidfVectorizer(ngram_range=(1, 2), stop_words=words, sublinear_tf=True)),
                             ('chi',  SelectKBest(chi2, k=224)), ## answer 684
                             ('clf', LinearSVC(C=1.0, penalty='l1', max_iter=20000, dual=False))])

        model = pipeline.fit(X_train, y_train)

        result = model.predict([input_data])

        result_data.append(result)

        return result_data

def run(train_path, test_path) :

    ## TEST CORPUS (we use it for give response)
    PATH = f"{test_path}"
    test_corpus = open(PATH, )
    test_data = json.load(test_corpus)
    test_corpus.close()

    r = [] ## result

    for i in range(10):
        for j in range(2):
            data = (test_data[i]["questions"][j])
            r = svm(train_path,data)

    res = []
    for i in range(20):
        res.append(r[i][0])

    y_train = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10] ## %100 true form

    cm = confusion_matrix(y_true=y_train,y_pred=res,normalize="true")

    df_cm = pd.DataFrame(cm, range(10), range(10))
    sn.set(font_scale=1.4) # for label size
    sn.heatmap(df_cm, annot=True, annot_kws={"size": 16}) # font size

    plt.title('SVM - Answer Based', fontsize = 20) # title with fontsize 20
    plt.xlabel('Predicted Classes', fontsize = 15) # x-axis label with fontsize 15
    plt.ylabel('True Classes', fontsize = 15) # y-axis label with fontsize 15

    plt.show()





















# confussion matrix

# Predicting the test set results

# Getting the true positives, false positives,
# false negatives and true negative
# and creating the matrix.

"""print("Y train: ",y_train)
testARR = [1,4,6,2,3,4,2,1,7]
cm = confusion_matrix(y_true=y_train,y_pred=testARR)
print("CM: ")
print(cm)
"""
