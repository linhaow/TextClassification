import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

#对输出文件进行分析，分析他们的相关程度

path="./submits" #文件夹目录
raw = pd.read_csv('0.82414645.csv')
raw = raw.drop('label',axis=1)
files= os.listdir(path) #得到文件夹下的所有文件名称
s = []
for file in files: #遍历文件夹
     print(file)
     if(file.find(".csv")>0):
         tmp = pd.read_csv(file)
         tmp = tmp[['id', 'label']]
         tmp.columns = ['id', file]
         raw = pd.merge(raw, tmp, on='id')

new = raw.drop(['id'],axis=1)

def test(df):
    dfData = df.corr()
    print(dfData)
    plt.subplots(figsize=(19, 19)) # 设置画面大小
    sns.heatmap(dfData, annot=True, vmax=1, square=True, cmap="Blues")
    plt.savefig('./SubmitRelation.png')
    plt.show()

test(new)
