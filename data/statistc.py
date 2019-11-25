import pandas as pd
#df=pd.read_csv('Train_DataSet_Label.csv')
# df.columns=['id','title','content']
# df['label']=0
# df[['id','label']].to_csv('submit_example.csv',index=False)
def cal(text):
    df=pd.read_csv(text)
    df0=len(df[df['label']==0])
    print(df0)
    df1=len(df[df['label']==1])
    print(df1)
    df2=len(df[df['label']==2])
    print(df2)
    sum=df1+df2+df0
    print(df0/sum,df1/sum,df2/sum)

cal('data_0/train.csv')
cal('data_0/dev.csv')