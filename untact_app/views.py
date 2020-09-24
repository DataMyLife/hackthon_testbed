from django.shortcuts import render
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import pandas as pd
import pickle


def main(request):
    return render(request, "survey.html")

def clustering():   #학습함수
    df_clustering = pd.read_csv(r"./survey.csv", encoding = "utf-8")
    kmeans = KMeans(n_clusters=3, random_state=0)
    kmean_label = kmeans.fit(df_clustering)
    df_clustering["label"] = kmean_label.labels_
    df_clustering.head()
    saved_model = pickle.dumps(kmean_label)
    return saved_model


saved_model = clustering()


def predict(request): #새로운 고객의 설문조사 결과를 출력(예측하는) 함수

    df_clustering = pd.read_csv(r"./survey.csv", encoding="utf-8")
    kmeans = KMeans(n_clusters=3, random_state=0)
    kmean_label = kmeans.fit(df_clustering)

    lst = []
    q0 = 0
    q1 = request.POST["1"]; q2 = request.POST["2"]; q3 = request.POST["3"]
    q4 = request.POST["4"]; q5 = request.POST["5"]; q6 = request.POST["6"]
    q7 = request.POST["7"]; q8 = request.POST["8"]; q9 = request.POST["9"]
    q10 = request.POST["10"]; q11 = request.POST["11"]; q12 = request.POST["12"]

    lst.append(q0)
    lst.append(int(q1))
    lst.append(int(q2))
    lst.append(int(q3))
    lst.append(int(q4))
    lst.append(int(q5))
    lst.append(int(q6))
    lst.append(int(q7))
    lst.append(int(q8))
    lst.append(int(q9))
    lst.append(int(q10))
    lst.append(int(q11))
    lst.append(int(q12))
    print(lst)

    new_df = pd.DataFrame(lst).T

    new_df.columns = ["USER_ID","Q_1", "Q_2", "Q_3", "Q_4", "Q_5", "Q_6",  # USER_ID 추가
                  "Q_7", "Q_8", "Q_9", "Q_10", "Q_11", "Q_12"]

    pred = kmean_label.predict(new_df)
    cluster_integer = int(pred)
    
    context = {
        "cluster_integer" : cluster_integer
    }

    return render(request, "predict.html", context)




#     # DB modeling 
# 1. 기존 데이터베이스에 데이터추가
import csv
import os
import django
 

from .models import survey, contents

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testbed3_app.settings")
django.setup()


csv_path = r"./survey.csv"
# survey 데이터베이스 저장하기
with open(csv_path, 'r', encoding='utf-8') as csvfile:
    data_reader = csv.DictReader(csvfile)
    for row in data_reader:
        print(row)
        survey.objects.create(
            USER_ID = row["USER_ID"],
            Q_1 = row["Q_1"],
            Q_2 = row["Q_2"],
            Q_3 = row["Q_3"],

            Q_4 = row["Q_4"],
            Q_5 = row["Q_5"],
            Q_6 = row["Q_6"],

            Q_7 = row["Q_7"],
            Q_8 = row["Q_8"],
            Q_9 = row["Q_9"],

            Q_10 = row["Q_10"],
            Q_11 = row["Q_11"],
            Q_12 = row["Q_11"]
        )




# DB modeling 
# 1. 기존 데이터베이스에 데이터추가
import csv
import os
import django
 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testbed3_app.settings")
django.setup()


csv_path = r"./corona_contents.csv"
# 코로나 컨텐츠 데이터베이스 저장하기
with open(csv_path, 'r', encoding='utf-8') as csvfile:
    data_reader = csv.DictReader(csvfile)
    for row in data_reader:
        print(row)
        contents.objects.create(
            contents_name = row["contents_name"],
            contents_href = row["contents_href"],
            contents_type = row["contents_type"],
            cluster_label = row["cluster_label"]
        )

