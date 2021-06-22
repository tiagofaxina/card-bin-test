from re import compile, match
from time import time
import numpy as np
import cupy as cp
import pandas as pd

start_total = time()

df = pd.read_excel('data/binlist-data.xlsx', 'binlist-data')

brl_discover_rows_df = df.loc[(df['brand'] == 'DISCOVER')]

brl_discover_bins_df = brl_discover_rows_df['bin']

brl_discover_bins = np.array(brl_discover_bins_df, dtype='int64')

file_object_invalid = open('results/discover/discover_invalid.txt', 'a')

discover_pattern = compile(r"^(6011|65|64[4-9])")

for card_bin in brl_discover_bins:
  start = time()
  if match(discover_pattern, str(card_bin)) is None:
    file_object_invalid.write(str(card_bin))
    file_object_invalid.write("\n")

end_total = time()
print(end_total - start_total)

file_object_invalid.close()
