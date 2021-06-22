from re import compile, match
from time import time
import numpy as np
import cupy as cp
import pandas as pd

start_total = time()

df = pd.read_excel('data/binlist-data.xlsx', 'binlist-data')

# brl_hipercard_rows_df = df.loc[(df['alpha_3'] == 'BRA') & (df['brand'] == 'HIPERCARD')]
brl_hipercard_rows_df = df.loc[(df['brand'] == 'HIPERCARD')]

brl_hipercard_bins_df = brl_hipercard_rows_df['bin']

brl_hipercard_bins = np.array(brl_hipercard_bins_df, dtype='int64')

file_object_invalid = open('results/hipercard/hipercard_invalid.txt', 'a')

# hipercard_pattern = compile(r"^(606282)|(3841)")
hipercard_pattern = compile(r"^((606282)|(3841)|(637095)|(637612)|(637599)|(637609)|(637568))")

for card_bin in brl_hipercard_bins:
  start = time()
  if match(hipercard_pattern, str(card_bin)) is None:
    file_object_invalid.write(str(card_bin))
    file_object_invalid.write("\n")

end_total = time()
print(end_total - start_total)

file_object_invalid.close()