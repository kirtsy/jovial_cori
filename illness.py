import numpy as np
import pandas as pd
import csv
import os

def get_ill(num,filename):
    with open(filename,'r') as f:
        time = []
        PESP = []
        # i=0
        first = 1
        r = 0
        for line in f:

            if first == 1:
                for p in range(5):
                    if ((line.split(',')[p]) == ' RESP'):
                        r = p
                        first += 1
            time.append(line.split(',')[0])
            PESP.append(line.split(',')[r])
        # print("r", r)
    zero_time = []
    zero_pesp = []

    count = 1
    while count <= 60001:
        if (float(PESP[count]) == 1.0):
            zero_pesp.append(PESP[count])
            zero_time.append(time[count])
        count += 1
    # print(zero_time)
    # print(zero_pesp)

    zero_time1 = np.array(zero_time)
    # print(zero_time1.shape)
    count1 = 0
    get_time = []
    get_pesp = []
    for i in range(zero_time1.shape[0]):
        if i >= 1:
            if ((float(zero_time[i]) - float(zero_time[i - 1])) > 1.0):
                get_time.append(zero_time[i])
                get_pesp.append(zero_pesp[i])
    # print(get_time)


    zero_time2 = np.array(get_pesp)
    rate = []
    count_min = 60
    count_num = 0
    for j in range(zero_time2.shape[0]):
        count_num += 1
        if float(get_time[j]) >= count_min:
            # print(get_time[j])
            rate.append(count_num)
            count_min += 60
            count_num = 0
    # print(rate)
    w = []
    w.append(num)

    for k in range(np.array(rate).shape[0]):
        w.append(rate[k])
    # print(w)
    return w

filePath='D:/学习资料/HealthHack/data/Hackathon_Patient files/'
files= os.listdir(filePath) #得到文件夹下的所有文件名称
SIG=[]

for file in files:
	if((file.split('_')[2]=='Signals.csv')==True):
		SIG.append(file)

def illness(num,w):
    if (np.array(w).shape[0]!=8):
        print(num,"This patient type is: UNKNOWN ")
    else:
        k=2
        error=[]
        for i in range(6):
            error.append(float(w[k])-float(w[i+1]))
            k+=1
        if(np.mean(np.abs(error)))>=1.563:
            print(num, "This patient type is: Abnormal ")
        else:
            print(num, "This patient type is: Healthy ")




for i in range(np.array(SIG).shape[0]):
    w = get_ill((i+1),SIG[i])
    illness((i+1),w)