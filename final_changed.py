import pandas as pd
import numpy as np
from collections import Counter

train_dataset = pd.read_csv('data/Train_DataSet.csv').values
train_label = pd.read_csv('data/Train_DataSet_Label.csv').values
train_label_dict = {}
# train label 和 train dataset似乎没有对齐，通过dict暴力对齐
for i in range(len(train_label)):
	train_label_dict[train_label[i][0]] = train_label[i][1]
test_dataset = pd.read_csv('data/Test_DataSet.csv').values
submission = pd.read_csv('result.csv').values

changed_num = 0
for i in range(len(test_dataset)):
	same_labels = []
	for j in range(len(train_dataset)):
		# title或content相同
		if train_dataset[j][1] == test_dataset[i][1]                 :
			if len(same_labels) == 0:
				print('************************************************************************')
			print(str(i) + ': ' + test_dataset[i][1] + '     Train Label: ' + str(train_label_dict[train_dataset[j][0]]))
			same_labels.append(train_label_dict[train_dataset[j][0]])

	if same_labels:
		changed_num += 1
		same_label_dict = Counter(same_labels)
		num_of_label0 = same_label_dict[0]
		num_of_label1 = same_label_dict[1]
		num_of_label2 = same_label_dict[2]
		if num_of_label0 > num_of_label1 and num_of_label0 > num_of_label2:
			submission[i][1] = 0
		elif num_of_label1 > num_of_label0 and num_of_label1 > num_of_label2:
			submission[i][1] = 1
		elif num_of_label2 > num_of_label0 and num_of_label2 > num_of_label1:
			submission[i][1] = 2
		# 有相等的，暂时先不改变
		else:
			pass

submit = pd.read_csv('data/submit_example.csv')
submit['label'] = submission[:, -1]
submit.to_csv('./result_after.csv', index = None)

origin_file = pd.read_csv(str('result.csv')).values
changed_file = pd.read_csv(str('result_after.csv')).values
changed = 0
for i in range(len(origin_file)):
	if origin_file[i][1] != changed_file[i][1]:
		changed += 1
print(str(changed) + ' labels have been changed.')
print(changed_num)