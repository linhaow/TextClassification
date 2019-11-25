import pandas as pd
import numpy as np

#vote 文件
submits_path='./submits'
#需要进行vote的文件
submits = ['0.82414645.csv','0.8172323.csv','0.81546885000.csv']
#vote时文件的权重
file_weight = [3,2,2]
#vote时标签的权重
label_weight =[1,1,1]

files = []
data = []
for f in submits:
    if 'csv' in f:
        files.append(f)
        data.append(pd.read_csv(submits_path+f).values)
print(len(files))
output = np.zeros([len(data[0]), 3])

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j][1] == 0:
            output[j][0] += file_weight[i]*label_weight
        elif data[i][j][1] == 1:
            output[j][1] += file_weight[i]*label_weight
        elif data[i][j][1] == 2:
            output[j][2] += file_weight[i]*label_weight
            
#读取提交模板,需要设置
submit = pd.read_csv('sub_teample.csv')
submit['label'] = np.argmax(output, axis = 1)
submit.to_csv('submit.csv',index=None)


