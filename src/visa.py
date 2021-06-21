from re import compile, match
from time import time
import numpy as np
import cupy as cp
import pandas as pd

start_total = time()

df = pd.read_excel('data/binlist-data.xlsx', 'binlist-data')

brl_visa_rows_df = df.loc[(df['alpha_3'] == 'BRA') & (df['brand'] == 'VISA')]

brl_visa_bins_df = brl_visa_rows_df['bin']

brl_visa_bins = np.array(brl_visa_bins_df, dtype='int64')

binsMatched = cp.array([])
binsNotMatched = cp.array([])

visa_pattern = compile(r"^4")

for bin_number in brl_visa_bins:
  start = time()
  if match(visa_pattern, str(bin_number)) is None:
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