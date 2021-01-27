# BasicQA-System-with-SVM-and-NaiveBayes
This project compares SVM and Naive Bayes and include a basic qa system.

You can ask questions about dataset's classes,these classes include Turkish datas.


e.g: Maksimum kaç kredi alabilirim ?, can be an input for system. Snowballstemmer library used for use input in SVM and Naive Bayes, for the best performance use Zemberek(Zemberek was used in stemmer in datasets), snawballstemmer tested against the zemberek. Question based system uses questions as train data,answer based uses answers.


You can get the code that compare two classifiers' performance in this dataset with use [this.](https://github.com/ilkerrisvan/SVM-vs-NaiveBayes-in-TextClassification)


### run
`pip install -r requirements.txt` 
`python3 main.py `
