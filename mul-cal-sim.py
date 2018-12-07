import os
import shutil
import pandas as pd
import numpy as np
import sys
import h5py

def cosin(v1,v2):
    v1 = np.mat(v1)
    v2 = np.mat(v2)
    num = float(v1*v2.T)
    denom = np.linalg.norm(v1)*np.linalg.norm(v2)
    cos = num / denom
    return cos

def l2_dis(v1,v2):
    return np.linalg.norm(v1 - v2)

def read_data():
    base_dir = os.path.expanduser("./")
    path_training = os.path.join(base_dir, 'validation.h5')

    fid_training = h5py.File(path_training,'r')

    s2_training = fid_training['sen2']
    print s2_training.shape
    label_training = fid_training['label']
    print label_training.shape

    label = np.argmax(np.array(label_training),axis=1)

    label5 = np.where(label == 5)[0]
    label8 = np.where(label == 8)[0]
    data5 = label_training[list(label5)]
    data8 = label_training[list(label8)]
    data1 = data5.reshape((data5.shape[0], -1))
    data2 = data8.reshape((data8.shape[0], -1))

    return data1,data2

data1,data2 = read_data()

###########cal similarity with multiprocessing###########
def fun_map(inTuple):
    pfea,pid = inTuple[0], inTuple[1]
    fout = open('tmp_dir/' + str(os.getpid()), 'a')
    simlay_array = []
    for jj in range(0,len(data2)):
        sim = cosin(pfea,data2[jj])
        simlay_array.append(sim)
    sort_array = np.argsort(-np.array(simlay_array))[:40]
    for cur_index in sort_array:
        if simlay_array[cur_index] < 0.8:
             break
        sim_str = '%.4f' % simlay_array[cur_index]
        fout.write(str(pid) + " " + str(cur_index) + " " + sim_str + "\n")

def fun_map2(inTuple):
    pfea,pid = inTuple[0], inTuple[1]
    fout = open('tmp_dir/' + str(os.getpid()), 'a')
    for jj in range(0,len(data2)):
        sim = cosin(pfea,data2[jj])
        if sim > 0.8:
            sim_str = '%.4f' % sim
            fout.write(str(pid) + " " + str(jj) + " " + sim_str + "\n")

if os.path.exists('tmp_dir/') == False:
    os.mkdir('tmp_dir/')

processNum = 20
from multiprocessing import Pool
pool = Pool(processes=processNum)
mapList = []
for ii in range(0,len(data1)):
    pfea = list(data1[ii])
    mapList.append((pfea,ii))
pool.map(fun_map2, mapList)

