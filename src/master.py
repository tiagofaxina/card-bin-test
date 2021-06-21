from re import compile, match
from time import time
import numpy as np
import cupy as cp
import pandas as pd

df = pd.read_excel('data/master-bins.xlsx', 'master-bins')
brl_rows = df.loc[df['COUNTRY'] == 'BRA']

account_ranges = brl_rows[['ACCOUNT_RANGE_FROM', 'ACCOUNT_RANGE_TO']]

start_total = time()

binsMatched = cp.array([])
binsNotMatched = cp.array([])

current_row = 0

master_pattern = compile(r"^(5[1-5]|2[2-7])")

for label, row in account_ranges.iterrows():
  start = time()
  intervals_range = cp.arange(row['ACCOUNT_RANGE_FROM'], row['ACCOUNT_RANGE_TO'] + 1, dtype='int64')
  print(intervals_range) 
  for card_bin in intervals_range:
    if match(master_pattern, str(card_bin)) is None:
      binsNotMatched = cp.append(binsNotMatched, card_bin)
    else:
      binsMatched = cp.append(binsMatched, card_bin)

  print("CURRENT ROW") 
  current_row += 1
  print(current_row) 
  end = time()
  print(end - start)


end_total = time()
print(end_total - start_total)