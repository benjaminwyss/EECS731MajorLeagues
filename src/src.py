import numpy as np
import pandas as pd
import sklearn as skl
import matplotlib.pyplot as plt
plt.close('all')
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import r2_score
from sklearn.multioutput import MultiOutputRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor

df = pd.read_csv('../data/raw/spi_matches.csv')

df = df[['season', 'league', 'team1', 'team2', 'spi1', 'spi2', 'score1', 'score2']]

futureGames = df
df = df.dropna()
futureGames = futureGames[~futureGames.isin(df).all(1)]

df = pd.get_dummies(df, columns=['league', 'team1', 'team2'])

df['season'] = (df['season'] - 2016) / 4
df['spi1'] = df['spi1'] / 100
df['spi2'] = df['spi2'] / 100

dfDiff = df[['spi1', 'spi2', 'score1', 'score2']]
dfDiff['spi1-spi2'] = dfDiff['spi1'] - dfDiff['spi2']

Y1 = df['score1'].values
Y2 = df['score2'].values

score1 = df.pop('score1')
score2 = df.pop('score2')
df['spidiff'] = dfDiff['spi1-spi2']

Xall = df.values

Xall_train1, Xall_validate1, Yall_train1, Yall_validate1 = train_test_split(Xall, Y1, test_size=0.2, shuffle=True)
Xall_train2, Xall_validate2, Yall_train2, Yall_validate2 = train_test_split(Xall, Y2, test_size=0.2, shuffle=True)

model1 = RandomForestRegressor(max_depth=8, n_jobs=-1).fit(Xall_train1, Yall_train1)
model2 = RandomForestRegressor(max_depth=8, n_jobs=-1).fit(Xall_train2, Yall_train2)

predictions1 = model1.predict(Xall_validate1)
predictions2 = model2.predict(Xall_validate2)

print(r2_score(Yall_validate1, predictions1))
print(r2_score(Yall_validate2, predictions2))

df = pd.DataFrame(data=Xall_validate1[:, 1:3], columns=['spi1', 'spi2'])
df['spidiff'] = df['spi1'] - df['spi2']
df['score1'] = pd.DataFrame(data=Yall_validate1)
df['score2'] = pd.DataFrame(data=Yall_validate2)
df['pred_score1'] = pd.DataFrame(data=predictions1)
df['pred_score2'] = pd.DataFrame(data=predictions2)

print(df)

