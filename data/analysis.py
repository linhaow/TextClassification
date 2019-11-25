import pandas as pd
import os
import random
import io

label_name='flag'
out='report.txt'   

os.system("rm report.txt")

def analyzefile(file):
    df=pd.read_csv(file)
    os.system("touch "+out)
    os.system("echo '-------------information about "+file+" set------------' >> "+out)
    os.system("echo 'the row number of "+file+" is "+str(df.shape[0])+"' >> "+out)
    if(file=='train.csv'):
        os.system("echo 'the label number of "+file+" is\n"+str(df[label_name].value_counts()[:10])+"' >> "+out) 
    os.system("echo '\n-------------the describe of "+file+" is ------------------ \n"+str(df.describe())+"' >> "+out)
    os.system("echo '\n--------------the info of "+file+" data --------------- \n' >> "+ out)
    buffer=io.StringIO()
    df.info(buf=buffer)
    info=buffer.getvalue()
    f=open('report.txt','a')
    f.write(info)
    f.write("\n\n\n")
    f.close()

analyzefile('train.csv')
analyzefile('test.csv')
