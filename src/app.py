import re
from time import time
# from flask import Flask
import numpy as np
import pandas as pd
# import ray
# import modin.numpy as np

# ray.init()
# app = Flask(__name__)

# app.config["DEBUG"] = True

xlsx = pd.ExcelFile('data/master-bins.xlsx')
df = pd.read_excel('data/master-bins.xlsx', 'master-bins')

brl_rows = df.loc[df['COUNTRY'] == 'BRA']

account_ranges = brl_rows[['ACCOUNT_RANGE_FROM', 'ACCOUNT_RANGE_TO']]


start_total = time()

intervals_numbers = np.array([])

binsMatched = np.array([])
binsNotMatched = np.array([])

master_pattern = r"^(5[1-5]|2[2-7])"

current_row = 0

for label, row in account_ranges.iterrows():
  # start = time()
  intervals_range = np.arange(row['ACCOUNT_RANGE_FROM'], row['ACCOUNT_RANGE_TO'])
  print(intervals_range) 
  for card_bin in intervals_range:
    if re.match(master_pattern, str(card_bin)):
      binsMatched = np.append(binsMatched, card_bin)
    else:
      binsNotMatched = np.append(binsNotMatched, card_bin)
  print('binsMatched') 
  print(binsMatched) 
  print('binsNotMatched') 
  print(binsNotMatched) 
  print("CURRENT ROW") 
  current_row += 1
  print(current_row) 
  # end = time()
  # print(end - start)


end_total = time()
print(end_total - start_total)


# master_pattern = '^(5[1-5]|2[2-7])'

# for bin in intervals_numbers:
#   if match(master_pattern, bin):
#     binsMatched.append(bin)
#   else:
#     binsNotMatched.append(bin)

# print('RESULT')
# print(binsMatched) 
# print(binsNotMatched) 

# @app.route('/')
# def hello():
#   print('xlsx')
#   # print(df['ACCOUNT_RANGE_FROM'])
#   # print(df['ACCOUNT_RANGE_TO'])
  
#   # intervalsNumbers = np.arange(df['ACCOUNT_RANGE_FROM'][0], df['ACCOUNT_RANGE_TO'][0] + 1)
#   account_ranges = df[['ACCOUNT_RANGE_FROM', 'ACCOUNT_RANGE_TO']]
#   account_range_from = df['ACCOUNT_RANGE_FROM'].tolist()
#   account_range_to = df['ACCOUNT_RANGE_TO'].tolist()
#   # intervalsNumbers = df.apply(lambda row: np.arange(row['ACCOUNT_RANGE_FROM'], row['ACCOUNT_RANGE_TO'])

#   intervals_numbers = np.array([])

#   print(account_ranges) 

#   for account_range in account_ranges:
#     print(account_range) 
#   #   print(account_range[0]) 
#   #   intervals_numbers = np.concatenate(intervals_numbers, np.arange(account_range[0], account_range[1]))

#   # print(account_ranges) 
#   # print(intervals_numbers) 

#   return 'hey'

# if __name__ == '__main__':
#   app.run(debug=True, host='0.0.0.0')