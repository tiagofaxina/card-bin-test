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

file_object_invalid = open('results/amex/amex_invalid.txt', 'a')

amex_pattern = compile(r"^3[47]")

for card_bin in brl_amex_bins:
  start = time()
  if match(amex_pattern, str(card_bin)) is None:
    file_object_invalid.write(str(card_bin))
    file_object_invalid.write("\n")

end_total = time()
print(end_total - start_total)

file_object_invalid.close()