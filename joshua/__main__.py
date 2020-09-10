from glob import glob
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
import warnings

warnings.filterwarnings('ignore')

import joshua as model

WR_FILE = 'data/2018/wr'
PLAYERS = 'data/free-agents/*'


df = pd.read_csv('data/player_stats/TE.tsv', delimiter='\t')
feats = model.features(df)
print(feats.columns)
print(feats.head())
