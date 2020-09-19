import numpy as np 
import statistics

data_readtime = [33, 65, 20, 21, 22, 40, 42, 25, 35, 80, 57, 43, 62, 21, 20, 33, 33, 38, 42, 37, 23, 42, 31, 15, 19, 82]


av_readtime = round(sum(data_readtime)/len(data_readtime))
med_readtime = statistics.median(data_readtime)
print(len(data_readtime))
print(av_readtime)
print(med_readtime)
