from re import compile, match
from time import time
import numpy as np
import cupy as cp
import pandas as pd

start_total = time()

df = pd.read_excel('data/binlist-data.xlsx', 'binlist-data')

brl_amex_rows_df = df.loc[(df['alpha_3'] == 'BRA') & (df['brand'] == 'AMERICAN EXPRESS')]

brl_amex_bins_df = brl_amex_rows_df['bin']

brl_amex_bins = np.array(brl_amex_bins_df, dtype='int64')

binsMatched = cp.array([])
binsNotMatched = cp.array([])

amex_pattern = compile(r"^3[47]")

for bin_number in brl_amex_bins:
  start = time()
  if match(amex_pattern, str(bin_number)) is None:
    binsNotMatched = cp.append(binsNotMatched, bin_number)
  else:
    binsMatched = cp.append(binsMatched, bin_number)

print('binsNotMatched') 
print(binsNotMatched) 
print(len(binsNotMatched)) 

print('binsMatched') 
print(binsMatched) 
print(len(binsMatched))

end_total = time()
print(end_total - start_total)