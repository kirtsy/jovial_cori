import os
import sys
import numpy as np
import csv
def read_txt(filename):
	result=[]
	with open(filename,'r') as f:
		for line in f:
			result.append(list(line.strip('\n').split(';')))
	return result[0][0].split("_")[1],result[5][0].split(":")[1],result[6][0].split(":")[1]

# name="bidmc_02_Fix.txt"
# read_txt(name)

filePath = 'D:/学习资料/HealthHack/data/Hackathon_Patient files/'

files= os.listdir(filePath) #得到文件夹下的所有文件名称
txt=[]
# print(files)
for file in files:
	if((file.split('.')[1]=='txt')==True):
		txt.append(file)


print(txt)
with open("all.csv", "w", newline="") as f:
	writer = csv.writer(f)
	for line in txt:
		infor=read_txt(line)
		print(infor)
		writer.writerow(infor)

