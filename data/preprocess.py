import pandas as pd
import os
import random
random.seed(1)
train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')

test_df['content']=test_df['content'].fillna('无。')
train_df['content']=train_df['content'].fillna('无。')
test_df['title']=test_df['title'].fillna('无。')
train_df['title']=train_df['title'].fillna('无。')
test_df['flag']=0

test_df.to_csv("data/test.csv",index=False)
train_df.to_csv("data/train.csv",index=False)

index=set(range(train_df.shape[0]))
K_fold=[]
for i in range(5):
    if i == 4:
        tmp=index
    else:
        tmp=random.sample(index,int(1.0/5*train_df.shape[0]))
    index=index-set(tmp)
    print("Number:",len(tmp))
    K_fold.append(tmp)
    

for i in range(5):
    print("Fold",i)
    os.system("mkdir data_{}".format(i))
    dev_index=list(K_fold[i])
    train_index=[]
    for j in range(5):
        if j!=i:
            train_index+=K_fold[j]
    train_df.iloc[train_index].to_csv("data_{}/train.csv".format(i),index=False)
    train_df.iloc[dev_index].to_csv("data_{}/dev.csv".format(i),index=False)
    test_df.to_csv("data_{}/test.csv".format(i),index=False)

os.system("mv data_0/dev.csv data/dev.csv")
