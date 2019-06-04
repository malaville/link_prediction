def logPerso(x) :
    import numpy as np
    return np.log(x + 0.01)
def isPositive(x):
    return 1*(x>0)
def identity(x):
    return x
def identityTruncate(T):
    return lambda x : x if x < T else T

transformations = {
        "LOC" : {
            "initialName":"Location #startups",
            "shouldUse": False,
            "cause":"too vast"
        },
        "F_DATE" : {
            "initialName":"Founded Date",
            "shouldUse": True,
            "nbtransform" : 1,
            "farray" : [logPerso],
            "names": ["LOG_F_DATE"]
        },
        "TOTFUND" : {
            "initialName":"Total Funding",
            "shouldUse" : False,
            "nbtransform" : 1,
            "farray" : [logPerso],
            "names" : ["LOG_TOTFUND"],
            "cause": "obvious reason if TOTFUND high, then bound to be invested"
        },
        "N_ROUNDS" : {
            "initialName":"Number of Rounds",
            "shouldUse" : False,
        },
        "LR_DATE" : {
            "initialName":"Last Round Date",
            "shouldUse" : False,
            "nbtransform" : 1,
            "farray" : [logPerso],
            "names" : ["LOG_LR_DATE"],
            "cause":"obvious reasons"
        },
        "FR_DATE" : {
            "initialName":"First Round Date",
            "shouldUse" : True,
            "nbtransform" : 1,
            "farray" : [logPerso],
            "names" : ["LOG_FR_DATE"]
        },
        "LR_VALUE" : {
            "initialName":"Last Round Funding",
            "shouldUse" : False ,
            "nbtransform" : 1,
            "farray" : [logPerso],
            "names" : ["LOG_LR_VALUE"],
            "cause": "not interesting"
        },
        "HAS_S" : {
            "initialName":"Has Seed",
            "shouldUse" : False ,
            "nbtransform" : 0,
            "farray" : [],
            "names" : [],
            "cause": "tout le temps vrai"
        },
        "HAS_A" : {
            "initialName":"Has A",
            "shouldUse" : False,
            "nbtransform" : 0,
            "farray" : [],
            "names" : [],
            "cause": "information leak, biased ML"
        },
        "HAS_B" : {
            "initialName":"Has B",
            "shouldUse" : False,
            "nbtransform" : 0,
            "farray" : [],
            "names" : [],
            "cause": "information leak, biased ML"
        },
        "HAS_C" : {
            "initialName":"Has C",
            "shouldUse" : False,
            "nbtransform" : 0,
            "farray" : [],
            "names" : [],
            "cause": "information leak, biased ML"
        }
        ,
        "HAS_D" : {
            "initialName":"Has D",
            "shouldUse" : False,
            "nbtransform" : 0,
            "farray" : [],
            "names" : [],
            "cause": "information leak, biased ML"
        },
        "NB_INV" : {
            "initialName":"Nb investors",
            "shouldUse" : False
        },
        "CENT" : {
            "initialName":"Centrality",
            "shouldUse" : False,
        },
        "MAXINV_CENT" : {
            "initialName":"Max Investor Centrality",
            "shouldUse" : False,
        },
        "SUM_INV_CENT" : {
            "initialName":"Sum Investor Centrality",
            "shouldUse" : False,
        },
        "MAXPORT" : {
            "initialName":"Max Portfolio",
            "shouldUse" : False,
            "nbtransform" : 2,
            "farray" : [logPerso, isPositive],
            "names" : ["LOG_MAXPORT", "MAXPORTBIN"],
            "cause" : "???"
        },
        "NBART" : {
            "initialName":"Nb articles total",
            "shouldUse" : False,
            "nbtransform" : 2,
            "farray" : [logPerso, isPositive],
            "names" : ["LOG_NBART", "NBARTBIN"],
            "cause": "data leakage"
        },
        "NEWSINC" : {
            "initialName":"News Increase",
            "shouldUse" : False,
        },
        "NBFOUNDERS" : {
            "initialName":"Nb Founders",
            "shouldUse" : True,
            "nbtransform" : 2,
            "farray" : [identityTruncate(6), isPositive],
            "names" : ["NBFOUNDERS", "HASFOUNDERS"]
        },
        "NBPREV" : {
            "initialName":"Nb Previous Startups",
            "shouldUse" : True,
            "nbtransform" : 2,
            "farray" : [identityTruncate(6), isPositive],
            "names" : ["NBPREVFOUNDED", "HASFOUNDED"]
        }
}