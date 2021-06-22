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

file_object_invalid = open('results/visa/visa_invalid.txt', 'a')

visa_pattern = compile(r"^4")

for card_bin in brl_visa_bins:
  start = time()
  if match(visa_pattern, str(card_bin)) is None:
    file_object_invalid.write(str(card_bin))
    file_object_invalid.write("\n")

end_total = time()
print(end_total - start_total)

file_object_invalid.close()