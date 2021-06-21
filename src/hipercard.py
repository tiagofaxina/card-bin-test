from re import compile, match
from time import time
import numpy as np
import cupy as cp
import pandas as pd

start_total = time()

df = pd.read_excel('data/binlist-data.xlsx', 'binlist-data')

brl_hipercard_rows_df = df.loc[(df['alpha_3'] == 'BRA') & (df['brand'] == 'HIPERCARD')]

brl_hipercard_bins_df = brl_hipercard_rows_df['bin']

brl_hipercard_bins = np.array(brl_hipercard_bins_df, dtype='int64')

binsMatched = cp.array([])
binsNotMatched = cp.array([])

hipercard_pattern = compile(r"^(606282)|(3841)")

for bin_number in brl_hipercard_bins:
  start = time()
  if match(hipercard_pattern, str(bin_number)) is None:
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