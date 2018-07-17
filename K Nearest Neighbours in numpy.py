# implement K Nearest Neighbours Classifier from scratch (using only numpy as a scientific library.)


from numpy import *
import operator

def createDataset():
    # dummy dataset
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=['A','A','B','B']
    return group,labels

