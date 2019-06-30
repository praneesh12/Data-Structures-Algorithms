from datetime import datetime as dt
import pandas as pd

train_df = pd.read_csv('/Users/praneeshkhanna/Documents/ibm/surge_old/surge_release/surge_driver/output_data/feature_train_df.csv')

train_df=train_df.rename(columns={'Unnamed: 0':'amid'})
print(train_df.columns)

# import datetime
# end_date_api = dt.today().strftime('%Y-%m-%d')

# def test(date=None):
# 	try:
# 		if date==None:
# 			datelist = []
# 			date = dt.today()
# 			mylist.append(today)
# 			date = mylist[0]
		
# 		END_DATE = date - datetime.timedelta(2*90)

# 	except Exception as e:
# 		print(e)
# 	return END_DATE

# print(test())

# # date==None
# datelist = []
# print(dt.today())
# datelist.append(today)
# date = datelist[0]

# end_date_api = dt.today()
# start_date_api = end_date_api - datetime.timedelta(2*90+365)
# print(end_date_api, start_date_api)