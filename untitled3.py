import numpy as np
import glob
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import scipy.cluster.hierarchy as sch
df=pd.read_csv(r'F:\explo\daily_dataset.csv\daily_dataset.csv')
counts=df['LCLid'].value_counts()
print(counts)
dff=df[df['LCLid'].isin(counts[counts>729].index)]
c=dff['LCLid'].value_counts()
print(c)
print(c.describe())
#print(counts)
counts=pd.Series.to_frame(dff['LCLid'].value_counts())
#print(counts)
df2=pd.DataFrame(columns=['id','value'])

df2['id']=dff['LCLid']
df2['value']=dff['energy_sum']
#print(df2)
g=df2.groupby('id').mean()
g.reset_index(inplace=True)
#print(g)
#x=pd.DataFrame(columns=['i'])
#x['i']=
#x=g
#g=g.drop('id',axis=1)
#dendrogram=sch.dendrogram((sch.linkage(g,method="ward")))