from re import compile, match
from time import time
import numpy as np
import cupy as cp
import pandas as pd

start_total = time()

df = pd.read_excel('data/elo-bins.xlsx', 'elo-bins')
bins_numbers_df = df['number']

print('bins_numbers_df') 
print(bins_numbers_df) 
bins_numbers = np.array(bins_numbers_df, dtype='int64')

print('bins_numbers') 
print(bins_numbers) 

binsMatched = cp.array([])
binsNotMatched = cp.array([])

current_row = 0

# elo_pattern = compile(r"^(50(67(0[78]|1[5789]|2[012456789]|3[0123459]|4[0-7]|53|7[4-8])|9(0(0[0-9]|1[34]|2[0134567]|3[0359]|4[01235678]|5[015789]|6[012356789]|7[013]|8[1234789]|9[1379])|1(0[34568]|4[6-9]|5[1-8]|8[36789])|2(2[02]|5[7-9]|6[012356789]|7[012345689]|8[02356789]|90)|357|4(0[7-9]|1[012456789]|2[02]|5[7-9]|6[0-7]|8[45])|55[01]|636|7(2[3-8]|31|6[5-9])))|4(0117[89]|3(1274|8935)|5(1416|7(393|63[12])))|6(27780|36368|5(0(0(3[1258]|4[026]|7[78])|4(06|1[0234]|2[2-9]|3[04589]|8[5-9]|9[0-9])|5(0[01346789]|1[012456789]|2[0-9]|3[0178]|5[2-9]|6[0123567]|7[7-9]|8[0134678]|9[1-8])|72[0-7]|9(0[1-9]|1[0-9]|2[0128]|3[89]|4[6-9]|5[0158]|6[2-9]|7[01]))|1(6(5[236789]|6[025678]|7[01456789]|88)|700)|50(0[01356789]|1[2568]|3[67]|5[1267]))))$")
# elo_pattern = compile(r"^4011(78|79)|^43(1274|8935)|^45(1416|7393|763(1|2))|^50(4175|6699|67[0-6][0-9]|677[0-8]|9[0-8][0-9]{2}|99[0-8][0-9]|999[0-9])|^627780|^63(6297|6368|6369)|^65(0(0(3([1-3]|[5-9])|4([0-9])|5[0-1])|4(0[5-9]|[1-3][0-9]|8[5-9]|9[0-9])|5([0-2][0-9]|3[0-8]|4[1-9]|[5-8][0-9]|9[0-8])|7(0[0-9]|1[0-8]|2[0-7])|9(0[1-9]|[1-6][0-9]|7[0-8]))|16(5[2-9]|[6-7][0-9])|50(0[0-9]|1[0-9]|2[1-9]|[3-4][0-9]|5[0-8]))")
elo_pattern = compile(r"^(4011(78|79)|43(1274|8935)|45(1416|7393|763(1|2))|50(4175|6699|67[0-7][0-9]|9000)|50(9[0-9][0-9][0-9])|627780|63(6297|6368)|650(03([^4])|04([0-9])|05(0|1)|05([7-9])|06([0-9])|07([0-9])|08([0-9])|4([0-3][0-9]|8[5-9]|9[0-9])|5([0-9][0-9]|3[0-8])|9([0-6][0-9]|7[0-8])|7([0-2][0-9])|541|700|720|727|901)|65165([2-9])|6516([6-7][0-9])|65500([0-9])|6550([0-5][0-9])|655021|65505([6-7])|6516([8-9][0-9])|65170([0-4]))")

for bin_number in bins_numbers:
  start = time()
  if match(elo_pattern, str(bin_number)) is None:
    binsNotMatched = cp.append(binsNotMatched, bin_number)
  else:
    binsMatched = cp.append(binsMatched, bin_number)

  print("CURRENT ROW") 
  current_row += 1
  print(current_row) 
  end = time()
  print(end - start)


print('binsNotMatched') 
print(binsNotMatched) 
print(len(binsNotMatched)) 

print('binsMatched') 
print(binsMatched) 
print(len(binsMatched))

end_total = time()
print(end_total - start_total)