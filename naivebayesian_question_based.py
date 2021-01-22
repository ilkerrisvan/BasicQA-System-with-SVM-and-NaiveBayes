import json
from sklearn.metrics import confusion_matrix
import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt

results_test = []


def nb(data_path,train_path,input_data) :
    global results_test

    # Opening JSON file
    ## B CORPUS
    PATH = f"{train_path}"  ## this path will change on AWS.
    b_corpus = open(PATH, )
    data = json.load(b_corpus)
    b_corpus.close()

    ## A CORPUS (we use it for give response)
    PATH = f"{data_path}"
    a_corpus = open(PATH, )
    response_data = json.load(a_corpus)
    a_corpus.close()

    answers = []
    answers_b_corpus = []

    tags = []  ## read JSON into the list
    questions = [[""] * 8 for i in range(10)]  ## read JSON into the 2D list

    tag_0_question = " "
    tag_1_question = " "
    tag_2_question = " "
    tag_3_question = " "
    tag_4_question = " "
    tag_5_question = " "  ## has 8 eight questions
    tag_6_question = " "
    tag_7_question = " "
    tag_8_question = " "
    tag_9_question = " "

    all_questions = []  ## we will keep questions in one list for reach the tag easily

    for i in range(10) :
        for j in range(len(data[i]['questions'])) :
            questions[i][j] = data[i]['questions'][j]  ## put questions to list

    for i in range(10) :
        tags.append(data[i]['tag'])  ## put tags to list
        answers.append(response_data[i]["answers"])
        answers_b_corpus.append(response_data[i]["answers"])

    p_t = 1 / len(tags)  ## this value is constant NOW.We can change this after.1/10 so we have 10 classes

    i = 0
    while i < 7 :
        tag_0_question += str(questions[0][i])
        tag_1_question += str(questions[1][i])
        tag_2_question += str(questions[2][i])
        tag_3_question += str(questions[3][i])
        tag_4_question += str(questions[4][i])
        tag_6_question += str(questions[6][i])
        tag_7_question += str(questions[7][i])
        tag_8_question += str(questions[8][i])
        tag_9_question += str(questions[9][i])
        ## when i changed words can be add together e.g mi,fx can be mifx so we can add " "
        tag_0_question += " "
        tag_1_question += " "
        tag_2_question += " "
        tag_3_question += " "
        tag_4_question += " "
        tag_6_question += " "
        tag_7_question += " "
        tag_8_question += " "
        tag_9_question += " "
        i += 1

    ## tag 5 has 8 different question
    for i in range(0, 8) :
        tag_5_question += str(questions[5][i])
        tag_5_question += " "

    all_questions.append(tag_0_question)
    all_questions.append(tag_1_question)
    all_questions.append(tag_2_question)
    all_questions.append(tag_3_question)
    all_questions.append(tag_4_question)
    all_questions.append(tag_5_question)
    all_questions.append(tag_6_question)
    all_questions.append(tag_7_question)
    all_questions.append(tag_8_question)
    all_questions.append(tag_9_question)

    """
    ## for see the words and check them.
    print(len(tag_5_question.split())) 
    print(tag_5_question.split()) 
    """
    counter_tag0 = 0
    counter_tag1 = 0
    counter_tag2 = 0
    counter_tag3 = 0
    counter_tag4 = 0
    counter_tag5 = 0
    counter_tag6 = 0
    counter_tag7 = 0
    counter_tag8 = 0
    counter_tag9 = 0
    ## for calculate p(s|t)
    for i in input_data :
        for j in range(len(all_questions)) :
            if i in all_questions[j].split() :
                if j == 0 :
                    counter_tag0 += 1
                if j == 1 :
                    counter_tag1 += 1
                if j == 2 :
                    counter_tag2 += 1
                if j == 3 :
                    counter_tag3 += 1
                if j == 4 :
                    counter_tag4 += 1
                if j == 5 :
                    counter_tag5 += 1
                if j == 6 :
                    counter_tag6 += 1
                if j == 7 :
                    counter_tag7 += 1
                if j == 8 :
                    counter_tag8 += 1
                if j == 9 :
                    counter_tag9 += 1
    prob_of_tag = []

    prob_of_tag.append((counter_tag0 / len(all_questions[0].split())) * p_t)
    prob_of_tag.append((counter_tag1 / len(all_questions[1].split())) * p_t)
    prob_of_tag.append((counter_tag2 / len(all_questions[2].split())) * p_t)
    prob_of_tag.append((counter_tag3 / len(all_questions[3].split())) * p_t)
    prob_of_tag.append((counter_tag4 / len(all_questions[4].split())) * p_t)
    prob_of_tag.append((counter_tag5 / len(all_questions[5].split())) * p_t)
    prob_of_tag.append((counter_tag6 / len(all_questions[6].split())) * p_t)
    prob_of_tag.append((counter_tag7 / len(all_questions[7].split())) * p_t)
    prob_of_tag.append((counter_tag8 / len(all_questions[8].split())) * p_t)
    prob_of_tag.append((counter_tag9 / len(all_questions[9].split())) * p_t)

    correct_tag = prob_of_tag.index(max(prob_of_tag))

    ## print(answers[correct_tag][0])

    results_test.append(correct_tag)
    return answers[correct_tag][0], results_test


def run(data_path,train_path,test_path):


     ## TEST CORPUS (we use it for give response)
    PATH = f"{test_path}"
    test_corpus = open(PATH, )
    test_data = json.load(test_corpus)
    test_corpus.close()

    r = [] ## results
    for i in range(10):
        for j in range(2):
            data = test_data[i]["questions"][j].split()
            a,r = nb(data_path,train_path,data)
    y_train = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]

   ## print(r)
   ## print(test_data[i]["questions"][j].split())
    cm = confusion_matrix(y_true=y_train,y_pred=r,normalize="true")
   ## print(cm)

    df_cm = pd.DataFrame(cm, range(10), range(10))
    # plt.figure(figsize=(10,7))
    sn.set(font_scale=1.4) # for label size
    sn.heatmap(df_cm, annot=True, annot_kws={"size": 16}) # font size

    plt.title('Naive Bayes - Question Based', fontsize = 20) # title with fontsize 20
    plt.xlabel('Predicted Classes', fontsize = 15) # x-axis label with fontsize 15
    plt.ylabel('True Classes', fontsize = 15) # y-axis label with fontsize 15

    plt.show()

    """data = ["yandal","ortalama","kaç","gerek"]
    print(run(data))"""
