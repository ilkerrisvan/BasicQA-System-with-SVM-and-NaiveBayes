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
        PATH = f"{train_path}"   ## this path will change on AWS.
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

        answers_b_corpus_s = " "

        tag_0_answer = " "
        tag_1_answer = " "
        tag_2_answer = " "
        tag_3_answer = " "
        tag_4_answer = " "
        tag_5_answer = " "
        tag_6_answer = " "
        tag_7_answer = " "
        tag_8_answer = " "
        tag_9_answer = " "

        all_answers = []


        for i in range(10) :
            tags.append(data[i]['tag'])  ## put tags to list
            answers.append(response_data[i]["answers"])
            answers_b_corpus.append(data[i]["answers"])

        for i in range(0, 10) :
            answers_b_corpus_s += str(answers_b_corpus[i][0])

        p_t = 1 / len(tags)  ## this value is constant NOW.We can change this after.1/10 so we have 10 classes

        tag_0_answer += str(answers_b_corpus[0][0])
        tag_1_answer += str(answers_b_corpus[1][0])
        tag_2_answer += str(answers_b_corpus[2][0])
        tag_3_answer += str(answers_b_corpus[3][0])
        tag_4_answer += str(answers_b_corpus[4][0])
        tag_5_answer += str(answers_b_corpus[5][0])
        tag_6_answer += str(answers_b_corpus[6][0])
        tag_7_answer += str(answers_b_corpus[7][0])
        tag_8_answer += str(answers_b_corpus[8][0])
        tag_9_answer += str(answers_b_corpus[9][0])

        all_answers.append(tag_0_answer)
        all_answers.append(tag_1_answer)
        all_answers.append(tag_2_answer)
        all_answers.append(tag_3_answer)
        all_answers.append(tag_4_answer)
        all_answers.append(tag_5_answer)
        all_answers.append(tag_6_answer)
        all_answers.append(tag_7_answer)
        all_answers.append(tag_8_answer)
        all_answers.append(tag_9_answer)
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
            for j in range(len(all_answers)) :
                if i in all_answers[j].split() :
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

        prob_of_tag.append((counter_tag0 / len(all_answers[0].split())) * p_t)
        prob_of_tag.append((counter_tag1 / len(all_answers[1].split())) * p_t)
        prob_of_tag.append((counter_tag2 / len(all_answers[2].split())) * p_t)
        prob_of_tag.append((counter_tag3 / len(all_answers[3].split())) * p_t)
        prob_of_tag.append((counter_tag4 / len(all_answers[4].split())) * p_t)
        prob_of_tag.append((counter_tag5 / len(all_answers[5].split())) * p_t)
        prob_of_tag.append((counter_tag6 / len(all_answers[6].split())) * p_t)
        prob_of_tag.append((counter_tag7 / len(all_answers[7].split())) * p_t)
        prob_of_tag.append((counter_tag8 / len(all_answers[8].split())) * p_t)
        prob_of_tag.append((counter_tag9 / len(all_answers[9].split())) * p_t)

        correct_tag = prob_of_tag.index(max(prob_of_tag))

        ## print(answers[correct_tag][0])
        results_test.append(correct_tag)
        return answers[correct_tag][0],results_test

    ######################## TEST ##########################
def run(data_path, train_path, test_path) :

     ## TEST CORPUS (we use it for give response)
    PATH = f"{test_path}"
    test_corpus = open(PATH, )
    test_data = json.load(test_corpus)
    test_corpus.close()

    r = []
    for i in range(10):
        for j in range(2):
            data = test_data[i]["questions"][j].split()
            a,r = nb(data_path,train_path,data)

    ##print(r)
    ## print(test_data[i]["questions"][j].split())
    y_train = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
    cm = confusion_matrix(y_true=y_train,y_pred=r,normalize="true") ## normalize="true"

    ##print(cm)







    df_cm = pd.DataFrame(cm, range(10), range(10))
    # plt.figure(figsize=(10,7))
    sn.set(font_scale=1.4) # for label size
    sn.heatmap(df_cm, annot=True, annot_kws={"size": 16}) # font size

    plt.title('Naive Bayes - Answer Based', fontsize = 20) # title with fontsize 20
    plt.xlabel('Predicted Classes', fontsize = 15) # x-axis label with fontsize 15
    plt.ylabel('True Classes', fontsize = 15) # y-axis label with fontsize 15
    plt.show()

    ## data = ["dr", "arıkan", "ne", "burs" ]
    ## print("******************************************" , run(data))
