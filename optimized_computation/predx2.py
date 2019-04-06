#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
import sys
from IPython.display import clear_output
import os
from math import floor

# In[2]:


with open('output_data/utils.p', 'rb') as f :
    utils = pickle.load(f)
G70 = utils['G70']
G100 = utils['G100']
INVTHRESHOLDINT = utils['INVTHRESHOLDINT']
def isInv(inv):
    return inv > INVTHRESHOLDINT
def isVent(v):
    return 0 < v < INVTHRESHOLDINT
ventures = [v for v in G70.nodes() if v<INVTHRESHOLDINT]
investors = [i for i in G70.nodes() if i > INVTHRESHOLDINT]

ventures100 = [v for v in G70.nodes() if v<INVTHRESHOLDINT]
investors100 = [i for i in G70.nodes() if i > INVTHRESHOLDINT]


# In[3]:


def isCandidate(G70, v, i) :
    if isVent(i) or isInv(v):
        print("Not in good order")
    return (i not in G70[v]) and (v not in G70[i])

def isTarget(G70, G100, v, i):
    if isVent(i) or isInv(v):
        print("Not in good order")
    return isCandidate(G70,v,i) and G100.has_edge(v,i) or G100.has_edge(i,v)

def predict(G, v, i, THRESHOLD, SCORETYPE, existing_edges_, verify=False) :
    if verify and (v,i) in existing_edges_:
        print("not candidate")
        return;
    if SCORETYPE=='random' :
        return random.random() > THRESHOLD
    
    if SCORETYPE == 'pref' :
        return  G70.degree(v)*G70.degree(i) > THRESHOLD*51910
    
def fast_predict_pref(G, v, i, THRESHOLD) :    
    return  G70.degree(v)*G70.degree(i) > THRESHOLD*51910
    
def put_inv_on_right(set_of_links):
    S = set()
    r = 0
    n=0
    for v,i in set_of_links:
        if v > INVTHRESHOLDINT:
            S.add((i,v))
            r+=1
        else :
            S.add((v,i))
            n+=1
    return S

existing_edges = set(put_inv_on_right(G70.edges()))
existing_edges_100 = set(put_inv_on_right(G100.edges()))
target_edges = existing_edges_100 - existing_edges


# In[4]:


from time import time
def print_BLABLA(data) :
    with open('output_data/utils.p', 'rb') as f :
        utils = pickle.load(f)

    def print_TPFPTNFN(utils_, ventures, THRESHOLD, printing=False, fore_string = ""):
        TP = 0
        FP = 0
        FN = 0
        TN = 0
        G100 = utils_['G100']
        G70 = utils_['G70']
        INVTHRESHOLDINT = utils_['INVTHRESHOLDINT']
        investors = [i for i in G70.nodes() if i> INVTHRESHOLDINT]
        existing_edges = set(put_inv_on_right(G70.edges()))
        existing_edges_100 = set(put_inv_on_right(G100.edges()))
        target_edges = existing_edges_100 - existing_edges
        del G100, existing_edges_100
        Nv = len(ventures)
        IT = 0
        for v in ventures :
            for i in investors :
                if (v,i) not in existing_edges :
                    if fast_predict_pref(G70, v, i, THRESHOLD) :
                        if (v,i) in target_edges:
                            TP +=1
                        else :
                            FP +=1
                    else:
                        if (v,i) in target_edges:
                            FN +=1
                        else :
                            TN +=1

        recall = 0 if not(TP+FN) else TP / (TP + FN)
        precision = 0 if not(TP+FP) else TP / (TP + FP)
        F1 = 0 if not(precision+recall) else  2*(precision*recall)/(precision+recall)
        return TP, FP, TN, FN, recall, precision, F1
    
    return print_TPFPTNFN(utils, data['ventures'], data['THRESHOLD'], printing=not(data['pid']), fore_string= data['pid'])




# In[ ]:


from multiprocessing import Pool


K=int(sys.argv[1])
THRESHOLDS = [0.02, 0.04, 0.06,0.08, 0.1, 0.2] #[0.0001, 0.0002,0.0003,0.0004,0.0006,0.0008,0.0010, 0.002,0.003,0.006,0.01]


print("Running with cores : " , K)
results=[]
for THRESHOLD in THRESHOLDS:
    t0 = time()
    ventures_split = [{'ventures':ventures[i::K], 'pid':i, 'THRESHOLD':THRESHOLD} for i in range(K)]
    print("Running for Threshold :", THRESHOLD)
    if __name__ == '__main__':
        p = Pool(K)
        results.append(p.map(print_BLABLA, ventures_split))
    print(time()-t0, "secondes")
    pickle.dump(results[-1], open("output_results/results{0}.p".format(THRESHOLD), "wb"))
