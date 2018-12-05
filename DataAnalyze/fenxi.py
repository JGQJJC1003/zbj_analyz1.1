import time

import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from pandas import DataFrame
from sklearn.externals import joblib
company_data = pd.read_csv('company.csv')
comment_data = pd.read_csv('comments.csv')
company_data_info = company_data[['company_name','company_address','company_level','company_type','serviced_employer',
                                  'head_turn','good_rate','company_income','item_title','link_name','company_id',
                                  'ability_number1','ability_number2','ability_number3']]
#城市种类
city = company_data_info.company_address.unique()
#公司等级
level = company_data_info.company_level.unique()
#业务类型
work = company_data_info.item_title.unique()
print(city,type(city),len(city))
print(level,len(level))
print(work,len(work))