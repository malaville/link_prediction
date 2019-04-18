from IPython.display import clear_output
import pandas as pd
import random
import networkx as nx
import numpy as np

def isInv(inv):
    return inv > INVTHRESHOLDINT
def isVent(v):
    return 0 < v < INVTHRESHOLDINT

def isCandidate70(G70, v, i) :
    if isVent(i) or isInv(v):
        print("Not in good order")
    return (i not in G70[v]) and (v not in G70[i])

def isTarget(G70, G100, v, i):
    if isVent(i) or isInv(v):
        print("Not in good order")
    return isCandidate(G70,v,i) and G100.has_edge(v,i) or G100.has_edge(i,v)

def fast_predict_pref70(G, v, i, THRESHOLD) :
    return  G70.degree(v)*G70.degree(i) > THRESHOLD*51910

def pref_attach70(edge):
    return (G70.degree(edge[0])*G70.degree(edge[1])/51910)

def shortest_path70(edge) :
    v,i = edge
    try :
        d = nx.shortest_path_length(G70, v ,i)
        return d
    except :
        return 20
    
def shortest_path_linked70(edge) :
    v,i = edge
    try :
        d = nx.shortest_path_length(G70, v ,i)
        return 1
    except :
        return 0
    
def degree70(v):
    return G70.degree(v)

def mean_degree70(nod) :
    degrees = []
    for neigh in G70.neighbors(nod) :
        degrees.append(degree(neigh))
    return(sum(degrees)/len(degrees))

def get_amount70(v,i):
    return G70[v][i]['corrected_amount']

def mean_investment70(nod) :
    investments = []
    for neigh in G70.neighbors(nod) :
        investments.append(get_amount(nod,neigh))
    return(sum(investments)/len(investments))

def progress(x, y, wait=True):
    clear_output(wait=wait)
    perc = round(100*x/y,1)
    string ="% [" + "="*round(perc/2) + " "*(50-round(perc/2)) + "]"
    print("Progression : {:>5}".format(perc) + string)
    
def dataframe_for_training(not_target_links, target_links, GR):
    
    import pandas as pd
    import random
    import networkx as nx
    import numpy as np
    
                # PREPARING FUNCTIONS #
    

    def pref_attach(edge):
        return (GR.degree(edge[0])*GR.degree(edge[1]))

    def shortest_path(edge) :
        v,i = edge
        try :
            d = nx.shortest_path_length(GR, v ,i)
            return d
        except :
            return 20

    def shortest_path_linked(edge) :
        v,i = edge
        try :
            d = nx.shortest_path_length(GR, v ,i)
            return 1
        except :
            return 0

    def degree(v):
        return GR.degree(v)

    def mean_degree(nod) :
        degrees = []
        for neigh in GR.neighbors(nod) :
            degrees.append(degree(neigh))
        return(sum(degrees)/len(degrees))

    def get_amount(v,i):
        return GR[v][i]['corrected_amount']

    def mean_investment(nod) :
        investments = []
        for neigh in GR.neighbors(nod) :
            investments.append(get_amount(nod,neigh))
        return(sum(investments)/len(investments))
    
    ##
    
                # PREPARING DATA #
                
    ##
    
    Nc = len(not_target_links)
    Nt = len(target_links)
    
    Y = np.vstack([np.zeros((Nc,1), int), np.ones((Nt,1), int)])
    X = np.vstack([np.array(list(not_target_links)), np.array(list(target_links))])

    df = pd.DataFrame(np.hstack([Y,X]), columns=["TARGET", "VID", "IID"])

    df['VDEGREE'] = df['VID'].map(degree)
    df['IDEGREE'] = df['IID'].map(degree)

    df['VMAI'] = df['VID'].map(mean_investment)
    df['IMAI'] = df['IID'].map(mean_investment)

    df['LVMAI'] = np.log(df['VMAI'] + 1)
    df['LIMAI'] = np.log(df['IMAI'] + 1)

    df['VMND'] = df['VID'].map(mean_degree)
    df['IMND'] = df['IID'].map(mean_degree)

    df['PREF'] = df[['VID', 'IID']].apply(pref_attach, axis=1)
    df['SHORT'], df['LINKED'] = df[['VID','IID']].apply(shortest_path, axis=1),df[['VID','IID']].apply(shortest_path_linked, axis=1)

    return df

def dataframe_for_training_with_infos(not_target_links, target_links, GR, descs_dataframe):
    return dataframe_for_training(not_target_links, target_links, GR)