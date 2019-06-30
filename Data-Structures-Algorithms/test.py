#bubble Sort

import pandas as pd 

train = pd.read_csv('/Users/praneeshkhanna/Documents/ibm/surge_old/surge_release/surge_driver/output_data/feature_train_df.csv')

print(train.columns)
print('\n\n\n')
print(train.index)
train.index.names = ['amid']

print(train.index)

train = train.reset_index(drop=False)
# train = train.rename(columns={index_name:'amid'})
print('\n\n\n\n\n\n\n\nAfter resetting the index\n\n\n\n\n\n')
print(train.columns)