
import pandas as pd
from matplotlib import pyplot as plt
import numpy as npy
import seaborn as sb
from seaborn.utils import load_dataset

df = sb.load_dataset('tips') 
print (df.head())