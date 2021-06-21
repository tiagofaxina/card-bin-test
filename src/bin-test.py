from re import compile, match
from time import time
import numpy as np
import cupy as cp
import pandas as pd

start_total = time()

df = pd.read_excel('data/binlist-data.xlsx', 'binlist-data')

brl_amex_rows_df = df.loc[(df['alpha_3'] == 'BRA') & (df['brand'] == 'AMERICAN EXPRESS')]
# brl_amex_rows_df = brl_rows_df.loc[brl_rows_df['brand'] == 'AMERICAN EXPRESS']

brl_amex_bins_df = brl_amex_rows_df['bin']

print('brl_amex_rows_df') 
print(brl_amex_rows_df) 

print('brl_amex_bins_df') 
print(brl_amex_bins_df) 
brl_amex_bins = np.array(brl_amex_bins_df, dtype='int64')

print('brl_amex_bins') 
print(brl_amex_bins) 