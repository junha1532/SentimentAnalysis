import numpy as np
import pandas as pd
import random as rd
######Stanford Sentiment Treebank######################
sstb = pd.read_csv("sets/datasetSentences.txt", sep = "\t", usecols=[1])
datasetsplit = pd.read_csv("sets/datasetSplit.txt", sep = ",", usecols=[1])

sstb = pd.concat([sstb,datasetsplit], axis=1)

sstb_train = sstb[sstb["splitset_label"] == 1]
sstb_test = sstb[sstb["splitset_label"] == 2]
sstb_validation = sstb[sstb["splitset_label"] == 3]
##########Stanford Twitter Sentiment Corpus#############

skip = sorted(rd.sample(range(1600000), 1600000-80000))
sts_train = pd.read_csv("sets/training.csv", encoding = "ISO-8859-1", engine='python', sep=",", header=None, skiprows = skip)
sts_test = pd.read_csv("sets/testdata.csv", sep=",", header = None)
skip = sorted(rd.sample(range(1600000), 1600000-16000))
sts_validation = pd.read_csv("sets/training.csv", encoding = "ISO-8859-1", engine="python", sep=",", header=None, skiprows = skip)

print("lollol")