import pandas as pd 
import numpy as np 
import scipy as sp 
from scipy import special

#NUMPY CODE
'''
sampleArr = np.array( [[ 0, 1, 3], 
                       [ 5, 7, 9]] )
print(sampleArr)
print("the shape of this array is : ", sampleArr.shape)
print("the size of this array is : ", sampleArr.size)
'''
#PANDAS CODE
'''
coronaReader = pd.read_csv('coronaData.csv')
print(coronaReader)
'''
#SCIPY CODE
exponent = special.exp10(3)
print(exponent)
